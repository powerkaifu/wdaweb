from django.db import models
from django.utils import timezone
from .utils import optimize_image

class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="軟刪除時間")

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

class Carousel(SoftDeleteModel):
    title = models.CharField(max_length=200, verbose_name="輪播主標題")
    subtitle = models.TextField(blank=True, verbose_name="副標題/宣傳文案")
    image = models.ImageField(upload_to="carousels/", blank=True, null=True, verbose_name="電腦版圖片")
    mobile_image = models.ImageField(upload_to="carousels/", blank=True, null=True, verbose_name="行動版圖片")
    image_alt = models.CharField(max_length=200, verbose_name="無障礙圖片替代文字 (Alt)")
    cta_text = models.CharField(max_length=50, default="立即探索期別", verbose_name="行動按鈕文字")
    cta_link = models.CharField(max_length=200, default="#batches", verbose_name="行動按鈕連結")
    cta_target = models.CharField(
        max_length=20,
        choices=[('_self', '當前視窗 (_self)'), ('_blank', '新分頁 (_blank)')],
        default='_self',
        verbose_name="開啟方式"
    )
    sort_order = models.IntegerField(default=0, verbose_name="排序權重 (越小越前)")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="建立時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        verbose_name = "首頁輪播圖"
        verbose_name_plural = "首頁輪播圖管理"
        ordering = ['sort_order', '-created_at']

    def save(self, *args, **kwargs):
        if self.image:
            optimize_image(self.image, max_width=1920)
        if self.mobile_image:
            optimize_image(self.mobile_image, max_width=1080)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AdmissionBatch(SoftDeleteModel):
    STATUS_CHOICES = [
        ('auto', '系統自動判定'),
        ('open', '熱烈報名中'),
        ('closing_soon', '即將截止'),
        ('full', '已額滿'),
        ('screening', '甄試作業中'),
        ('preparing', '開訓準備中'),
        ('training', '培訓進行中'),
        ('upcoming', '即將開放報名'),
        ('ended', '本期已截止'),
        ('hidden', '前台隱藏'),
    ]

    batch_name = models.CharField(max_length=100, verbose_name="期別名稱 (例：第 1 期)", help_text="🤖 爬蟲自動同步：班級名稱")
    total_hours = models.IntegerField(default=920, verbose_name="總訓練時數", help_text="官方核定總訓練時數（預設 920 小時）")
    enroll_start_date = models.DateField(verbose_name="報名起始日期", help_text="🤖 爬蟲自動同步：官方報名開始日期")
    enroll_end_date = models.DateField(verbose_name="報名截止日期", help_text="🤖 爬蟲自動同步：官方報名截止日期")
    screening_date = models.DateField(null=True, blank=True, verbose_name="甄試日期", help_text="🤖 爬蟲自動同步：官方甄試日期")
    training_start_date = models.DateField(verbose_name="開訓日期", help_text="🤖 爬蟲自動同步：官方正式開訓日期")
    training_end_date = models.DateField(verbose_name="結訓日期", help_text="🤖 爬蟲自動同步：官方預計結訓日期")
    planned_trainees = models.IntegerField(default=24, verbose_name="預定招訓人數", help_text="🤖 爬蟲自動同步：官方預定招訓人數")
    applicants_count = models.IntegerField(default=0, verbose_name="目前報名人數", help_text="🤖 爬蟲自動同步：來自台灣就業通的最新報名人數")
    apply_url = models.URLField(max_length=500, verbose_name="台灣就業通官方報名網址", help_text="🤖 爬蟲自動對應之官方就業通報名連結（亦可手動覆寫）")
    course_code = models.CharField(max_length=50, blank=True, verbose_name="台灣就業通課程代碼 (例：159268)", help_text="🤖 爬蟲追蹤識別碼：以此代碼向台灣就業通爬取該班最新狀態")
    status_override = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='auto',
        verbose_name="狀態顯示模式",
        help_text="💡 建議維持「系統自動判定」（由系統依爬蟲日期動態計算）。若需緊急手動干預或強制隱藏才做變更"
    )
    click_count = models.IntegerField(default=0, verbose_name="報名點擊次數 (轉換追蹤)", help_text="📊 官網前台民眾點擊「前往報名」按鈕的累計次數（數據轉換成效）")
    sort_order = models.IntegerField(default=0, verbose_name="排序", help_text="數字越小越靠前，預設 0")
    last_synced_at = models.DateTimeField(null=True, blank=True, verbose_name="最後外部同步時間", help_text="🤖 爬蟲最後一次成功連線台灣就業通並更新資料庫的時間")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="建立時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        verbose_name = "招生期別 (爬蟲儲存)"
        verbose_name_plural = "招生期別 (🤖 台灣就業通爬蟲自動同步)"
        ordering = ['sort_order', 'enroll_start_date']

    @property
    def dynamic_status(self):
        if self.status_override != 'auto':
            return self.status_override
        
        today = timezone.now().date()
        if today < self.enroll_start_date:
            return 'upcoming'
        elif self.enroll_start_date <= today <= self.enroll_end_date:
            delta = (self.enroll_end_date - today).days
            if delta <= 7:
                return 'closing_soon'
            return 'open'
        elif self.enroll_end_date < today < self.training_start_date:
            if self.screening_date and today <= self.screening_date:
                return 'screening'
            return 'preparing'
        elif self.training_start_date <= today <= self.training_end_date:
            return 'training'
        else:
            return 'ended'

    def __str__(self):
        return f"{self.batch_name} ({self.enroll_start_date} ~ {self.enroll_end_date})"

class CurriculumModule(SoftDeleteModel):
    module_number = models.CharField(max_length=10, verbose_name="模組編號 (例：M1)")
    module_name = models.CharField(max_length=100, verbose_name="模組名稱")
    hours = models.IntegerField(verbose_name="時數 (小時)")
    category_tab = models.CharField(max_length=50, verbose_name="分類標籤 (例：基礎與設計)")
    description = models.TextField(verbose_name="課程大綱詳細說明")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="建立時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        verbose_name = "課程模組"
        verbose_name_plural = "7大課程模組管理"
        ordering = ['sort_order', 'module_number']

    def __str__(self):
        return f"{self.module_number} - {self.module_name} ({self.hours}h)"

class TechCard(SoftDeleteModel):
    category_tab = models.CharField(max_length=50, verbose_name="分類標籤")
    tech_name = models.CharField(max_length=100, verbose_name="技術名稱 (例：Vue.js 3)")
    icon = models.ImageField(upload_to="tech_icons/", blank=True, null=True, verbose_name="Icon圖標")
    image_alt = models.CharField(max_length=200, verbose_name="圖標替代文字")
    description = models.CharField(max_length=255, verbose_name="技術重點摘要")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    class Meta:
        verbose_name = "核心技術卡片"
        verbose_name_plural = "核心技術卡片管理"
        ordering = ['sort_order', 'id']

    def save(self, *args, **kwargs):
        if self.icon:
            optimize_image(self.icon, max_width=256)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tech_name

class Facility(SoftDeleteModel):
    facility_name = models.CharField(max_length=100, verbose_name="設施名稱")
    description = models.TextField(verbose_name="設施亮點說明")
    image = models.ImageField(upload_to="facilities/", blank=True, null=True, verbose_name="教室實景照片")
    image_alt = models.CharField(max_length=200, verbose_name="照片替代文字")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    class Meta:
        verbose_name = "教學設備設施"
        verbose_name_plural = "教學設備設施管理"
        ordering = ['sort_order', 'id']

    def save(self, *args, **kwargs):
        if self.image:
            optimize_image(self.image, max_width=1920)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.facility_name

class StudentProject(SoftDeleteModel):
    student_name = models.CharField(max_length=100, verbose_name="學員姓名")
    batch_tag = models.CharField(max_length=50, default="前端專班結訓成果", verbose_name="期別標籤")
    project_name = models.CharField(max_length=150, verbose_name="專題作品名稱")
    cover_image = models.ImageField(upload_to="projects/", blank=True, null=True, verbose_name="作品首頁縮圖")
    image_alt = models.CharField(max_length=200, blank=True, verbose_name="縮圖替代文字")
    demo_url = models.URLField(max_length=500, verbose_name="線上 Demo 網址")
    github_url = models.URLField(max_length=500, blank=True, verbose_name="GitHub 原始碼網址")
    view_count = models.IntegerField(default=0, verbose_name="瀏覽次數")
    is_featured = models.BooleanField(default=False, verbose_name="是否精選置頂")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="建立時間")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新時間")

    class Meta:
        verbose_name = "學員專題作品"
        verbose_name_plural = "學員作品集管理"
        ordering = ['-is_featured', 'sort_order', '-created_at']

    def save(self, *args, **kwargs):
        if self.cover_image:
            optimize_image(self.cover_image, max_width=1280)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_name} - {self.project_name}"

class FAQ(SoftDeleteModel):
    category = models.CharField(max_length=50, verbose_name="問答類別 (例：生活津貼)")
    question = models.CharField(max_length=255, verbose_name="問題題目")
    answer = models.TextField(verbose_name="解答說明")
    sort_order = models.IntegerField(default=0, verbose_name="排序")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")

    class Meta:
        verbose_name = "常見問答 (FAQ)"
        verbose_name_plural = "常見問答 (FAQ) 管理"
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"[{self.category}] {self.question}"

class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, default="泰山職訓－前端網頁技術與AI應用", verbose_name="網站標題")
    site_logo = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="全站 Logo")
    favicon = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="網站 Favicon")
    seo_description = models.TextField(default="從零開始的網頁設計課程，政府自辦待業者完全免費，920小時培訓前端開發工程師職能。", verbose_name="SEO 描述 (Description)")
    seo_keywords = models.CharField(max_length=300, default="前端網頁, AI應用, Vue, 職訓, 泰山職業訓練場, 免費課程, 生活津貼", verbose_name="SEO 關鍵字")
    og_image = models.ImageField(upload_to="site/", blank=True, null=True, verbose_name="社群分享圖 (OG Image)")
    gtm_id = models.CharField(max_length=50, blank=True, verbose_name="GTM Container ID (例：GTM-XXXXXXX)")
    ga4_measurement_id = models.CharField(max_length=50, blank=True, verbose_name="GA4 Measurement ID (例：G-XXXXXXXXXX)")
    announcement_bar_enabled = models.BooleanField(default=True, verbose_name="啟用頂部快訊跑馬條")
    announcement_text = models.CharField(max_length=255, default="🔥 115 年度第 1 期熱烈招生中！待業民眾享全額免費受訓與生活津貼補助！", verbose_name="快訊文字")
    announcement_link = models.CharField(max_length=200, default="#batches", verbose_name="快訊點擊連結")
    discord_server_id = models.CharField(max_length=50, default="463880731828158464", verbose_name="Discord Server ID")
    discord_channel_id = models.CharField(max_length=50, blank=True, verbose_name="Discord Channel ID")
    discord_invite_url = models.CharField(max_length=200, default="https://discord.gg/TrerFKG", verbose_name="Discord 邀請連結")
    contact_phone = models.CharField(max_length=50, default="(02) 2901-8274", verbose_name="諮詢電話")
    contact_address = models.CharField(max_length=200, default="新北市泰山區貴子里致遠新村 55 之 1 號", verbose_name="職訓場地址")
    footer_copyright = models.CharField(max_length=200, default="本網站為前端班師資自主推廣與學員成果展示網頁", blank=True, verbose_name="頁尾宣告 (選填)")

    class Meta:
        verbose_name = "全域站台與宣傳設定"
        verbose_name_plural = "全域站台與宣傳設定"

    def save(self, *args, **kwargs):
        if self.site_logo:
            optimize_image(self.site_logo, max_width=512)
        if self.og_image:
            optimize_image(self.og_image, max_width=1200)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.site_title
