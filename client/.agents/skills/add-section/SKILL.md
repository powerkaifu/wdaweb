---
name: add-section
description: 新增前台 Vue 3 Section 組件的端對端 SOP。當使用者說「新增 X 區塊」、「建立 Y Section」時啟動此技能。
---

# 技能：新增前台 Section 組件

觸發條件：使用者要求新增一個前台展示區塊（Section）。

## 執行 SOP

### Step 1：確認新 Section 的資料來源
確認此 Section 需要顯示的資料是否已有對應的後端 API 端點。
- 若尚無 API：提示使用者先至後端建立對應 API（參考 server 的 add-cms-model 技能）。
- 若已有 API：確認 `http://127.0.0.1:8000/api/v1/docs` 上的回傳資料結構。

### Step 2：在 TypeScript 型別檔新增介面
在 `client/src/types/index.ts` 中新增對應資料的 TypeScript Interface。

### Step 3：在 API Client 新增請求方法
在 `client/src/api/client.ts` 中的 `api` 物件新增對應的 GET 請求方法。

### Step 4：在 Pinia Store 新增 Action
在 `client/src/stores/useCmsStore.ts` 中新增：
- 狀態（ref）：儲存 API 回傳的資料清單
- Action：呼叫 api.get...() 並更新狀態

### Step 5：建立 Section 組件 SFC
在 `client/src/components/sections/` 建立新的 `XxxSection.vue`，遵循以下結構：
- script setup lang="ts"：引入 useCmsStore、onMounted 呼叫 Action
- template：渲染資料，所有 img 加 alt，列表加 :key
- style scoped：若有特殊動畫樣式才加入

### Step 6：在 App.vue 引入並插入新 Section
在 `client/src/App.vue` 中依照頁面順序引入並放置新 Section 組件。

### Step 7：建置驗證
執行 `npm run build` 確認 TypeScript 零錯誤，打包成功。