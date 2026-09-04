from typing import List, Optional
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.db.models import F
from apps.cms.models import (
    Carousel, AdmissionBatch, CurriculumModule, TechCard,
    Facility, StudentProject, FAQ, SiteSetting
)
from .schemas import (
    CarouselOut, AdmissionBatchOut, CurriculumModuleOut,
    TechCardOut, FacilityOut, StudentProjectOut, FAQOut,
    SiteSettingOut, ApiResponse
)

api = NinjaAPI(
    title="泰山職訓「前端網頁技術與AI應用」招生推廣系統 API",
    version="1.0.0",
    description="提供前台 Vue 3 招生網站所需要之動態資料與互動介面"
)

def get_media_url(request, field):
    if not field:
        return ""
    try:
        # 實體檔案防呆檢查：若實體檔案在磁碟中不存在，直接回傳空字串，由前端 0 延遲呈現打包資產
        if hasattr(field, 'name') and hasattr(field, 'storage') and field.name:
            if not field.storage.exists(field.name):
                return ""
        return request.build_absolute_uri(field.url)
    except Exception:
        return field.url if hasattr(field, 'url') else ""

@api.get("/public/site-settings", response=SiteSettingOut, tags=["Public 前台公開"])
def get_site_settings(request):
    setting = SiteSetting.objects.first()
    if not setting:
        setting = SiteSetting.objects.create()
    return {
        "site_title": setting.site_title,
        "site_logo_url": get_media_url(request, setting.site_logo),
        "favicon_url": get_media_url(request, setting.favicon),
        "seo_description": setting.seo_description,
        "seo_keywords": setting.seo_keywords,
        "og_image_url": get_media_url(request, setting.og_image),
        "gtm_id": setting.gtm_id,
        "ga4_measurement_id": setting.ga4_measurement_id,
        "announcement_bar_enabled": setting.announcement_bar_enabled,
        "announcement_text": setting.announcement_text,
        "announcement_link": setting.announcement_link,
        "discord_server_id": setting.discord_server_id,
        "discord_channel_id": setting.discord_channel_id,
        "discord_invite_url": setting.discord_invite_url,
        "contact_phone": setting.contact_phone,
        "contact_address": setting.contact_address,
        "footer_copyright": setting.footer_copyright
    }

@api.get("/public/carousels", response=List[CarouselOut], tags=["Public 前台公開"])
def get_carousels(request):
    qs = Carousel.objects.filter(is_active=True, deleted_at__isnull=True).order_by('sort_order', '-created_at')
    return [
        {
            "id": c.id,
            "title": c.title,
            "subtitle": c.subtitle,
            "image_url": get_media_url(request, c.image),
            "mobile_image_url": get_media_url(request, c.mobile_image),
            "image_alt": c.image_alt,
            "cta_text": c.cta_text,
            "cta_link": c.cta_link,
            "cta_target": c.cta_target,
            "sort_order": c.sort_order
        }
        for c in qs
    ]

_last_auto_sync_ts = 0

@api.get("/public/batches", response=List[AdmissionBatchOut], tags=["Public 前台公開"])
def get_batches(request):
    global _last_auto_sync_ts
    import time
    now_ts = time.time()
    # 每 30 分鐘自動嘗試一次背景非同步同步（守護執行緒，絕不阻塞前台回應速度）
    if now_ts - _last_auto_sync_ts > 1800 or not AdmissionBatch.objects.filter(deleted_at__isnull=True).exists():
        _last_auto_sync_ts = now_ts
        import threading
        try:
            from apps.cms.services.batch_sync import sync_admission_batches
            threading.Thread(target=sync_admission_batches, daemon=True).start()
        except Exception:
            pass

    qs = AdmissionBatch.objects.filter(deleted_at__isnull=True).exclude(status_override='hidden').order_by('sort_order', 'enroll_start_date')
    return [
        {
            "id": b.id,
            "batch_name": b.batch_name,
            "total_hours": b.total_hours,
            "enroll_start_date": b.enroll_start_date,
            "enroll_end_date": b.enroll_end_date,
            "screening_date": b.screening_date,
            "training_start_date": b.training_start_date,
            "training_end_date": b.training_end_date,
            "planned_trainees": b.planned_trainees,
            "applicants_count": b.applicants_count,
            "apply_url": b.apply_url,
            "course_code": b.course_code,
            "dynamic_status": b.dynamic_status,
            "status_override": b.status_override,
            "click_count": b.click_count,
            "sort_order": b.sort_order,
            "last_synced_at": b.last_synced_at
        }
        for b in qs
    ]

@api.post("/public/batches/{batch_id}/click", response=ApiResponse, tags=["Public 轉換追蹤"])
def track_batch_click(request, batch_id: int):
    get_object_or_404(AdmissionBatch, id=batch_id, deleted_at__isnull=True)
    AdmissionBatch.objects.filter(id=batch_id).update(click_count=F('click_count') + 1)
    return {"success": True, "message": "點擊已記錄"}

@api.post("/admin/batches/sync", response=ApiResponse, tags=["Admin 管理操作"])
def trigger_batches_sync(request):
    from apps.cms.services.batch_sync import sync_admission_batches
    res = sync_admission_batches()
    if res["success"]:
        return {"success": True, "message": f"同步成功！新增 {res['created']} 筆，更新 {res['updated']} 筆。"}
    return {"success": False, "message": f"同步失敗: {', '.join(res['errors'])}"}

@api.get("/public/curriculum/modules", response=List[CurriculumModuleOut], tags=["Public 前台公開"])
def get_curriculum_modules(request):
    qs = CurriculumModule.objects.filter(deleted_at__isnull=True).order_by('sort_order', 'module_number')
    return [
        {
            "id": m.id,
            "module_number": m.module_number,
            "module_name": m.module_name,
            "hours": m.hours,
            "category_tab": m.category_tab,
            "description": m.description,
            "sort_order": m.sort_order
        }
        for m in qs
    ]

@api.get("/public/curriculum/tech-cards", response=List[TechCardOut], tags=["Public 前台公開"])
def get_tech_cards(request):
    qs = TechCard.objects.filter(is_active=True, deleted_at__isnull=True).order_by('sort_order', 'id')
    return [
        {
            "id": t.id,
            "category_tab": t.category_tab,
            "tech_name": t.tech_name,
            "icon_url": get_media_url(request, t.icon),
            "image_alt": t.image_alt,
            "description": t.description,
            "sort_order": t.sort_order
        }
        for t in qs
    ]

@api.get("/public/facilities", response=List[FacilityOut], tags=["Public 前台公開"])
def get_facilities(request):
    qs = Facility.objects.filter(is_active=True, deleted_at__isnull=True).order_by('sort_order', 'id')
    return [
        {
            "id": f.id,
            "facility_name": f.facility_name,
            "description": f.description,
            "image_url": get_media_url(request, f.image),
            "image_alt": f.image_alt,
            "sort_order": f.sort_order
        }
        for f in qs
    ]

@api.get("/public/projects", response=List[StudentProjectOut], tags=["Public 前台公開"])
def get_student_projects(request, featured: Optional[bool] = None):
    qs = StudentProject.objects.filter(is_active=True, deleted_at__isnull=True)
    if featured is not None:
        qs = qs.filter(is_featured=featured)
    qs = qs.order_by('-is_featured', 'sort_order', '-created_at')
    return [
        {
            "id": p.id,
            "student_name": p.student_name,
            "batch_tag": p.batch_tag,
            "project_name": p.project_name,
            "cover_image_url": get_media_url(request, p.cover_image),
            "image_alt": p.image_alt or p.project_name,
            "demo_url": p.demo_url,
            "github_url": p.github_url,
            "view_count": p.view_count,
            "is_featured": p.is_featured,
            "sort_order": p.sort_order
        }
        for p in qs
    ]

@api.post("/public/projects/{project_id}/view", response=ApiResponse, tags=["Public 轉換追蹤"])
def track_project_view(request, project_id: int):
    get_object_or_404(StudentProject, id=project_id, deleted_at__isnull=True)
    StudentProject.objects.filter(id=project_id).update(view_count=F('view_count') + 1)
    return {"success": True, "message": "瀏覽次數已累計"}

@api.get("/public/faqs", response=List[FAQOut], tags=["Public 前台公開"])
def get_faqs(request):
    qs = FAQ.objects.filter(is_active=True, deleted_at__isnull=True).order_by('sort_order', 'id')
    return [
        {
            "id": faq.id,
            "category": faq.category,
            "question": faq.question,
            "answer": faq.answer,
            "sort_order": faq.sort_order
        }
        for faq in qs
    ]

