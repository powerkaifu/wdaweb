import logging
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.html import format_html
from django.utils import timezone
from unfold.admin import ModelAdmin
from .models import (
    Carousel, AdmissionBatch, CurriculumModule, TechCard,
    Facility, StudentProject, FAQ, SiteSetting
)

logger = logging.getLogger(__name__)

class SafeUploadAdminMixin:
    """
    安全上傳與儲存防護 Mixin：
    攔截雲端圖床 (Cloudinary) 通訊逾時、憑證錯誤或網路中斷異常，
    以 Django messages.error 友善呈現具體問題，絕不讓管理員面對 Server Error (500)。
    """
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        try:
            return super().changeform_view(request, object_id, form_url, extra_context)
        except Exception as e:
            logger.error(f"[Admin 操作異常] 表單儲存失敗: {e}", exc_info=True)
            messages.error(
                request,
                f"❌ 儲存失敗！若您正嘗試上傳圖片，請檢查 Cloudinary 環境變數或網路狀態。錯誤原因：{e}"
            )
            if object_id:
                return redirect(request.path)
            return redirect('../')

@admin.register(Carousel)
class CarouselAdmin(SafeUploadAdminMixin, ModelAdmin):
    list_display = ['image_preview', 'title', 'cta_text', 'cta_link', 'sort_order', 'is_active', 'deleted_status']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    list_editable = ['sort_order', 'is_active']
    actions = ['soft_delete_selected', 'restore_selected']

    def image_preview(self, obj):
        try:
            if obj.image:
                return format_html('<img src="{}" style="max-height: 45px; border-radius: 6px;" />', obj.image.url)
        except Exception:
            pass
        return '無圖片'
    image_preview.short_description = '縮圖'

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶 (軟刪除)'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 從垃圾桶還原'


@admin.register(AdmissionBatch)
class AdmissionBatchAdmin(ModelAdmin):
    list_display = ['batch_name', 'course_code', 'applicants_ratio', 'enroll_period', 'screening_date', 'training_period', 'status_override', 'status_badge', 'last_synced_at', 'click_count', 'sort_order', 'deleted_status']
    list_filter = ['status_override']
    search_fields = ['batch_name', 'course_code']
    list_editable = ['status_override', 'sort_order']
    actions = ['soft_delete_selected', 'restore_selected', 'sync_batches_action']

    def has_add_permission(self, request):
        # 🚨 禁用手動新增期別：所有招生期別一律由台灣就業通官方爬蟲自動建立與同步，防止人為誤填
        return False

    def applicants_ratio(self, obj):
        percent = int(obj.applicants_count / obj.planned_trainees * 100) if obj.planned_trainees else 0
        return format_html(
            '<b>{}</b> / {} 人 <span style="color: {}; font-size: 11px;">({}%)</span>',
            obj.applicants_count,
            obj.planned_trainees,
            '#10b981' if percent >= 100 else '#f59e0b',
            percent
        )
    applicants_ratio.short_description = '報名 / 招訓人數'

    def sync_batches_action(self, request, queryset):
        from apps.cms.services.batch_sync import sync_admission_batches
        res = sync_admission_batches()
        if res["success"]:
            self.message_user(request, f"成功同步資料！新增 {res['created']} 筆，更新 {res['updated']} 筆。")
        else:
            self.message_user(request, f"同步失敗: {', '.join(res['errors'])}", level='ERROR')
    sync_batches_action.short_description = '🔄 從台灣就業通追蹤系統同步最新資料'

    def enroll_period(self, obj):
        return f'{obj.enroll_start_date} ~ {obj.enroll_end_date}'
    enroll_period.short_description = '報名起訖'

    def training_period(self, obj):
        return f'{obj.training_start_date} ~ {obj.training_end_date}'
    training_period.short_description = '受訓起訖'

    def status_badge(self, obj):
        st = obj.dynamic_status
        colors = {
            'open': '#10b981',
            'closing_soon': '#f59e0b',
            'full': '#ef4444',
            'screening': '#f97316',
            'preparing': '#06b6d4',
            'training': '#3b82f6',
            'upcoming': '#8b5cf6',
            'ended': '#6b7280',
            'hidden': '#374151'
        }
        labels = {
            'open': '熱烈報名中',
            'closing_soon': '即將截止',
            'full': '已額滿',
            'screening': '甄試作業中',
            'preparing': '等待開訓',
            'training': '培訓中',
            'upcoming': '尚未開始',
            'ended': '已結束',
            'hidden': '已隱藏'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 4px; font-size: 12px;">{}</span>',
            colors.get(st, '#6b7280'),
            labels.get(st, st)
        )
    status_badge.short_description = '對外狀態'

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '資料狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(CurriculumModule)
class CurriculumModuleAdmin(ModelAdmin):
    list_display = ['module_number', 'module_name', 'hours', 'category_tab', 'sort_order', 'deleted_status']
    list_filter = ['category_tab']
    search_fields = ['module_number', 'module_name', 'description']
    list_editable = ['sort_order', 'hours']
    actions = ['soft_delete_selected', 'restore_selected']

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(TechCard)
class TechCardAdmin(SafeUploadAdminMixin, ModelAdmin):
    list_display = ['icon_preview', 'tech_name', 'category_tab', 'description', 'sort_order', 'is_active', 'deleted_status']
    list_filter = ['category_tab', 'is_active']
    search_fields = ['tech_name', 'description']
    list_editable = ['sort_order', 'is_active']
    actions = ['soft_delete_selected', 'restore_selected']

    def icon_preview(self, obj):
        try:
            if obj.icon:
                return format_html('<img src="{}" style="max-height: 35px; border-radius: 4px;" />', obj.icon.url)
        except Exception:
            pass
        return '無圖標'
    icon_preview.short_description = 'Icon'

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(Facility)
class FacilityAdmin(SafeUploadAdminMixin, ModelAdmin):
    list_display = ['image_preview', 'facility_name', 'description', 'sort_order', 'is_active', 'deleted_status']
    list_filter = ['is_active']
    search_fields = ['facility_name', 'description']
    list_editable = ['sort_order', 'is_active']
    actions = ['soft_delete_selected', 'restore_selected']

    def image_preview(self, obj):
        try:
            if obj.image:
                return format_html('<img src="{}" style="max-height: 45px; border-radius: 6px;" />', obj.image.url)
        except Exception:
            pass
        return '無照片'
    image_preview.short_description = '實景照片'

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(StudentProject)
class StudentProjectAdmin(SafeUploadAdminMixin, ModelAdmin):
    list_display = ['cover_preview', 'student_name', 'project_name', 'batch_tag', 'view_count', 'is_featured', 'sort_order', 'is_active', 'deleted_status']
    list_filter = ['batch_tag', 'is_featured', 'is_active']
    search_fields = ['student_name', 'project_name']
    list_editable = ['is_featured', 'sort_order', 'is_active']
    actions = ['soft_delete_selected', 'restore_selected']

    def cover_preview(self, obj):
        try:
            if obj.cover_image:
                return format_html('<img src="{}" style="max-height: 45px; border-radius: 6px;" />', obj.cover_image.url)
        except Exception:
            pass
        return '無縮圖'
    cover_preview.short_description = '作品縮圖'

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ['category', 'question', 'sort_order', 'is_active', 'deleted_status']
    list_filter = ['category', 'is_active']
    search_fields = ['category', 'question', 'answer']
    list_editable = ['sort_order', 'is_active']
    actions = ['soft_delete_selected', 'restore_selected']

    def deleted_status(self, obj):
        return '🗑️ 垃圾桶中' if obj.deleted_at else '✅ 正常'
    deleted_status.short_description = '狀態'

    def soft_delete_selected(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
    soft_delete_selected.short_description = '🗑️ 移至垃圾桶'

    def restore_selected(self, request, queryset):
        queryset.update(deleted_at=None)
    restore_selected.short_description = '♻️ 還原'


@admin.register(SiteSetting)
class SiteSettingAdmin(SafeUploadAdminMixin, ModelAdmin):
    list_display = ['site_title', 'contact_phone', 'announcement_bar_enabled', 'gtm_id', 'ga4_measurement_id']

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()
