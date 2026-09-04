---
trigger: always_on
description: 後台 CMS 動態連動與資料治理規範，確保前台展示與後台管理 100% 同步連動
---

# 後台 CMS 動態連動與資料治理核心規範 (CMS Dynamic Sync & Governance)

## 1. 核心原則：後台 CMS 為單一真實資料來源 (Single Source of Truth)

前台展示端（Vue 3）所有經常變動或業務相關之展示資訊，**嚴禁在 UI Component 中寫死（Hardcoded）**，必須透過後端 Django CMS 模型（server/apps/cms/models.py）與 Pinia Store（useCmsStore.ts）進行動態渲染與管理。

---

## 2. 前後端模組與資料連動對照矩陣

| 前台分頁 / 區塊 | 前端組件 (Component) | 後端 Model (CMS) | API 端點 (Ninja API) | 後台可控關鍵欄位 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁頂部輪播** | HeroCarousel.vue | Carousel | /api/v1/public/carousels | 主標題、宣傳副標、電腦/手機版圖片、按鈕文案與連結、排序、啟用狀態 |
| **招生期別與報名** | BatchesSection.vue | AdmissionBatch | /api/v1/public/batches | 期別名稱、報名起訖日、訓練起訖日、就業通報名連結、課程代碼、狀態覆寫 (open/closing_soon/training/ended/hidden) |
| **7 大課程模組** | CurriculumSection.vue | CurriculumModule | /api/v1/public/curriculum/modules | 模組編號 (M1~M7)、模組名稱、受訓時數、分類標籤、課程大綱說明、排序 |
| **核心技術棧** | TechStackSection.vue | TechCard | /api/v1/public/curriculum/tech-cards | 技術名稱、分類標籤、Icon圖標、重點摘要、排序、啟用狀態 |
| **教學設備環境** | FacilitiesSection.vue | Facility | /api/v1/public/facilities | 設施名稱、亮點說明、實景照片、排序、啟用狀態 |
| **學員專題成果** | ShowcaseSection.vue | StudentProject | /api/v1/public/projects | 學員姓名、作品名稱、技術標籤、封面縮圖、Demo 網址、GitHub 連結、精選置頂、啟用狀態 |
| **常見問答 FAQ** | FAQSection.vue | FAQ | /api/v1/public/faqs | 問題類別、問題題目、解答說明、排序、啟用狀態 |
| **全站設定與聯絡** | Navbar.vue / Footer.vue / CommunitySection.vue | SiteSetting | /api/v1/public/site-settings | 網站標題、Logo、Favicon、SEO Description、跑馬燈快訊、Discord Server ID、Discord 邀請連結、諮詢電話、職訓場地址、頁尾版權 |

---

## 3. 開發與異動必須遵循之 8 步驟連動鏈路 (SOP)

當需要新增或調整任何前台展示欄位時，**嚴禁只改前端，必須依序完成以下完整鏈路**：

1. **server/apps/cms/models.py**：新增/調整欄位（提供合理 default 值，圖片欄位同步新增 _alt 欄位）。
2. **python manage.py makemigrations && migrate**：執行資料庫結構遷移。
3. **server/apps/cms/admin.py**：將新欄位加入 list_display、list_editable 或 fieldsets，提供管理員直覺操作。
4. **server/apps/api/schemas.py**：在對應的 XxxOut Schema 中定義輸出型別。
5. **server/apps/api/routers.py**：在 API 查詢中序列化新欄位（圖片必須使用 get_media_url 生成完整絕對網址）。
6. **client/src/types/index.ts**：同步更新前端 TypeScript Interface。
7. **client/src/stores/useCmsStore.ts**：更新 Pinia Store 的 defaultData 快照與狀態綁定。
8. **client/src/components/sections/**：在 Vue SFC 中進行資料渲染，並提供 fallback 預設值（例如：store.settings?.contact_phone || '(02) 2901-8274'）。

---

## 4. 前台防禦性設計守則 (Fallback & Offline First)

1. **雙重防護機制**：
   - 即使後端冷啟動或暫時無網路，前台 Pinia Store 必須維持精準的 defaultData 快照與 localStorage 離線快取，達成 0.01 秒秒開與 100% 容錯。
2. **所有動態欄位必備 Fallback**：
   - 範例：store.settings?.contact_address || '新北市泰山區貴子里致遠新村 55 之 1 號'
   - 嚴格禁止直接以 undefined 渲染或導致頁面崩潰。
