---
name: animation-motion-patterns
description: 前端微互動、動效原則與高難度 CSS/JS 動畫模式。當開發 3D 翻轉卡片、CSS Grid 高度平滑過渡、打字機動效、數字滾動計數器或 GSAP 時啟動此技能。
---

# 技能：前端微互動與動畫模式規範

## 1. 動效設計三大鐵律
1. **目的性 (Purposeful)**：動畫必須服務於「提供即時視覺回饋」或「引導使用者注意力」，嚴格避免無意義的雜亂動效。
2. **高效能 (Performant)**：優先使用 `transform` 與 `opacity`（由 GPU Compositor 處理），避免引發 DOM 重排 (Reflow)。
3. **無障礙相容 (Accessible)**：遵循 `prefers-reduced-motion` 規範。

## 2. 經典動態實作模式

### 2.1 CSS Grid 免 JS 計算高度絲滑手風琴
```html
<div
  class="grid transition-[grid-template-rows] duration-300 ease-out"
  :class="isOpen ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'"
>
  <div class="overflow-hidden">
    <!-- 內容區塊 -->
  </div>
</div>
```

### 2.2 3D 翻轉卡片 (3D Card Flip)
- 外層容器：`perspective-1000 group cursor-pointer`
- 內層翻轉：`transform-style-3d duration-500 transition-transform` 與 `:class="isFlipped ? 'rotate-y-180' : ''"`
- 正面與背面：`backface-hidden`，背面帶有 `rotate-y-180`
- **焦點防呆**：背面按鈕在正面時設定 `:tabindex="isFlipped ? 0 : -1"`。

### 2.3 數字平滑滾動動畫 (Animated Counter with RAF)
- 使用 `performance.now()` 與 `easeOutQuad` 緩動計算。
- **記憶體防呆**：必須保存 `requestAnimationFrame` 回傳的 ID，並在 `onUnmounted` 中呼叫 `cancelAnimationFrame`。
