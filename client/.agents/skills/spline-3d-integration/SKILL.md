---
name: spline-3d-integration
description: Spline 3D 模型與互動場景在 Vue 3 前端專案中的非同步整合、事件雙向綁定與 WebGL 記憶體管理 SOP。當需要嵌入 3D 浮空科技物件、機器人、滑鼠跟隨 3D 模型或 Spline 互動時啟動此技能。
---

# 技能：Spline 3D 與 Vue 3 現代前端整合規範

## 1. 核心定位與設計原則
Spline 3D 能為網頁帶來極致的現代科技感與互動體驗。在 Vue 3 專案中整合 Spline 時，必須遵循以下三大原則：
1. **非同步懶載入 (Lazy Loading)**：禁止在首屏靜態打包巨型 3D 依賴，一律使用非同步動態 `import('@splinetool/runtime')`。
2. **優雅降級與骨架屏 (Graceful Degradation)**：在 3D 場景載入完成（`spline.load()`）前，必須展示流暢的脈衝骨架屏（Skeleton Loader）。
3. **嚴格 WebGL 銷毀 (Memory Disposal)**：組件卸載時必須呼叫 `spline.dispose()` 釋放 GPU 顯存，避免 SPA 換頁記憶體洩漏。

---

## 2. Vue 3 企業級 Spline 組件標準範本

```vue
<template>
  <div class="relative w-full h-[400px] sm:h-[500px] rounded-3xl overflow-hidden bg-slate-900/60 border border-slate-800 flex items-center justify-center">
    <!-- 1. 載入中骨架屏 (Skeleton Loader) -->
    <div
      v-if="!isLoaded"
      class="absolute inset-0 flex flex-col items-center justify-center p-6 bg-slate-900/90 backdrop-blur-md z-10 animate-pulse"
    >
      <div class="w-16 h-16 rounded-2xl bg-cyan-500/20 border border-cyan-500/30 flex items-center justify-center text-2xl mb-4">
        🧊
      </div>
      <div class="text-sm font-bold text-cyan-400">正在載入 3D 互動場景...</div>
      <div class="text-xs text-slate-500 mt-1">首次載入需時數秒，請稍候</div>
    </div>

    <!-- 2. Spline 3D WebGL 畫布容器 -->
    <canvas
      ref="canvasRef"
      role="img"
      aria-label="3D 互動模型，可用滑鼠旋轉與互動"
      class="w-full h-full object-cover transition-opacity duration-700"
      :class="isLoaded ? 'opacity-100' : 'opacity-0'"
    ></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  /** Spline 匯出的 .splinecode 場景網址 */
  sceneUrl: string
}>()

const emit = defineEmits<{
  (e: 'loaded'): void
  (e: 'objectClick', objectName: string): void
}>()

const canvasRef = ref<HTMLCanvasElement | null>(null)
const isLoaded = ref(false)
let splineApp: any = null

onMounted(async () => {
  if (!canvasRef.value) return

  try {
    // 1. 動態非同步載入執行庫，保持初始 Bundle 輕量
    const { Application } = await import('@splinetool/runtime')
    
    // 2. 初始化 Application 實例
    splineApp = new Application(canvasRef.value)
    
    // 3. 載入 3D 場景
    await splineApp.load(props.sceneUrl)
    isLoaded.value = true
    emit('loaded')

    // 4. 監聽 3D 場景內部物件點擊事件 (選填)
    splineApp.addEventListener('mouseDown', (e: any) => {
      if (e.target && e.target.name) {
        emit('objectClick', e.target.name)
      }
    })
  } catch (err) {
    console.warn('Spline 3D 載入異常，請檢查網路或 sceneUrl:', err)
  }
})

onUnmounted(() => {
  // 核心銷毀：釋放 WebGL 著色器與記憶體
  if (splineApp) {
    splineApp.dispose()
    splineApp = null
  }
})
</script>
```

---

## 3. 效能優化與注意事項清單

1. **依賴安裝**：若要在專案中實裝 Spline，需在 client 目錄執行：
   ```bash
   npm install @splinetool/runtime
   ```
2. **場景壓縮優化**：在 Spline 編輯器中導出時，開啟 **Texture Compression** 與 **Geometry Simplification**，將場景檔案控制在 2MB 以內。
3. **無障礙 (A11y)**：在 `<canvas>` 加上 `role="img"` 與語意化 `aria-label`。
