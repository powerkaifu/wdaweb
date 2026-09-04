<template>
  <section id="faq" :class="hideHeader ? 'py-12 bg-slate-950 relative overflow-hidden' : 'py-24 bg-slate-950 relative overflow-hidden'">
    <!-- 頂部環境發光微暈 -->
    <div class="absolute -top-32 left-1/3 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
      <div v-if="!hideHeader" class="text-center mb-12">
        <span class="px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-bold uppercase tracking-wider">
          FAQ
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mt-4 tracking-tight">
          常見問題與解答
        </h2>
        <p class="text-slate-400 mt-4 text-base sm:text-lg">
          解答待業參訓者最關心的生活津貼、零基礎學習與就業輔導疑慮。
        </p>
      </div>

      <!-- FAQ 手風琴清單 (直接呈現完整常見問答列表，無多餘篩選) -->
      <div class="space-y-4">
        <div
          v-for="faq in store.faqs"
          :key="faq.id"
          class="rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-slate-700/80 overflow-hidden transition-[border-color,background-color,box-shadow] duration-300 shadow-md"
          :class="activeId === faq.id ? 'border-cyan-500/40 bg-slate-900' : ''"
        >
          <button
            type="button"
            :id="'faq-btn-' + faq.id"
            :aria-controls="'faq-panel-' + faq.id"
            @click="toggleFaq(faq.id)"
            class="w-full p-5 sm:p-6 text-left flex items-center justify-between space-x-4 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400"
            :aria-expanded="activeId === faq.id"
          >
            <div class="flex items-center space-x-3.5">
              <span class="px-2.5 py-1 rounded-lg bg-cyan-500/10 text-xs font-bold text-cyan-400 border border-cyan-500/20 flex-shrink-0">
                {{ faq.category }}
              </span>
              <span class="font-bold text-white text-base sm:text-lg">
                {{ faq.question }}
              </span>
            </div>
            <span
              aria-hidden="true"
              class="text-slate-400 text-2xl font-black flex-shrink-0 transition-transform duration-300"
              :class="activeId === faq.id ? 'rotate-45 text-cyan-400' : ''"
            >
              ＋
            </span>
          </button>

          <!-- 絲滑 Grid 展開動效 (WAI-ARIA 合規 region) -->
          <div
            :id="'faq-panel-' + faq.id"
            role="region"
            :aria-labelledby="'faq-btn-' + faq.id"
            class="grid transition-[grid-template-rows] duration-300 ease-out"
            :class="activeId === faq.id ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'"
          >
            <div class="overflow-hidden">
              <div class="px-5 sm:px-6 pb-6 pt-2 text-slate-300 text-base leading-relaxed border-t border-slate-800/60 whitespace-pre-line">
                {{ faq.answer }}
              </div>
            </div>
          </div>
        </div>
      </div>

            <!-- 官方規範指引與免責聲明卡片 (加大字級更清晰易讀) -->
      <div class="mt-10 p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-cyan-500/30 shadow-xl shadow-slate-950/50 text-left flex items-start space-x-4">
        <span class="text-cyan-400 text-2xl sm:text-3xl flex-shrink-0 mt-0.5">ℹ️</span>
        <div class="space-y-2.5 flex-1">
          <div class="flex items-center space-x-3 flex-wrap gap-y-1">
            <span class="text-base sm:text-lg font-black text-white tracking-tight">權益提醒</span>
            <span class="px-2.5 py-0.5 rounded-lg text-xs font-bold bg-cyan-500/15 text-cyan-300 border border-cyan-500/40 font-mono">重要規範</span>
          </div>
          <p class="text-base text-slate-300 leading-relaxed">
            有關參訓資格認定、全額免費受訓審查、每月職訓生活津貼申請條件與各期招生期程，<strong class="text-white font-bold bg-cyan-500/10 px-1 py-0.5 rounded border border-cyan-500/20">一律以勞動部勞動力發展署北分署（台灣就業通）及相關主管機關之最新官方公告與簡章規定為主</strong>。
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { createScrollStagger, gsap } from '@/utils/motion'
import { useCmsStore } from '@/stores/useCmsStore'

const props = withDefaults(
  defineProps<{
    hideHeader?: boolean
  }>(),
  {
    hideHeader: false
  }
)

const store = useCmsStore()
const activeId = ref<number | null>(null)
let scrollTriggerCtx: ReturnType<typeof createScrollStagger> | null = null

function toggleFaq(id: number) {
  activeId.value = activeId.value === id ? null : id
}

function initStaggerAnimation() {
  if (scrollTriggerCtx) {
    scrollTriggerCtx.revert()
    scrollTriggerCtx = null
  }
  nextTick(() => {
    if (props.hideHeader) {
      gsap.fromTo(
        '#faq .rounded-2xl',
        { y: 20, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, stagger: 0.05, ease: 'power1.out', clearProps: 'transform,opacity' }
      )
    } else {
      // FAQ 手風琴條目統一由全域工廠函式調度 (100% 全站標準一致)
      scrollTriggerCtx = createScrollStagger(
        '#faq .rounded-2xl',
        '#faq',
        { stagger: 0.06 }
      )
    }
  })
}

onMounted(() => {
  initStaggerAnimation()
})

// 當非同步取得後端 FAQ 資料後，重新精準綁定動畫
watch(
  () => store.faqs.length,
  () => {
    initStaggerAnimation()
  }
)

onUnmounted(() => {
  if (scrollTriggerCtx) scrollTriggerCtx.revert()
})
</script>
