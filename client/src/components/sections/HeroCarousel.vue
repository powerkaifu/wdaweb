<template>
  <!-- 全裝置 100dvh 首屏極致滿版架構 (Navbar + 最新快訊 + Hero Banner 剛好滿版一整屏) -->
  <section id="hero" class="relative min-h-[100dvh] lg:h-[100dvh] lg:max-h-[100dvh] flex flex-col justify-between pt-24 sm:pt-28 lg:pt-32 pb-4 overflow-hidden bg-transparent">
    <!-- Background Decorative Glow -->
    <div class="absolute -top-40 -left-40 w-96 h-96 bg-cyan-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 -right-40 w-96 h-96 bg-blue-600/15 rounded-full blur-3xl pointer-events-none"></div>

    <!-- 1. Top Section: Announcement Bar (使用 translate-y 向下微移，100% 絕不推擠下方內容) -->
    <div
      v-if="showAnnouncementBar"
      class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 w-full flex-shrink-0 translate-y-3 sm:translate-y-5 lg:translate-y-6"
    >
      <a
        v-if="isExternalUrl(store.settings?.announcement_link)"
        :href="store.settings.announcement_link"
        target="_blank"
        rel="noopener noreferrer"
        class="group flex items-center justify-between p-2.5 sm:p-3.5 rounded-2xl bg-gradient-to-r from-cyan-950/80 via-blue-950/80 to-slate-900/80 border border-cyan-500/30 hover:border-cyan-500/60 shadow-lg shadow-cyan-950/30 backdrop-blur-md transition-all"
      >
        <div class="flex items-center space-x-3 overflow-hidden">
          <span class="flex-shrink-0 px-2.5 py-1 text-xs sm:text-sm font-bold uppercase rounded-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/40">
            最新快訊
          </span>
          <span class="text-sm md:text-base font-medium text-slate-200 truncate group-hover:text-cyan-300 transition-colors">
            {{ dynamicAnnouncementText }}
          </span>
        </div>
        <span class="hidden sm:inline-flex items-center text-xs font-semibold text-cyan-400 group-hover:translate-x-1 transition-transform">
          查看詳情 →
        </span>
      </a>
      <router-link
        v-else
        :to="resolveLink(store.settings?.announcement_link || '/admission')"
        class="group flex items-center justify-between p-2.5 sm:p-3.5 rounded-2xl bg-gradient-to-r from-cyan-950/80 via-blue-950/80 to-slate-900/80 border border-cyan-500/30 hover:border-cyan-500/60 shadow-lg shadow-cyan-950/30 backdrop-blur-md transition-all"
      >
        <div class="flex items-center space-x-3 overflow-hidden">
          <span class="flex-shrink-0 px-2.5 py-1 text-xs sm:text-sm font-bold uppercase rounded-full bg-cyan-500/20 text-cyan-400 border border-cyan-500/40">
            最新快訊
          </span>
          <span class="text-sm md:text-base font-medium text-slate-200 truncate group-hover:text-cyan-300 transition-colors">
            {{ dynamicAnnouncementText }}
          </span>
        </div>
        <span class="hidden sm:inline-flex items-center text-xs font-semibold text-cyan-400 group-hover:translate-x-1 transition-transform">
          查看詳情 →
        </span>
      </router-link>
    </div>
    <!-- 佔位符確保無快訊時保持上下空間平衡 -->
    <div v-else class="h-1 flex-shrink-0"></div>

    <!-- 2. Middle Section: Hero Content Carousel (內容向上微調上提，視覺重心更佳) -->
    <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 w-full relative z-10 flex-1 flex items-center my-auto -translate-y-2 sm:-translate-y-4 lg:-translate-y-6">
      <div v-if="currentSlide" class="w-full grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center py-4">
        <!-- Left Text Content (8pt 垂直律動與格式塔群組精準重構) -->
        <div id="hero-left-content" class="lg:col-span-6 flex flex-col items-center lg:items-start text-center lg:text-left self-center transform-gpu will-change-transform">
          <!-- 1. 頂部認證標籤 Badge (權威背書) -->
          <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-cyan-500/30 text-sm font-bold text-cyan-400 shadow-sm shadow-cyan-950/40 mb-3 sm:mb-3.5 lg:mb-4">
            <span>✨ 勞動部自辦職前訓練 ｜ <span class="inline-block">920 小時實體培訓</span></span>
          </div>

          <!-- 2. 主標題與副標題固定安全高度容器 (頂部定錨 0 抖動，精密貼合文案階梯高度) -->
          <div class="relative h-[185px] sm:h-[155px] lg:h-[158px] xl:h-[178px] w-full [perspective:1000px]">
            <div class="absolute inset-x-0 top-0 text-center lg:text-left [perspective:800px]">
              <h1 id="hero-main-title" class="text-3xl sm:text-4xl lg:text-4xl xl:text-5xl font-extrabold text-white tracking-tight leading-[1.2] sm:leading-[1.18] xl:leading-[1.15] [transform-style:preserve-3d] text-balance">
                <template v-for="(token, tIdx) in splitTitleTokens" :key="`token-${currentIndex}-${tIdx}`">
                  <span v-if="token.isWord" class="inline-block whitespace-nowrap">
                    <span
                      v-for="(char, cIdx) in token.chars"
                      :key="`c-${tIdx}-${cIdx}`"
                      class="hero-char inline-block will-change-transform [transform-origin:50%_100%_-10px]"
                    >{{ char }}</span>
                  </span>
                  <span
                    v-else
                    class="hero-char inline-block will-change-transform [transform-origin:50%_100%_-10px]"
                  >{{ token.chars[0] === ' ' ? '\u00A0' : token.chars[0] }}</span>
                </template>
              </h1>

              <p ref="subtitleRef" class="mt-3 sm:mt-3.5 lg:mt-3.5 xl:mt-4 text-base sm:text-base xl:text-lg text-slate-300 max-w-2xl font-normal leading-relaxed text-pretty will-change-transform">
                <template v-if="subtitleChunks.length > 1">
                  <!-- 具有「｜」三段式副標：手機端語意塊自然斷詞＋隱藏「｜」；桌機端大器單行 -->
                  <template v-for="(chunk, idx) in subtitleChunks" :key="`sub-chunk-${currentIndex}-${idx}`">
                    <span class="inline-block">{{ chunk }}</span>
                    <!-- 桌機顯示優雅「｜」分隔線 -->
                    <span
                      v-if="idx < subtitleChunks.length - 1"
                      class="hidden sm:inline text-slate-500 mx-2 select-none"
                      aria-hidden="true"
                    >｜</span>
                    <!-- 手機端：若為第一塊則自然換行，使版面呈現乾淨整齊的兩行 -->
                    <span
                      v-if="idx === 0 && subtitleChunks.length > 2"
                      class="sm:hidden block h-1"
                      aria-hidden="true"
                    ></span>
                    <!-- 手機端：若為第二塊與第三塊之間，以精緻微點「·」銜接 -->
                    <span
                      v-else-if="idx < subtitleChunks.length - 1"
                      class="sm:hidden text-cyan-400 mx-1.5 font-bold select-none"
                      aria-hidden="true"
                    >·</span>
                  </template>
                </template>
                <template v-else>
                  {{ currentSlide.subtitle }}
                </template>
              </p>
            </div>
          </div>

          <!-- 3. 行動按鈕列 (黃金間距滑落，大器飽滿) -->
          <div class="w-full sm:w-auto flex items-center justify-center lg:justify-start mt-5 sm:mt-6 lg:mt-6 xl:mt-7">
            <a
              v-if="isExternalUrl(currentSlide.cta_link)"
              :href="currentSlide.cta_link"
              :target="currentSlide.cta_target || '_blank'"
              rel="noopener noreferrer"
              class="w-full sm:w-auto px-8 py-3.5 sm:px-9 sm:py-4 rounded-2xl text-base font-bold text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/45 hover:-translate-y-0.5 active:scale-95 transition-all text-center flex items-center justify-center space-x-2 group"
            >
              <span>{{ currentSlide.cta_text || '立即查看招生期別與報名資訊' }}</span>
              <span class="group-hover:translate-x-1 transition-transform">→</span>
            </a>
            <router-link
              v-else
              :to="resolveLink(currentSlide.cta_link || '/admission')"
              class="w-full sm:w-auto px-8 py-3.5 sm:px-9 sm:py-4 rounded-2xl text-base font-bold text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/45 hover:-translate-y-0.5 active:scale-95 transition-all text-center flex items-center justify-center space-x-2 group"
            >
              <span>{{ currentSlide.cta_text || '立即查看招生期別與報名資訊' }}</span>
              <span class="group-hover:translate-x-1 transition-transform">→</span>
            </router-link>
          </div>

          <!-- 4. 信任底座：水平分割線與 4 大核心指標 (大器呼吸空間與無障礙對比) -->
          <div class="w-full border-t border-slate-800/80 pt-5 sm:pt-6 mt-7 sm:mt-8 lg:mt-8 xl:mt-9 max-w-3xl">
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 sm:gap-4 xl:gap-6">
              <div class="text-center lg:text-left">
                <div class="text-2xl sm:text-3xl font-black text-cyan-400 font-mono tracking-tight">{{ display100 }}%</div>
                <div class="text-sm font-semibold text-slate-200 mt-1">待業者全額免費補助</div>
              </div>
              <div class="text-center lg:text-left">
                <div class="text-2xl sm:text-3xl font-black text-blue-400 font-mono tracking-tight">{{ display920 }}h</div>
                <div class="text-sm font-semibold text-slate-200 mt-1"><span class="inline-block">920 小時</span>實體培訓</div>
              </div>
              <div class="text-center lg:text-left">
                <div class="text-xl sm:text-2xl font-bold text-emerald-400 font-sans tracking-tight leading-8 sm:leading-9">專題實作</div>
                <div class="text-sm font-semibold text-slate-200 mt-1">累積個人專題作品</div>
              </div>
              <div class="text-center lg:text-left">
                <div class="text-xl sm:text-2xl font-bold text-purple-400 font-sans tracking-tight leading-8 sm:leading-9">生活津貼</div>
                <div class="text-sm font-semibold text-slate-200 mt-1">可申請受訓生活津貼</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Hero Visual / AI Code Generator Interactive Window (擴大為 6 欄，展現旗艦科技感) -->
        <div id="hero-right-content" class="lg:col-span-6 w-full relative self-center flex items-center justify-center transform-gpu will-change-transform">
          <Transition name="fade-slide" mode="out-in">
            <!-- 若有上傳圖片且非預設，顯示照片；否則展示頂級科技感的 AI Code Generator 互動視窗 -->
            <div v-if="currentSlide.image_url && !brokenSlideImages.has(currentSlide.id)" :key="currentSlide.image_url" class="w-full relative rounded-3xl overflow-hidden border border-slate-800/80 bg-slate-900/60 p-3 shadow-2xl shadow-cyan-950/40 backdrop-blur-xl group">
              <div class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-slate-800 flex items-center justify-center">
                <img
                  :src="currentSlide.image_url"
                  :alt="currentSlide.image_alt"
                  @error="handleSlideImgError(currentSlide.id)"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                />
              </div>
            </div>
            <!-- AI Code Generator 即時互動編輯器視窗 (方案 A) -->
            <AiCodeWindow v-else key="ai-window" />
          </Transition>
        </div>
      </div>
    </div>

    <!-- 3. Bottom Section: Carousel Indicators (進度指示點) -->
    <div class="flex justify-center items-center space-x-2.5 flex-shrink-0 py-3">
      <button
        v-if="store.carousels.length > 1"
        v-for="(slide, idx) in store.carousels"
        :key="slide.id"
        @click="switchSlide(idx)"
        :class="[
          'h-2 rounded-full transition-all duration-500',
          currentIndex === idx
            ? 'w-8 bg-gradient-to-r from-cyan-400 to-blue-500 shadow-sm shadow-cyan-500/50'
            : 'w-2 bg-slate-800 hover:bg-slate-700'
        ]"
        :aria-label="`切換到第 ${idx + 1} 張輪播`"
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, nextTick, type Ref } from 'vue'
import { useCmsStore } from '@/stores/useCmsStore'
import AiCodeWindow from '@/components/common/AiCodeWindow.vue'

const store = useCmsStore()

// 智慧快訊動態期別與顯隱邏輯：自動判斷當前開放第幾期 (每年 2 期)，無須硬編碼年度
const activeBatches = computed(() => {
  if (!store.batches || store.batches.length === 0) return []
  return store.batches.filter(b => {
    const status = b.status_override && b.status_override !== 'auto' ? b.status_override : b.dynamic_status
    return status === 'open' || status === 'closing_soon'
  })
})

const hasActiveAdmission = computed(() => {
  return activeBatches.value.length > 0
})

const dynamicAnnouncementText = computed(() => {
  const customText = store.settings?.announcement_text?.trim()
  const defaultAnnouncement = '🔥 115 年度第 1 期熱烈招生中！待業民眾享全額免費受訓與生活津貼補助！'
  // 若管理員在後台明確自訂快訊，100% 優先尊重管理員設定
  if (customText && customText !== defaultAnnouncement) {
    return customText
  }
  if (activeBatches.value.length > 0) {
    const batchLabels = activeBatches.value.map(b => {
      const match = b.batch_name.match(/第\s*\d+\s*期/)
      return match ? match[0] : b.batch_name
    })
    const batchSummary = batchLabels.join(' & ')
    return `🔥 ${batchSummary}熱烈招生中！待業民眾享全額免費受訓與生活津貼補助！`
  }
  return customText || '🔥 熱烈招生中！待業民眾享全額免費受訓與生活津貼補助！'
})

const showAnnouncementBar = computed(() => {
  if (!store.settings?.announcement_bar_enabled) return false
  return hasActiveAdmission.value
})
const currentIndex = ref(0)
const brokenSlideImages = ref<Set<number>>(new Set())

// 雙重防禦：若輪播自訂圖片 404 或載入失敗，自動優雅退回展示頂級科技感 AiCodeWindow
function handleSlideImgError(id?: number) {
  if (id !== undefined) {
    brokenSlideImages.value.add(id)
  }
}
let timer: ReturnType<typeof setInterval> | null = null
let raf1: number | null = null
let raf2: number | null = null

function isExternalUrl(url?: string): boolean {
  if (!url) return false
  return url.startsWith('http://') || url.startsWith('https://')
}

function resolveLink(link?: string): string {
  if (!link) return '/admission'
  if (link === '#batches' || link === 'batches') return '/admission'
  if (link === '#showcase' || link === 'showcase') return '/showcase'
  if (link === '#curriculum' || link === 'curriculum') return '/curriculum'
  if (link === '#community' || link === 'community') return '/community'
  if (link === '#faq' || link === 'faq') return '/faq'
  return link.startsWith('/') ? link : `/${link}`
}

// 動態計數器 (Animated Counters)
const display100 = ref(0)
const display920 = ref(0)

function animateValue(targetRef: Ref<number>, start: number, end: number, duration: number, onFrame?: (id: number) => void) {
  const startTime = performance.now()
  function step(now: number) {
    const elapsed = now - startTime
    const progress = Math.min(elapsed / duration, 1)
    // easeOutQuad 緩動函數
    const easeProgress = 1 - (1 - progress) * (1 - progress)
    targetRef.value = Math.floor(start + (end - start) * easeProgress)
    if (progress < 1) {
      const id = requestAnimationFrame(step)
      if (onFrame) onFrame(id)
    } else {
      targetRef.value = end
    }
  }
  const initialId = requestAnimationFrame(step)
  if (onFrame) onFrame(initialId)
}

const currentSlide = computed(() => {
  if (store.carousels.length === 0) {
    return {
      title: '你不需要一開始就會寫程式。重要的是，你願不願意從第一行開始。',
      subtitle: '從零開始，不代表只能靠自己摸索。在 920 小時的實體陪伴中，循序建立能真正動手完成作品的扎實能力。',
      cta_text: '立即線上報名',
      cta_link: '#batches',
      cta_target: '_self',
      image_url: '',
      image_alt: '泰山職訓前端網頁技術與AI應用班主視覺'
    }
  }
  return store.carousels[currentIndex.value]
})

// 智慧 SplitText 資料結構：中英單字混合智能拆分，防止英文單字中斷
interface SplitToken {
  isWord: boolean
  chars: string[]
}

const splitTitleTokens = computed<SplitToken[]>(() => {
  const text = currentSlide.value?.title || ''
  const regex = /([a-zA-Z0-9_#+.-]+|[\s\S])/g
  const matches = text.match(regex) || []

  return matches.map(token => ({
    isWord: /^[a-zA-Z0-9_#+.-]+$/.test(token),
    chars: token.split('')
  }))
})

// 智慧解析副標題為語意分塊（支援手機端自然分行與「｜」分隔符響應式隱藏）
const subtitleChunks = computed(() => {
  const raw = currentSlide.value?.subtitle || ''
  if (!raw) return []
  if (raw.includes('｜') || raw.includes('|')) {
    const separator = raw.includes('｜') ? '｜' : '|'
    return raw.split(separator).map(s => s.trim()).filter(Boolean)
  }
  return [raw]
})

const subtitleRef = ref<HTMLElement | null>(null)
let isSwitching = false
let currentTimeline: gsap.core.Timeline | null = null

// 切換至指定 Slide (帶 GSAP SplitText 3D 字符矩陣翻轉動畫)
const switchSlide = (targetIndex: number) => {
  if (targetIndex === currentIndex.value || isSwitching) return
  if (targetIndex < 0 || targetIndex >= store.carousels.length) return

  isSwitching = true
  resetTimer()

  const chars = document.querySelectorAll('#hero-main-title .hero-char')
  const subtitle = subtitleRef.value

  if (currentTimeline) currentTimeline.kill()
  currentTimeline = gsap.timeline({
    onComplete: () => {
      currentIndex.value = targetIndex
      nextTick(() => {
        animateSlideIn()
      })
    }
  })

  // 1. 舊字元 3D 翻轉 + 向上微移 + 粒子模糊消散
  currentTimeline
    .to(chars, {
      y: -20,
      rotateX: 60,
      opacity: 0,
      filter: 'blur(5px)',
      stagger: {
        each: 0.007,
        from: 'start'
      },
      duration: 0.32,
      ease: 'power2.in'
    }, 0)
    .to(subtitle, {
      y: -10,
      opacity: 0,
      filter: 'blur(4px)',
      duration: 0.25,
      ease: 'power2.in'
    }, 0.04)
}

// 新 Slide 字元 3D 翻正升起 + 晶透光澤浮現
const animateSlideIn = () => {
  const chars = document.querySelectorAll('#hero-main-title .hero-char')
  const subtitle = subtitleRef.value

  if (currentTimeline) currentTimeline.kill()
  currentTimeline = gsap.timeline({
    onComplete: () => {
      isSwitching = false
    }
  })

  currentTimeline
    .fromTo(chars, {
      y: 18,
      rotateX: -55,
      opacity: 0,
      filter: 'blur(6px)',
      scale: 0.96
    }, {
      y: 0,
      rotateX: 0,
      opacity: 1,
      filter: 'blur(0px)',
      scale: 1,
      stagger: {
        each: 0.016,
        from: 'start'
      },
      duration: 0.52,
      ease: 'power3.out'
    }, 0)
    .fromTo(subtitle, {
      y: 12,
      opacity: 0,
      filter: 'blur(4px)'
    }, {
      y: 0,
      opacity: 1,
      filter: 'blur(0px)',
      duration: 0.42,
      ease: 'power2.out'
    }, 0.14)
}

const startTimer = () => {
  timer = setInterval(() => {
    if (store.carousels.length > 1) {
      const nextIdx = (currentIndex.value + 1) % store.carousels.length
      switchSlide(nextIdx)
    }
  }, 8000)
}

const resetTimer = () => {
  if (timer) clearInterval(timer)
  startTimer()
}

import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

let scrollTriggerCtx: gsap.Context | null = null

onMounted(() => {
  // 啟動數字滾動動畫 (帶 RAF 清理追蹤)
  animateValue(display100, 0, 100, 1500, id => { raf1 = id })
  animateValue(display920, 0, 920, 1800, id => { raf2 = id })

  // 啟動輪播計時器
  startTimer()

  // 首頁載入時觸發初次進場 3D 字符動畫
  nextTick(() => {
    animateSlideIn()
  })

  // GSAP 滾動 Smooth Ease 速率差視差動畫
  scrollTriggerCtx = gsap.context(() => {
    // 1. 左側文字區塊速率差 (y: -40px, scrub: 1)
    gsap.to('#hero-left-content', {
      y: -40,
      ease: 'power1.out',
      scrollTrigger: {
        trigger: '#hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1
      }
    })

    // 2. 右側 AI Code 視窗速率差 (y: -20px, scrub: 1.2)
    gsap.to('#hero-right-content', {
      y: -20,
      ease: 'power1.out',
      scrollTrigger: {
        trigger: '#hero',
        start: 'top top',
        end: 'bottom top',
        scrub: 1.2
      }
    })
  })
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
  if (currentTimeline) currentTimeline.kill()
  if (raf1) cancelAnimationFrame(raf1)
  if (raf2) cancelAnimationFrame(raf2)
  if (scrollTriggerCtx) scrollTriggerCtx.revert()
})
</script>

<style scoped>
/* 標題與副標題極致絲滑的頂部定錨交叉淡入淡出 (0.4s，無高低差，無文字抖動) */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(6px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>

