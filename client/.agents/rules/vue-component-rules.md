---
trigger: always_on
---

# Vue 3 組件撰寫守則

## SFC 結構順序

每個 .vue 單一文件組件必須嚴格依照以下順序排列：
1. script setup lang="ts"
2. template
3. style scoped

## Script Setup 規範

- 使用 script setup lang="ts" Composition API 語法。
- Props 定義使用 defineProps 泛型語法。
- 外部資料來源統一透過 useCmsStore() 取得，禁止直接呼叫 api。

## 生命週期與清理

- 在 onMounted() 中建立的事件監聽器，必須在 onUnmounted() 中進行清理。
- 在 onMounted() 中啟動的 setInterval，必須在 onUnmounted() 中執行 clearInterval。

## Template 規範

- 超過 3 個條件的複雜判斷邏輯必須抽離至 computed，不可直接寫在 v-if 中。
- 列表渲染 v-for 必須指定 :key，使用資料唯一識別 id 作為 key 值。
- 圖片元素 img 必須提供 :alt 屬性（無障礙規範）。