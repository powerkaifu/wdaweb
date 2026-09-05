---
name: claude-design
description: >-
  現代頂級 Web 應用美學、深邃毛玻璃擬態、細膩微互動與極致細節打磨規範。當需要提升 UI 精緻度、設計現代科技感卡片、優化呼吸留白律動、打磨按鈕觸控反饋與深色科技質感時啟動此技能。
---

# 技能：Claude Design 現代旗艦組件美學規範

## 1. 核心視覺風格：深色暗黑科技（Dark Tech Aesthetic）
本規範專為前端網頁技術與 AI 應用打造，呈現高度工程專業感與未來科技感：
- **深色底座堆疊**：
  - 全域背景：`slate-950`（#020617）與深邃星空粒子穿透。
  - 第一層卡片：`slate-900/80` 搭配 `backdrop-blur-xl` 毛玻璃質感。
  - 懸浮/浮動層：`slate-800/90` 搭配細膩光澤邊框。
- **微光羽化邊框（1px Subsurface Glow）**：
  - 卡片邊框一律採用 `border border-slate-800/90 hover:border-cyan-500/50`。
  - 關鍵組件融入 1px 流光邊框與內部漫射背光穿透。

---

## 2. 呼吸空間與 8pt 幾何排版系統

### 垂直節奏（Vertical Rhythm）
- 組件內部 Padding 採 8pt 模組化倍數：
  - 緊湊卡片：`p-4 sm:p-5`（16px~20px）
  - 標準卡片：`p-6 sm:p-8`（24px~32px）
  - 巨幅焦點看板：`p-8 sm:p-10 lg:p-12`（32px~48px）
- 標題與內文間距：`mb-3 sm:mb-4`（12px~16px），維持格式塔緊密親密性。

### 點狀狀態膠囊與徽章（Badge System）
- 狀態徽章統一採用柔和半透明背景＋細微邊框：
  - 進行中／開放中：`bg-cyan-500/10 text-cyan-400 border border-cyan-500/30`
  - 成果／已結訓：`bg-emerald-500/10 text-emerald-400 border border-emerald-500/30`
  - 津貼／特別亮點：`bg-purple-500/10 text-purple-400 border border-purple-500/30`
  - 呼吸脈衝微點：`<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>`

---

## 3. 按鈕與微互動物理學（Micro-interactions）

### 旗艦主按鈕（Primary Hero CTA）
- 漸層背景：`bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500`
- 霓虹陰影：`shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/45`
- 懸浮物理過渡：`hover:-translate-y-0.5 active:scale-95 transition-all duration-300 ease-out`
- 箭頭滑動回饋：`group-hover:translate-x-1 transition-transform`

### 輔助次按鈕（Secondary Ghost CTA）
- 外框與背景：`bg-slate-900/80 border border-slate-700 hover:border-cyan-500/50 text-slate-200 hover:text-white`
- 懸浮光暈：`hover:bg-slate-800/80 transition-all`

---

## 4. 全域字級與無障礙強制守則
- **字型分流**：
  - 中文：`Noto Sans TC` 思源黑體，剛健端莊。
  - 英文／阿拉伯數字：`Plus Jakarta Sans`，飽滿圓潤未來感。
  - 程式碼／序號水印：`JetBrains Mono`。
- **字級底線**：
  - 重要內文一律維持 `text-base`（16px）以上，行高 `1.7~1.8`。
  - 嚴禁 `text-[10px]` 或任何小於 12px 的隨意字級。