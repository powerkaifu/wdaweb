---
name: a11y-audit
description: WCAG 2.1 AA 級無障礙全站稽核 SOP。在部署 GitHub Pages 前或使用者要求無障礙審查時啟動。
---

# 技能：WCAG 2.1 AA 無障礙稽核

## 稽核檢查清單

### 1. 圖片 Alt Text 稽核
使用 grep_search 在 client/src/components/ 中搜尋所有 img 標籤，確認：
- 每個 img 元素都有 alt 屬性
- alt 屬性不為空字串（裝飾性圖片除外，裝飾性圖片使用 alt=""）
- alt 文字具有語意說明（不可只寫「圖片」）

### 2. 鍵盤操作稽核
確認以下互動元素均可透過 Tab 鍵聚焦，並在聚焦時有明顯的 focus:ring 視覺提示：
- 所有 button 元素
- 所有 a 連結元素
- FAQ 手風琴的展開按鈕
- 3D 翻轉卡片（確認 tabindex 與 keyboard Enter 觸發）

### 3. 語意化 HTML 稽核
確認頁面結構使用正確的語意化標籤：
- 頁面只有一個 h1 主標題
- 標題層級不跳躍（h1 > h2 > h3）
- 導覽列使用 nav 元素包裹
- 主要內容區使用 main 元素

### 4. 色彩對比度確認
確認主要文字色彩與背景色符合 4.5:1 對比度（使用 tailwind-rules 中的色彩規範）。

### 5. 產出稽核報告
完成稽核後，整理一份列表說明：
- 發現的問題項目
- 已修復的項目
- 建議後續改善的項目