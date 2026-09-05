<template>
  <section
    id="facilities"
    :class="[
      hideHeader
        ? 'py-8 sm:py-12 bg-transparent relative'
        : 'py-16 sm:py-24 lg:py-32 bg-transparent relative overflow-hidden'
    ]"
  >
    <!-- 頂部與底部環境發光微暈 -->
    <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
      <!-- 區塊標題 -->
      <div v-if="!hideHeader" class="text-center max-w-5xl mx-auto mb-10 sm:mb-14">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-mono font-bold uppercase tracking-wider shadow-sm mb-3">
          <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
          <span>Learning Environment ｜ 實體環境</span>
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight text-balance">
          接下來的半年，你會在這樣的地方學習
        </h2>
        <p class="text-slate-400 mt-4 text-base sm:text-lg max-w-none mx-auto leading-relaxed text-pretty">
          專注的空間、一起學習的人，以及一段真正投入的時間。
        </p>
      </div>

      <!-- 手機端橫向滑動提示 (平板與桌機隱藏) -->
      <div v-if="!hideHeader" class="flex md:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4">
        <span>👈 左右滑動瀏覽教學環境實景 👉</span>
      </div>

      <!-- 教室環境實景展示清單 (手機橫向滑軌，平板與桌機 md: 2 欄) -->
      <div
        id="facilities-cards-grid"
        class="flex md:grid md:grid-cols-2 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 md:mx-auto md:px-0 gap-4 sm:gap-6 xl:gap-8 max-w-6xl pb-4 md:pb-0"
      >
        <div
          v-for="(fac, index) in store.facilities"
          :key="fac.id"
          class="facility-card card-subsurface-glow relative rounded-3xl overflow-hidden bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between transform-gpu will-change-transform cursor-default w-[86vw] sm:w-[460px] max-w-[500px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
        >
          <!-- 角落序號水印 (01, 02) -->
          <div class="absolute -right-2 -bottom-4 text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none z-20">
            {{ String(index + 1).padStart(2, '0') }}
          </div>

          <!-- 圖片展示相框 (固定 16:10 比例) -->
          <div class="aspect-[16/10] bg-slate-800/80 relative overflow-hidden flex items-center justify-center">
            <img
              :src="getFacilityImage(fac, index)"
              :alt="fac.image_alt || fac.facility_name"
              @error="handleFacilityImgError(fac.id)"
              class="w-full h-full object-cover"
            />

            <!-- 底部微光漸層遮罩 -->
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent opacity-60"></div>
          </div>

          <!-- 說明區塊 -->
          <div class="p-6 sm:p-8 flex-1 flex flex-col relative z-10">
            <div class="flex items-center space-x-2 mb-2">
              <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
              <span class="text-sm font-mono text-cyan-400 font-bold uppercase tracking-wider">Professional Facility</span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-white mb-2 text-balance">
              {{ fac.facility_name }}
            </h3>
            <p class="text-slate-200 leading-relaxed text-base sm:text-lg text-pretty">
              {{ fac.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { createScrollStagger } from '@/utils/motion'
import { useCmsStore } from '@/stores/useCmsStore'
import facility1Img from '@/assets/facilities/learning_ijciKln_09KM7k0_ddXbwFz.webp'
import facility2Img from '@/assets/facilities/lunch_g71Ci6n_NsJ8XsZ_mJ12g5T.webp'

const defaultFacilityImages = [facility1Img, facility2Img]
const brokenFacilityIds = ref<Set<number>>(new Set())

function getFacilityImage(fac: { id?: number; image_url?: string }, index: number) {
  // 若該設施圖片已被標記載入失敗，或後端未提供有效圖片路徑，100% 穩定回傳本地高畫質實景資產
  if ((fac.id && brokenFacilityIds.value.has(fac.id)) || !fac.image_url) {
    return defaultFacilityImages[index % defaultFacilityImages.length]
  }
  return fac.image_url
}

// 雙重防禦：遠端圖片 404 或載入失敗時，立即觸發響應式降級，切換至本地實景照片
function handleFacilityImgError(facId?: number) {
  if (facId !== undefined) {
    brokenFacilityIds.value.add(facId)
  }
}

withDefaults(
  defineProps<{
    hideHeader?: boolean
  }>(),
  {
    hideHeader: false
  }
)

const store = useCmsStore()
let scrollTriggerCtx: ReturnType<typeof createScrollStagger> | null = null

function initStaggerAnimation() {
  if (scrollTriggerCtx) {
    scrollTriggerCtx.revert()
    scrollTriggerCtx = null
  }
  nextTick(() => {
    // 兩大設施卡片統一由全域工廠函式調度 (100% 全站標準一致)
    scrollTriggerCtx = createScrollStagger(
      '#facilities-cards-grid .facility-card',
      '#facilities',
      { stagger: 0.1 }
    )
  })
}

onMounted(() => {
  initStaggerAnimation()
})

// 當非同步取得後端設施資料後，重新精準綁定動畫
watch(
  () => store.facilities.length,
  () => {
    initStaggerAnimation()
  }
)

onUnmounted(() => {
  if (scrollTriggerCtx) scrollTriggerCtx.revert()
})
</script>
