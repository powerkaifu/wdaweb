---
name: tailwind-design-system
description: 現代 Tailwind CSS v4 設計系統規範與 UI/UX 排版準則。當進行前端組件樣式設計、色彩系統擴充、深色科技美學打磨或響應式佈局時啟動此技能。
---

# 技能：Tailwind CSS v4 現代設計系統與 UI/UX 規範

## 1. 核心設計哲學
本專案採用**深色科技感（Dark Cyberpunk / Modern Tech）**視覺風格，以極致沉浸的黑藍色調搭配青藍色光暈，呈現專業、現代、俐落的前端工程師職訓形象。

## 2. 色彩系統規範 (Color Tokens)
- **基底深色背景**：
  - 主要背景：`bg-slate-950` (#020617)
  - 卡片與容器次背景：`bg-slate-900` (#0f172a) / `bg-slate-900/80`
  - 邊框與分隔線：`border-slate-800` / `border-slate-800/60`
- **主視覺霓虹強調色**：
  - 主色調：`text-cyan-400` / `bg-cyan-500` (#06b6d4)
  - 次強調色：`text-blue-400` / `bg-blue-600`
  - 輔助社群色：`bg-[#5865F2]` (Discord Indigo)
  - 成功與狀態色：`text-emerald-400` (開班中) / `text-amber-400` (即將截止)
- **大氣微光 (Ambient Glow)**：
  - 發光暈染：`bg-cyan-500/15 blur-3xl pointer-events-none rounded-full`
  - 卡片陰影：`shadow-xl shadow-cyan-950/30`

## 3. 全站容器與排版律動
- **全站一致寬度基準**：外層容器強制統一為 `max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8`。
- **垂直節奏 (Vertical Rhythm)**：大區塊 Section 間距設為 `py-16 sm:py-20 lg:py-24`。
- **行動優先響應式斷點**：`sm:` (>= 640px), `md:` (>= 768px), `lg:` (>= 1024px), `xl:` (>= 1280px)。
