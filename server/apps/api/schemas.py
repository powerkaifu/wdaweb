from typing import List, Optional
from datetime import date, datetime
from ninja import Schema

class CarouselOut(Schema):
    id: int
    title: str
    subtitle: Optional[str] = ""
    image_url: str
    mobile_image_url: Optional[str] = ""
    image_alt: str
    cta_text: str
    cta_link: str
    cta_target: str
    sort_order: int

class AdmissionBatchOut(Schema):
    id: int
    batch_name: str
    total_hours: int
    enroll_start_date: date
    enroll_end_date: date
    screening_date: Optional[date] = None
    training_start_date: date
    training_end_date: date
    planned_trainees: int = 24
    applicants_count: int = 0
    apply_url: str
    course_code: Optional[str] = ""
    dynamic_status: str
    status_override: str
    click_count: int
    sort_order: int
    last_synced_at: Optional[datetime] = None

class CurriculumModuleOut(Schema):
    id: int
    module_number: str
    module_name: str
    hours: int
    category_tab: str
    description: str
    sort_order: int

class TechCardOut(Schema):
    id: int
    category_tab: str
    tech_name: str
    icon_url: Optional[str] = ""
    image_alt: str
    description: str
    sort_order: int

class FacilityOut(Schema):
    id: int
    facility_name: str
    subtitle: Optional[str] = ""
    description: str
    image_url: str
    image_alt: str
    sort_order: int

class StudentProjectOut(Schema):
    id: int
    student_name: str
    batch_tag: str
    project_name: str
    cover_image_url: Optional[str] = ""
    image_alt: Optional[str] = ""
    demo_url: str
    github_url: Optional[str] = ""
    view_count: int
    is_featured: bool
    sort_order: int

class FAQOut(Schema):
    id: int
    category: str
    question: str
    answer: str
    sort_order: int

class SiteSettingOut(Schema):
    site_title: str
    site_logo_url: Optional[str] = ""
    favicon_url: Optional[str] = ""
    seo_description: str
    seo_keywords: str
    og_image_url: Optional[str] = ""
    gtm_id: Optional[str] = ""
    ga4_measurement_id: Optional[str] = ""
    announcement_bar_enabled: bool
    announcement_text: str
    announcement_link: str
    discord_server_id: str
    discord_channel_id: Optional[str] = ""
    discord_invite_url: str
    contact_phone: str
    contact_address: str
    footer_copyright: str

class ApiResponse(Schema):
    success: bool
    message: str
    data: Optional[dict] = None

