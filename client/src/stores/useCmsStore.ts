import { defineStore } from 'pinia'
import { ref } from 'vue'
import { api } from '@/api/client'
import type {
  SiteSetting, CarouselItem, AdmissionBatch,
  CurriculumModule, TechCard, Facility,
  StudentProject, FAQItem
} from '@/types'

const CACHE_KEY = 'wdaweb_cms_cache_v1'

// 預設靜態快照 (確保 0.01 秒秒開與 Render 後端休眠冷啟動零等待體驗)
const defaultSettings: SiteSetting = {
  site_title: '泰山職訓－前端網頁技術與AI應用',
  site_logo_url: '',
  favicon_url: '',
  seo_description: '從零開始的網頁設計課程，政府自辦待業者完全免費，920小時培訓前端開發工程師職能。',
  seo_keywords: '前端網頁, AI應用, Vue, 職訓, 泰山職業訓練場, 免費課程, 生活津貼',
  og_image_url: '',
  gtm_id: '',
  ga4_measurement_id: '',
  announcement_bar_enabled: true,
  announcement_text: '第 1 期招生中 ｜ 待業民眾可申請全額免費受訓與生活津貼',
  announcement_link: '#batches',
  discord_server_id: '463880731828158464',
  discord_channel_id: '',
  discord_invite_url: 'https://discord.gg/TrerFKG',
  contact_phone: '(02) 2901-8274',
  contact_address: '新北市泰山區貴子里致遠新村 55 之 1 號',
  footer_copyright: '本網站為前端班師資自主推廣與學員成果展示網頁'
}

const defaultCarousels: CarouselItem[] = [
  {
    id: 1,
    title: '從零開始的前端工程師養成',
    subtitle: '政府自辦 920 小時紮實培訓 ｜ 待業者完全免費 ｜ 輔導就業與生活津貼',
    image_url: '',
    mobile_image_url: '',
    image_alt: '泰山職訓前端網頁技術與AI應用班主視覺',
    cta_text: '立即線上報名',
    cta_link: '#batches',
    cta_target: '_self',
    sort_order: 1
  },
  {
    id: 2,
    title: '現代前端框架與 AI 協同開發',
    subtitle: '一人兩機雙螢幕教學設備 ｜ 打造 AI 應用的優秀作品集 ｜ 跨領域轉職最佳起點',
    image_url: '',
    mobile_image_url: '',
    image_alt: '泰山職訓雙螢幕教室實境',
    cta_text: '立即線上報名',
    cta_link: '#batches',
    cta_target: '_self',
    sort_order: 2
  },
  {
    id: 3,
    title: '打造專屬的個人全端作品集',
    subtitle: '獨立完成全端架構 ｜ 實踐 AI 工具輔助開發 ｜ 累積求職競爭力的實戰作品集',
    image_url: '',
    mobile_image_url: '',
    image_alt: '泰山職訓跨領域轉職前端網頁成果',
    cta_text: '立即線上報名',
    cta_link: '#batches',
    cta_target: '_self',
    sort_order: 3
  }
]

const defaultBatches: AdmissionBatch[] = [
  {
    id: 1,
    batch_name: '前端網頁技術與AI應用 (第 1 期)',
    total_hours: 920,
    enroll_start_date: '2025-12-04',
    enroll_end_date: '2026-02-25',
    screening_date: '2026-03-11',
    training_start_date: '2026-03-25',
    training_end_date: '2026-09-10',
    planned_trainees: 24,
    applicants_count: 36,
    apply_url: 'https://its.taiwanjobs.gov.tw/Course/Detail?ID=159268',
    course_code: '159268',
    dynamic_status: 'training',
    status_override: 'auto',
    click_count: 0,
    sort_order: 1
  },
  {
    id: 2,
    batch_name: '前端網頁技術與AI應用 (第 2 期)',
    total_hours: 920,
    enroll_start_date: '2026-05-07',
    enroll_end_date: '2026-08-21',
    screening_date: '2026-09-03',
    training_start_date: '2026-09-23',
    training_end_date: '2027-03-24',
    planned_trainees: 24,
    applicants_count: 38,
    apply_url: 'https://its.taiwanjobs.gov.tw/Course/Detail?ID=159269',
    course_code: '159269',
    dynamic_status: 'screening',
    status_override: 'auto',
    click_count: 0,
    sort_order: 2
  }
]

const defaultModules: CurriculumModule[] = [
  { id: 1, module_number: 'M1', module_name: '一般與共同課程', hours: 53, category_tab: '基礎與設計', description: '就業市場分析、勞動法規與權益、性別主流化與職場倫理、職涯資源與求職準備。', sort_order: 1 },
  { id: 2, module_number: 'M2', module_name: '網頁排版編輯', hours: 160, category_tab: '基礎與設計', description: 'HTML5 語意化結構、CSS3 現代排版佈局、Bootstrap 響應式框架、RWD 跨裝置自適應設計、VS Code 開發環境配置。', sort_order: 2 },
  { id: 3, module_number: 'M3', module_name: '視覺影像設計', hours: 120, category_tab: '基礎與設計', description: 'Adobe Photoshop 數位影像編修、網頁版面視覺規劃與調色修圖、Adobe Illustrator 貝茲曲線繪圖、向量圖標與 Web Icon 製作。', sort_order: 3 },
  { id: 4, module_number: 'M4', module_name: '數位媒體應用', hours: 107, category_tab: '基礎與設計', description: '視覺傳達設計基礎、UI/UX 介面設計與使用者體驗流程、原型設計工具應用、企業參訪與業界職場體驗。', sort_order: 4 },
  { id: 5, module_number: 'M5', module_name: '網頁動態技術', hours: 240, category_tab: '前端核心與框架', description: 'JavaScript 核心語法與 ES6+、DOM 原生操作與前端動態互動、RESTful API 非同步資料串接、Git 版本控制與 GitHub 協同開發、Vue.js 漸進式框架與 Pinia 狀態管理。', sort_order: 5 },
  { id: 6, module_number: 'M6', module_name: '資料庫程式設計', hours: 80, category_tab: '後端與資料庫', description: 'NoSQL 資料庫概念與操作、MongoDB 資料管理與塑模、Node.js 執行環境、NPM 套件管理與基礎後端 API 整合測試。', sort_order: 6 },
  { id: 7, module_number: 'M7', module_name: '網頁設計實務', hours: 160, category_tab: '專案實務與作品', description: '前端專案專題製作、前後端 API 整合實務、GitHub Pages 雲端部署發布、成果簡報發表與作品集指導。', sort_order: 7 }
]

const defaultProjects: StudentProject[] = [
  { id: 1, student_name: '蔡昀容', batch_tag: '結訓成果', project_name: '夢百貨', cover_image_url: '', image_alt: '夢百貨', demo_url: 'https://blackcat0708.github.io/DreamDepartmentStore-front/#/', github_url: '', view_count: 0, is_featured: true, sort_order: 1 },
  { id: 2, student_name: '董元琪', batch_tag: '結訓成果', project_name: 'Matching TRPG', cover_image_url: '', image_alt: 'Matching TRPG', demo_url: 'https://chichitung.github.io/MatchingTRPG-front/#/', github_url: '', view_count: 0, is_featured: true, sort_order: 2 },
  { id: 3, student_name: '仲崇安', batch_tag: '結訓成果', project_name: 'Voice Land', cover_image_url: '', image_alt: 'Voice Land', demo_url: 'https://josh19961201.github.io/VoiceLand_front/#/', github_url: '', view_count: 0, is_featured: true, sort_order: 3 },
  { id: 4, student_name: '楊詠茜', batch_tag: '結訓成果', project_name: '桌下吧', cover_image_url: '', image_alt: '桌下吧', demo_url: 'https://cloris222.github.io/quasar-project/#/', github_url: '', view_count: 0, is_featured: true, sort_order: 4 },
  { id: 5, student_name: '黃姿瑄', batch_tag: '結訓成果', project_name: '團購趣', cover_image_url: '', image_alt: '團購趣', demo_url: 'https://a733181.github.io/2022-buytogether/#/', github_url: '', view_count: 0, is_featured: true, sort_order: 5 },
  { id: 6, student_name: '許凱炫', batch_tag: '結訓成果', project_name: '一個地方', cover_image_url: '', image_alt: '一個地方', demo_url: 'https://qweasd333ee.github.io/a-place-bar-front/', github_url: '', view_count: 0, is_featured: false, sort_order: 6 },
  { id: 7, student_name: '徐嘉伶', batch_tag: '結訓成果', project_name: 'AZ.ZERO', cover_image_url: '', image_alt: 'AZ.ZERO', demo_url: 'https://lisia229.github.io/AZFront/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 7 },
  { id: 8, student_name: '郭思緯', batch_tag: '結訓成果', project_name: 'Show Time', cover_image_url: '', image_alt: 'Show Time', demo_url: 'https://kkone0275.github.io/top-free-time-front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 8 },
  { id: 9, student_name: '王政文', batch_tag: '結訓成果', project_name: 'Ocean', cover_image_url: '', image_alt: 'Ocean', demo_url: 'https://nailshort.github.io/Ocean-front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 9 },
  { id: 10, student_name: '胡俊宇', batch_tag: '結訓成果', project_name: '揪遊 (JoYo)', cover_image_url: '', image_alt: '揪遊 (JoYo)', demo_url: 'https://lilmax922.github.io/JoYo-Front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 10 },
  { id: 11, student_name: '張雅涵', batch_tag: '結訓成果', project_name: 'Sunday', cover_image_url: '', image_alt: 'Sunday', demo_url: 'https://vvn719.github.io/SUNDAY-vue-project/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 11 },
  { id: 12, student_name: '黃佳琦', batch_tag: '結訓成果', project_name: '綠善生活農場', cover_image_url: '', image_alt: '綠善生活農場', demo_url: 'https://gagiherdesign.github.io/susi-front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 12 },
  { id: 13, student_name: '蔡文瑜', batch_tag: '結訓成果', project_name: 'BCoffee', cover_image_url: '', image_alt: 'BCoffee', demo_url: 'https://pato830729.github.io/BCcoffee-front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 13 },
  { id: 14, student_name: '蘇俞甄', batch_tag: '結訓成果', project_name: 'MAUNA COFFEE', cover_image_url: '', image_alt: 'MAUNA COFFEE', demo_url: 'https://a5a5aa.github.io/TSFP-front/#/', github_url: '', view_count: 0, is_featured: false, sort_order: 14 }
]

const defaultTechCards: TechCard[] = [
  { id: 1, category_tab: '基礎與排版', tech_name: 'HTML5 & CSS3', icon_url: '', image_alt: 'HTML5 & CSS3', description: '現代網頁語意標籤與進階排版', sort_order: 1 },
  { id: 2, category_tab: '基礎與排版', tech_name: 'Bootstrap & Tailwind', icon_url: '', image_alt: 'Bootstrap & Tailwind', description: '現代前端 UI 框架、快速建立高質感響應式 (RWD) 介面', sort_order: 2 },
  { id: 3, category_tab: '視覺與設計', tech_name: 'Adobe Photoshop & AI', icon_url: '', image_alt: 'Adobe Photoshop & AI', description: '影像處理修圖、Icon 圖示設計與 UI/UX 視覺傳達流程', sort_order: 3 },
  { id: 4, category_tab: '核心動態技術', tech_name: 'JavaScript (ES6+)', icon_url: '', image_alt: 'JavaScript (ES6+)', description: '原生 DOM 操作、非同步 Promise / Async-Await 與現代語法', sort_order: 4 },
  { id: 5, category_tab: '核心動態技術', tech_name: 'Vue.js 3 & Pinia', icon_url: '', image_alt: 'Vue.js 3 & Pinia', description: '組件化架構、Composition API、Vue Router 路由與狀態管理', sort_order: 5 },
  { id: 6, category_tab: '核心動態技術', tech_name: 'RESTful API & Axios', icon_url: '', image_alt: 'RESTful API & Axios', description: '前後端分離資料串接、JSON 處理與非同步請求處理', sort_order: 6 },
  { id: 7, category_tab: '環境與資料管理', tech_name: 'Node.js & MongoDB', icon_url: '', image_alt: 'Node.js & MongoDB', description: 'Node.js 執行環境、NoSQL 資料庫設計與基礎 API 開發', sort_order: 7 },
  { id: 8, category_tab: '協同開發', tech_name: 'Git & GitHub', icon_url: '', image_alt: 'Git & GitHub', description: '版本控制、分支管理、團隊協同開發與 GitHub Pages 部署', sort_order: 8 }
]

const defaultFacilities: Facility[] = [
  {
    id: 1,
    facility_name: '一人雙螢幕高階實作環境',
    description: '每位學員配置獨立雙螢幕電腦，邊看講師即時示範邊同步動手編程，學習不漏拍！',
    image_url: '',
    image_alt: '泰山職訓雙螢幕電腦教室',
    sort_order: 1
  },
  {
    id: 2,
    facility_name: '寬敞明亮專屬沉浸空間',
    description: '專屬獨立座位與高速光纖網路，提供 920 小時專注沉浸式程式開發與專題發表環境。',
    image_url: '',
    image_alt: '寬敞明亮的教室實作環境',
    sort_order: 2
  }
]

const defaultFAQs: FAQItem[] = [
  { id: 1, category: '參訓資格', question: '完全沒有寫過程式或設計背景適合報名嗎？', answer: '非常適合！本專班專為零基礎及跨領域轉職者量身打造，只要您對程式設計與 AI 應用抱持濃厚興趣即可報名。課程從最基礎的 HTML/CSS 排版與視覺設計教起，循序漸進至 JavaScript 與 Vue 3 動態框架，並深度結合生成式 AI 輔助開發，全力培養能靈活運用 AI 賦能的跨領域現代網頁設計與前端實戰人才！', sort_order: 1 },
  { id: 2, category: '參訓費用', question: '參加本訓練需要負擔學費或材料費嗎？', answer: '待業者完全免費！本課程為勞動部自辦職前訓練，政府全額補助學費與材料費。', sort_order: 2 },
  { id: 3, category: '生活津貼', question: '受訓期間可以申請職業訓練生活津貼嗎？', answer: '符合非自願離職、特定對象身分者，每月可申請基本工資 60% 之職業訓練生活津貼，最高補助 6 個月。', sort_order: 3 },
  { id: 4, category: '上課時間', question: '上課時間與地點為何？', answer: '週一至週五 08:30 ~ 16:35（全日制培訓），上課地點於勞動部泰山職業訓練場（新北市泰山區致遠新村 55 之 1 號）。', sort_order: 4 },
  { id: 5, category: '就業輔導', question: '結訓前會提供履歷健檢與作品集指導嗎？', answer: '會的！課程最後階段會由專業師資個別提供一對一履歷健檢、作品集面試優化指導，並舉辦專題成果發表會，協助學員以具備競爭力的完整作品集底氣十足接軌就業市場。', sort_order: 5 },
  {
    id: 6,
    category: '住宿申請',
    question: '外縣市或遠道學員有提供宿舍住宿嗎？申請資格與費用為何？',
    answer: `有提供！泰山職業訓練場備有學員宿舍，提供符合條件之遠道待業學員申請：

1. 申請資格：以戶籍地距離訓練場較遠（通常為 30 公里以上）之外縣市遠道學員優先，因床位有限需依規定名額審查分配。
2. 費用規定：免收房間住宿費（免房費），僅需自付基本耗能費（如冷氣費依規定計收）及繳交住宿保證金（結訓無損點交後無息退還）。
3. 宿舍環境：多為 4 人團體寢室，需自備個人盥洗用品與寢具，並遵守場區宿舍生活管理要點。

※ 實際申請流程與床位分配，請一律以錄取報到通知單及訓練場最新公告為準。`,
    sort_order: 6
  }
]

interface CmsCachePayload {
  settings?: SiteSetting
  carousels?: CarouselItem[]
  batches?: AdmissionBatch[]
  modules?: CurriculumModule[]
  techCards?: TechCard[]
  facilities?: Facility[]
  projects?: StudentProject[]
  faqs?: FAQItem[]
  savedAt?: number
}

const CACHE_TTL_MS = 24 * 60 * 60 * 1000 // 24 小時快取效期

export type NavbarStyleType = 'smart_morph' | 'full_autohide'
export type GlowMotionPreset = 'cosmic_pulse' | 'gentle_aurora' | 'quantum_radar' | 'hyperdrive_warp'

export const useCmsStore = defineStore('cms', () => {
  // 優先從 localStorage 讀取快取（含 24h TTL 檢查），若無或過期則使用預設快照 (0.01 秒秒開)
  let cachedData: CmsCachePayload | null = null
  try {
    const raw = localStorage.getItem(CACHE_KEY)
    if (raw) {
      const parsed = JSON.parse(raw) as CmsCachePayload
      if (parsed.savedAt && Date.now() - parsed.savedAt < CACHE_TTL_MS) {
        cachedData = parsed
      }
    }
  } catch (e) {}

  const settings = ref<SiteSetting>(cachedData?.settings || defaultSettings)
  const carousels = ref<CarouselItem[]>(cachedData?.carousels || defaultCarousels)
  const batches = ref<AdmissionBatch[]>(cachedData?.batches || defaultBatches)
  const modules = ref<CurriculumModule[]>(cachedData?.modules || defaultModules)
  const techCards = ref<TechCard[]>(cachedData?.techCards || defaultTechCards)
  const facilities = ref<Facility[]>(cachedData?.facilities || defaultFacilities)
  const projects = ref<StudentProject[]>(cachedData?.projects || defaultProjects)
  const faqs = ref<FAQItem[]>(cachedData?.faqs || defaultFAQs)

  const isLiveConnected = ref(false)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  // 背景靜默非同步喚醒後端 API 並更新最新狀態
  async function fetchAll() {
    isLoading.value = true
    error.value = null
    try {
      const [
        settingsRes,
        carouselsRes,
        batchesRes,
        modulesRes,
        techCardsRes,
        facilitiesRes,
        projectsRes,
        faqsRes
      ] = await Promise.all([
        api.getSiteSettings().catch(() => null),
        api.getCarousels().catch(() => null),
        api.getBatches().catch(() => null),
        api.getCurriculumModules().catch(() => null),
        api.getTechCards().catch(() => null),
        api.getFacilities().catch(() => null),
        api.getProjects().catch(() => null),
        api.getFAQs().catch(() => null),
      ])

      if (settingsRes) settings.value = settingsRes
      if (Array.isArray(carouselsRes)) carousels.value = carouselsRes
      if (Array.isArray(batchesRes)) batches.value = batchesRes
      if (Array.isArray(modulesRes)) modules.value = modulesRes
      if (Array.isArray(techCardsRes)) techCards.value = techCardsRes
      if (Array.isArray(facilitiesRes)) facilities.value = facilitiesRes
      if (Array.isArray(projectsRes)) projects.value = projectsRes
      if (Array.isArray(faqsRes)) faqs.value = faqsRes

      const hasValidData = !!(settingsRes || batchesRes || carouselsRes)
      isLiveConnected.value = hasValidData

      // 儲存最新快照到 localStorage
      try {
        const payload: CmsCachePayload = {
          settings: settings.value,
          carousels: carousels.value,
          batches: batches.value,
          modules: modules.value,
          techCards: techCards.value,
          facilities: facilities.value,
          projects: projects.value,
          faqs: faqs.value,
          savedAt: Date.now()
        }
        localStorage.setItem(CACHE_KEY, JSON.stringify(payload))
      } catch (e) {}
    } catch (err: unknown) {
      error.value = err instanceof Error ? err.message : '後端 API 連線異常'
      console.warn('CMS API 背景載入提示（目前使用即時離線快照呈現）:', err)
    } finally {
      isLoading.value = false
    }
  }

  async function trackBatchClick(id: number) {
    try {
      await api.trackBatchClick(id)
      const target = batches.value.find(b => b.id === id)
      if (target) target.click_count++
    } catch (e) {}
  }

  async function trackProjectView(id: number) {
    try {
      await api.trackProjectView(id)
      const target = projects.value.find(p => p.id === id)
      if (target) target.view_count++
    } catch (e) {}
  }

  // 全站導覽列風格狀態 (2 種風格隨時切換並持久化)
  const NAVBAR_STYLE_KEY = 'wda_navbar_style'
  const savedNavbarStyle = (localStorage.getItem(NAVBAR_STYLE_KEY) as NavbarStyleType) || 'smart_morph'
  const activeNavbarStyle = ref<NavbarStyleType>(savedNavbarStyle)

  function setNavbarStyle(style: NavbarStyleType) {
    activeNavbarStyle.value = style
    try {
      localStorage.setItem(NAVBAR_STYLE_KEY, style)
    } catch (e) {}
  }

  // 全站邊框光芒動效風格 (4 大頂級動態物理預設 + 速度乘數)
  const GLOW_PRESET_KEY = 'wda_glow_preset'
  const GLOW_SPEED_KEY = 'wda_glow_speed'

  const savedGlowPreset = (localStorage.getItem(GLOW_PRESET_KEY) as GlowMotionPreset) || 'cosmic_pulse'
  const activeGlowPreset = ref<GlowMotionPreset>(savedGlowPreset)

  const savedGlowSpeed = parseFloat(localStorage.getItem(GLOW_SPEED_KEY) || '1.0')
  const glowSpeedMultiplier = ref<number>(isNaN(savedGlowSpeed) ? 1.0 : savedGlowSpeed)

  function applyGlowSpeedCssVar(multiplier: number) {
    if (typeof document !== 'undefined') {
      document.documentElement.style.setProperty('--glow-speed-mult', String(multiplier))
    }
  }

  // 立即套用持久化之速度係數到 CSS 變數
  applyGlowSpeedCssVar(glowSpeedMultiplier.value)

  function setGlowPreset(preset: GlowMotionPreset) {
    activeGlowPreset.value = preset
    try {
      localStorage.setItem(GLOW_PRESET_KEY, preset)
    } catch (e) {}
  }

  function setGlowSpeedMultiplier(multiplier: number) {
    glowSpeedMultiplier.value = multiplier
    applyGlowSpeedCssVar(multiplier)
    try {
      localStorage.setItem(GLOW_SPEED_KEY, String(multiplier))
    } catch (e) {}
  }

  // =========================================================================
  // 🌌 3D 宇宙深空星雲與微塵 4 大核心物理特性開關
  // =========================================================================
  const nebulaFeatures = ref({
    mouseParallax: true,    // 1. 游標引力透鏡視差
    filamentNoise: true,    // 2. 絲狀雲氣纖維紋理
    entangledPulse: true,   // 3. 引力波能量交織呼吸
    scrollWarp: false,      // 4. 滾動深空穿梭推進 (已停用，保持閱讀平穩舒適)
  })

  // =========================================================================
  // 🌠 Awwwards 級 360° 天球仰望偶發流星物理系統
  // =========================================================================
  const meteorConfig = ref({
    enabled: true,
    mode: 'sporadic' as 'sporadic' | 'shower' | 'fireball',     // 'sporadic' (8~22s 偶發) | 'shower' (2~5s 流星雨) | 'fireball' (純火流星)
    direction: 'omnidirectional' as 'omnidirectional' | 'radiant' | 'diagonal', // 'omnidirectional' (360° 四面八方) | 'radiant' (天頂向外放射) | 'diagonal' (經典斜掠)
    fireballChance: 0.25,                                     // 25% 機率微爆火流星
    manualTriggerCount: 0                                     // 手動立即發射計數器
  })

  function triggerMeteor() {
    meteorConfig.value.manualTriggerCount++
  }

  function setMeteorMode(mode: 'sporadic' | 'shower' | 'fireball') {
    meteorConfig.value.mode = mode
  }

  function setMeteorDirection(dir: 'omnidirectional' | 'radiant' | 'diagonal') {
    meteorConfig.value.direction = dir
  }

  return {
    activeNavbarStyle,
    setNavbarStyle,
    activeGlowPreset,
    glowSpeedMultiplier,
    setGlowPreset,
    setGlowSpeedMultiplier,
    nebulaFeatures,
    meteorConfig,
    triggerMeteor,
    setMeteorMode,
    setMeteorDirection,
    settings,
    carousels,
    batches,
    modules,
    techCards,
    facilities,
    projects,
    faqs,
    isLiveConnected,
    isLoading,
    error,
    fetchAll,
    trackBatchClick,
    trackProjectView,
  }
})
