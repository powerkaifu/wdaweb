---
name: gsap-scroll-animation
description: GSAP 3 (GreenSock) 與 ScrollTrigger 滾動視差、時間軸編排及文字進場動態規範。當需要為頁面建立滾動視差、釘住效果 (Pinning)、序列時間軸 (Timeline) 或文字分割特效時啟動此技能。
---

# 技能：GSAP 3 與 ScrollTrigger 專業動效規範

## 1. 核心觀念與架構
GSAP 是 Web 2D 動畫的業界工業標準。在 Vue 3 中使用 GSAP 時，**核心原則是使用 `gsap.context()` 進行全域範圍管理**，確保組件銷毀時能 100% 乾淨清理。

## 2. Vue 3 整合標準範本 (生命週期與清理)
```vue
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const mainContainer = ref<HTMLElement | null>(null)
let ctx: gsap.Context | null = null

onMounted(() => {
  ctx = gsap.context(() => {
    // 建立時間軸或滾動觸發
    gsap.from('.feature-card', {
      scrollTrigger: {
        trigger: '.feature-card',
        start: 'top 80%',
        end: 'bottom 20%',
        toggleActions: 'play none none reverse'
      },
      y: 40,
      opacity: 0,
      duration: 0.8,
      stagger: 0.15,
      ease: 'power3.out'
    })
  }, mainContainer.value)
})

onUnmounted(() => {
  // 核心清理：清除所有 ScrollTrigger 實例與動畫 Timeline
  if (ctx) ctx.revert()
})
</script>
```

## 3. 常見高階動效模式
- **Stagger 序列進場**：使用 `stagger: { each: 0.1, from: 'start' }` 呈現流暢的網格卡片展開。
- **平滑視差 (Parallax)**：`yPercent: -20, ease: 'none', scrollTrigger: { scrub: true }`。
- **GPU 硬體加速**：對目標元素加入 `will-change: transform`。
