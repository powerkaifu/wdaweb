# 前台展示端（Vue 3 SPA）AI 代理人核心準則

> activation: always_on
> scope: client/ 目錄下所有檔案

---

## 1. 前台架構概覽

  client/src/
  ├── api/client.ts          # API 唯一出口（所有請求必須從這裡發出）
  ├── components/
  │   ├── layout/            # Navbar.vue、Footer.vue（全域排版）
  │   └── sections/          # 所有頁面區塊組件
  ├── stores/useCmsStore.ts  # Pinia Store（唯一業務邏輯層）
  ├── types/index.ts         # 所有 TypeScript 型別定義（單一來源）
  └── App.vue                # 根組件，負責引入與排列所有 Section

---

## 2. 組件設計規範

### 命名規範
- Section 組件：PascalCase + Section 後綴（例：BatchesSection.vue、FAQSection.vue）
- Layout 組件：PascalCase（例：Navbar.vue、Footer.vue）

### 職責分離原則（SoC）
- Section 組件（View 層）：只負責「渲染資料」與「處理使用者互動事件」，禁止撰寫業務邏輯或直接呼叫 API。
- Pinia Store（useCmsStore.ts）：所有 API 呼叫、資料轉換與狀態快取統一在此處理。
- API Client（api/client.ts）：所有 HTTP 請求的唯一出口，禁止在組件或 Store 中直接使用 axios。

---

## 3. TypeScript 嚴格規範

- 所有 Component Props 必須定義介面型別，禁止使用 any。
- 所有 API 回應資料型別必須在 src/types/index.ts 中先定義。
- 新增型別後需執行 npm run build 確認零 TypeScript 錯誤。

---

## 4. 禁止事項與排版守則

- **字級嚴格規範**：所有文字大小必須嚴格符合 `style.css` 的全域變數階梯（最小底線為 `text-xs` 12px）。**嚴格禁止**使用 `text-[10px]`、`text-[11px]` 或任何自定義極小字級。
- 禁止在 template 或 style 區塊中撰寫 inline style。
- 禁止在 Section 組件中直接 import axios 或使用 fetch()。
- 禁止硬編碼後端 API 網址，一律透過 import.meta.env.VITE_API_BASE_URL 讀取。
- 禁止跨 Section 組件直接互相傳遞資料，統一透過 Pinia Store 共享狀態。

---

## 5. 常用指令

```
npm run dev       # 啟動開發伺服器
npm run build     # TypeScript 型別檢查與生產打包
```
