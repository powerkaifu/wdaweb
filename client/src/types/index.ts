export interface SiteSetting {
  site_title: string
  site_logo_url: string
  favicon_url: string
  seo_description: string
  seo_keywords: string
  og_image_url: string
  gtm_id: string
  ga4_measurement_id: string
  announcement_bar_enabled: boolean
  announcement_text: string
  announcement_link: string
  discord_server_id: string
  discord_channel_id: string
  discord_invite_url: string
  contact_phone: string
  contact_address: string
  footer_copyright: string
}

export interface CarouselItem {
  id: number
  title: string
  subtitle: string
  image_url: string
  mobile_image_url: string
  image_alt: string
  cta_text: string
  cta_link: string
  cta_target: string
  sort_order: number
}

export interface AdmissionBatch {
  id: number
  batch_name: string
  total_hours: number
  enroll_start_date: string
  enroll_end_date: string
  screening_date?: string | null
  training_start_date: string
  training_end_date: string
  planned_trainees?: number
  applicants_count?: number
  apply_url: string
  course_code: string
  dynamic_status: 'open' | 'closing_soon' | 'full' | 'screening' | 'preparing' | 'training' | 'upcoming' | 'ended'
  status_override: string
  click_count: number
  sort_order: number
  last_synced_at?: string | null
}

export interface CurriculumModule {
  id: number
  module_number: string
  module_name: string
  hours: number
  category_tab: string
  description: string
  sort_order: number
}

export interface TechCard {
  id: number
  category_tab: string
  tech_name: string
  icon_url: string
  image_alt: string
  description: string
  sort_order: number
}

export interface Facility {
  id: number
  facility_name: string
  subtitle?: string
  description: string
  image_url: string
  image_alt: string
  sort_order: number
}

export interface StudentProject {
  id: number
  student_name: string
  batch_tag: string
  project_name: string
  cover_image_url: string
  image_alt: string
  demo_url: string
  github_url: string
  view_count: number
  is_featured: boolean
  sort_order: number
}

export interface FAQItem {
  id: number
  category: string
  question: string
  answer: string
  sort_order: number
}

