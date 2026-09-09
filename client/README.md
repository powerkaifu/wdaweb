# 泰山職訓「前端網頁技術與AI應用」招生展示系統 - 前端 (Client)

本目錄為專案之 Vue 3 前端單頁應用程式（SPA）。

## 技術棧

- **框架**：Vue 3 (Composition API) + Vite + TypeScript
- **狀態管理**：Pinia
- **樣式與 UI**：Tailwind CSS v4 + Radix Vue + Lucide Icons
- **視覺動效**：Three.js (WebGL 3D 星雲與繁星系統) + Canvas 2D + GSAP ScrollTrigger

## CI/CD 雙遠端倉庫自動部署 (Dual Remote Deployment)

本專案配置為一鍵雙推（Dual Push），程式碼變更將同時推送到：
1. https://github.com/powerkaifu/wdaweb.git
2. https://github.com/wdaweb/frontend.git

每當 client/** 目錄有新提交並推送時，兩邊倉庫的 GitHub Actions 將自動被觸發，獨立完成建置並發布至 GitHub Pages，同時共享同一個 Render 後端 API。
