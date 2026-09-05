import { onMounted, onUnmounted, nextTick, watch, type WatchSource } from 'vue'
import { createScrollStagger, type ScrollStaggerOptions } from '@/utils/motion'

/**
 * 通用滾動微升進場動效 Composable
 * 遵循 DRY 與 SRP 原則，統一封裝全站各 Section 的 GSAP ScrollTrigger 生命週期與非同步重新綁定
 * 
 * @param targets 目標選擇器或元素 (例如: '#tech-cards-grid .tech-card')
 * @param trigger 觸發容器選擇器或元素 (例如: '#tech-stack')
 * @param options 動畫覆寫選項 (yOffset, duration, stagger 等)
 * @param watchSource 可選的響應式監聽對象 (例如: () => store.techCards.length)，當資料載入後自動刷新動畫
 */
export function useScrollStagger(
  targets: gsap.DOMTarget,
  trigger: gsap.DOMTarget,
  options?: ScrollStaggerOptions,
  watchSource?: WatchSource<unknown>
) {
  let ctx: ReturnType<typeof createScrollStagger> | null = null

  const refresh = () => {
    if (ctx) {
      ctx.revert()
      ctx = null
    }
    nextTick(() => {
      ctx = createScrollStagger(targets, trigger, options)
    })
  }

  onMounted(() => {
    refresh()
  })

  if (watchSource) {
    watch(watchSource, () => {
      refresh()
    })
  }

  onUnmounted(() => {
    if (ctx) {
      ctx.revert()
      ctx = null
    }
  })

  return {
    refresh
  }
}
