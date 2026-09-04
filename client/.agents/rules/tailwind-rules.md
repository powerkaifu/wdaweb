---
trigger: always_on
---

# Tailwind CSS 樣式規範

## 使用原則

- 所有樣式一律使用 Tailwind CSS utility class，禁止撰寫自定義 CSS（除動畫 keyframes 外）。
- 禁止在 HTML 元素上使用 inline style 屬性。

## 色彩系統

- 主視覺色彩：以 cyan-500（#06b6d4）為主色調，hover 使用 cyan-400。
- 錯誤狀態：text-red-500；成功狀態：text-green-500；警告狀態：text-orange-500。

## 無障礙色彩對比度要求

- 一般文字（14px 以下）：文字與背景對比度須大於等於 4.5:1。
- 大型文字（18px 以上）：對比度須大於等於 3:1。

## 響應式斷點規範（行動優先 Mobile First）

- 行動裝置（預設）：< 768px
- 平板（md:）：>= 768px
- 桌機（lg:）：>= 1024px
- 寬螢幕（xl:）：>= 1280px

## 字級與排版規範（Typography & Font Hierarchy，強制執行）

- **全站最小字級底線**：全站**最小字級一律為 `text-xs`（12px / 0.75rem）**，**嚴格禁止在任何組件中使用 `text-[10px]`、`text-[11px]` 或任何小於 12px 的硬編碼極小字級**。
- **階梯標準對齊**：
  - 徽章、輔助標籤、微小提示：`text-xs`（12px）
  - 次要正文、卡片內文、說明描述：`text-sm`（14px）
  - 標準內文、一般段落：`text-base`（16px）
  - 卡片標題、副標題：`text-lg`（18px）~ `text-xl`（20px）
  - 區塊標題 H2：`text-3xl`（30px）~ `text-4xl`（36px）
  - Hero 巨幅大標題 H1：`text-5xl`（48px）~ `text-6xl`（60px）
- **無障礙閱讀體驗**：確保所有字體在手機與高解析度螢幕上具備足夠的字距、行高與辨識度，絕不犧牲可讀性。

## 全域動效與滾動調度規範（Single Source of Motion，最高強制力）

- **全站動效單一真實來源**：所有 Section 卡片、列表與項目的滾動進場動畫，**一律強制呼叫 `@/utils/motion` 的 `createScrollStagger`**，嚴禁在個別組件中自行隨意定義 GSAP 參數。
- **統一標準參數**：
  - `y: 28px`（優雅微升，嚴禁過大位移或 scale 膨脹突變）
  - `duration: 1.0s`（溫潤沉穩）
  - `stagger: 0.07 ~ 0.08s`
  - `ease: 'power1.out'`（Quad 溫和減速，起步初速度平滑，絕不突然加速或衝刺）
  - `scrollTrigger: { start: 'top 88%', once: true }`
- **嚴禁 CSS `transition-all` 攔截 transform**：凡是由 GSAP 控制的卡片容器，**嚴格禁止在其 HTML class 上撰寫 `transition-all`**，必須精確指定為 `transition-[border-color,background-color,box-shadow]`，把 transform 完全交由 GSAP 純淨管理，徹底杜絕補間衝突與掉幀抽動。
- **嚴禁對中文標題使用 SplitText**：繁體中文標題一律採用 Vue `<Transition>` 或整體淡入，禁止在文字載入時使用 SplitText 拆解 DOM 與 revert 閃爍。