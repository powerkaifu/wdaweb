<template>
  <!-- 信任底座：水平分割線與 4 大核心指標 (大器呼吸空間與無障礙對比，iPad 768px 以上優雅切 4 欄) -->
  <div class="w-full border-t border-slate-800/80 pt-4 sm:pt-6 mt-5 sm:mt-8 lg:mt-8 xl:mt-9 max-w-3xl">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3.5 sm:gap-4 xl:gap-6">
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
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, type Ref } from 'vue'

// 動態計數器 (Animated Counters)
const display100 = ref(0)
const display920 = ref(0)
let raf1: number | null = null
let raf2: number | null = null

function animateValue(
  targetRef: Ref<number>,
  start: number,
  end: number,
  duration: number,
  onFrame?: (id: number) => void
) {
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

onMounted(() => {
  animateValue(display100, 0, 100, 1500, id => (raf1 = id))
  animateValue(display920, 0, 920, 2000, id => (raf2 = id))
})

onUnmounted(() => {
  if (raf1) cancelAnimationFrame(raf1)
  if (raf2) cancelAnimationFrame(raf2)
})
</script>
