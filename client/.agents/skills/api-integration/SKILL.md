---
name: api-integration
description: 串接後端 Django Ninja 新 API 端點的標準 SOP。當後端新增了 API 需要前台接入時使用。
---

# 技能：串接後端 API 標準流程

## 執行 SOP

### Step 1：確認 API 規格
打開 `http://127.0.0.1:8000/api/v1/docs` 確認新 API 端點的路徑與回傳資料欄位結構。

### Step 2：新增 TypeScript 型別
在 `client/src/types/index.ts` 新增對應 API 回傳資料的 Interface，欄位名稱與後端 Schema 對齊。

### Step 3：在 API Client 新增方法
在 `client/src/api/client.ts` 的 `api` 物件中新增對應的 axios 請求方法，引用剛新增的型別。

### Step 4：在 Pinia Store 整合
在 `client/src/stores/useCmsStore.ts` 中：
- 新增 `ref` 狀態變數存放資料
- 新增 `async` action 呼叫 api 方法並更新狀態
- 在 `loadAll()` 或初始化函式中呼叫此 action

### Step 5：驗證
啟動 `npm run dev`，確認資料正確從後端載入並顯示於組件中。