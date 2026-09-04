---
name: canvas-particle-effects
description: 高效能 HTML5 Canvas 2D / 粒子流光背景、連線科技節點與音訊波形視覺化。當需要為網站建立動態科技背景、互動粒子網格或流動星空時啟動此技能。
---

# 技能：Canvas 2D 粒子特效與科技背景規範

## 1. Canvas 高效能渲染架構
- **DPI 適配 (Retina Ready)**：依據 `window.devicePixelRatio` 放大 Canvas 畫布寬高，再以 CSS 縮回原始尺寸，確保高解析螢幕下文字與粒子邊緣銳利不模糊。
- **物件池設計 (Object Pool)**：預先初始化固定長度的粒子陣列，循環更新位置與透明度，嚴禁在每幀迴圈中 `new Particle()` 引發垃圾回收 (GC) 停頓。

## 2. 標準粒子畫布架構範本
```vue
<template>
  <canvas ref="canvasRef" class="absolute inset-0 pointer-events-none z-0"></canvas>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const canvasRef = ref<HTMLCanvasElement | null>(null)
let rafId: number | null = null
let onResize: (() => void) | null = null

interface Particle {
  x: number
  y: number
  vx: number
  vy: number
  size: number
  alpha: number
}

onMounted(() => {
  const canvas = canvasRef.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  let width = 0
  let height = 0
  let particles: Particle[] = []
  const COUNT = 60

  onResize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2)
    width = canvas.parentElement?.clientWidth || window.innerWidth
    height = canvas.parentElement?.clientHeight || window.innerHeight
    canvas.width = width * dpr
    canvas.height = height * dpr
    ctx.scale(dpr, dpr)
  }
  window.addEventListener('resize', onResize)
  onResize()

  // 初始化粒子池
  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.6,
      vy: (Math.random() - 0.5) * 0.6,
      size: Math.random() * 2 + 1,
      alpha: Math.random() * 0.5 + 0.2
    })
  }

  function render() {
    ctx.clearRect(0, 0, width, height)
    ctx.fillStyle = 'rgba(6, 182, 212, 0.6)' // cyan-500

    for (let p of particles) {
      p.x += p.vx
      p.y += p.vy
      if (p.x < 0 || p.x > width) p.vx *= -1
      if (p.y < 0 || p.y > height) p.vy *= -1

      ctx.beginPath()
      ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2)
      ctx.fill()
    }
    rafId = requestAnimationFrame(render)
  }

  rafId = requestAnimationFrame(render)
})

onUnmounted(() => {
  if (rafId) cancelAnimationFrame(rafId)
  if (onResize) window.removeEventListener('resize', onResize)
})
</script>
```
