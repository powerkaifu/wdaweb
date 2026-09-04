import axios from 'axios'
import type {
  SiteSetting, CarouselItem, AdmissionBatch,
  CurriculumModule, TechCard, Facility,
  StudentProject, FAQItem
} from '@/types'

// 優先使用環境變數 VITE_API_BASE_URL (如 Render 後端網址)，否則 fallback 至 '/api/v1'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const api = {
  getSiteSettings: () => apiClient.get<SiteSetting>('/public/site-settings').then(res => res.data),
  getCarousels: () => apiClient.get<CarouselItem[]>('/public/carousels').then(res => res.data),
  getBatches: () => apiClient.get<AdmissionBatch[]>('/public/batches').then(res => res.data),
  trackBatchClick: (id: number) => apiClient.post(`/public/batches/${id}/click`),
  getCurriculumModules: () => apiClient.get<CurriculumModule[]>('/public/curriculum/modules').then(res => res.data),
  getTechCards: () => apiClient.get<TechCard[]>('/public/curriculum/tech-cards').then(res => res.data),
  getFacilities: () => apiClient.get<Facility[]>('/public/facilities').then(res => res.data),
  getProjects: (featured?: boolean) => apiClient.get<StudentProject[]>('/public/projects', { params: { featured } }).then(res => res.data),
  trackProjectView: (id: number) => apiClient.post(`/public/projects/${id}/view`),
  getFAQs: () => apiClient.get<FAQItem[]>('/public/faqs').then(res => res.data),
}

