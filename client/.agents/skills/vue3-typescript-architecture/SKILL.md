---
name: vue3-typescript-architecture
description: Vue 3.5+ Composition API、Pinia 狀態快取、TypeScript 嚴格型別架構與 Vite 生產打包優化守則。當進行組件架構設計、狀態快取重構或打包優化時啟動。
---

# 技能：Vue 3 + TypeScript 企業級前端架構規範

## 1. 職責嚴格分離 (SoC)
- **View / Section 組件層**：僅負責渲染與使用者互動事件，禁止直接呼叫 API 或進行複雜運算。
- **Pinia Store 層 (`useCmsStore.ts`)**：統一負責 API 請求、離線快取（24h TTL）、錯誤捕捉與響應式狀態同步。
- **API Client 層 (`api/client.ts`)**：HTTP 請求單一出口，嚴格對齊後端 Swagger/OpenAPI 定義。
- **型別層 (`types/index.ts`)**：TypeScript 介面單一真相來源，嚴格禁止殘留 `any`。

## 2. 記憶體管理與生命週期清理
- **計時器**：在 `onMounted` 建立的 `setInterval` / `setTimeout`，變數型別宣告為 `ReturnType<typeof setInterval> | null`，並在 `onUnmounted` 執行 `clearInterval`。
- **事件監聽**：所有 `window.addEventListener('resize' / 'scroll')` 必須在 `onUnmounted` 執行 `removeEventListener`。
- **高頻事件**：滾動與視窗縮放必須加入 `requestAnimationFrame` 節流保護。

## 3. Vite 生產代碼分割 (Manual Chunks)
在 `vite.config.ts` 中配置 `build.rollupOptions.output.manualChunks`，將大型第三方依賴（Three.js、Vue 生態系、動畫庫）獨立分拆，提升快取命中率與首屏秒開效能。
