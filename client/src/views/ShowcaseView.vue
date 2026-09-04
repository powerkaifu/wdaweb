<template>
  <div class="flex-grow">
    <!-- 標準化頂部 Header -->
    <PageHeader
      badge="真實學員專題成果"
      title="歷屆學員專題成果牆"
      theme="blue"
    >
      <template #subtitle>
        <div class="text-base sm:text-lg max-w-5xl mx-auto leading-relaxed space-y-1 sm:space-y-1.5">
          <p class="text-slate-300">
            所有專案皆為學員於 920 小時培訓期間「100% 獨立自主開發」之前後端分離＋資料庫 Web 專案。
          </p>
          <p class="text-slate-300">
            為期一個月的專題實戰，歷經「期初企劃報告」與「期末成果展」嚴謹淬鍊！
          </p>
          <p class="text-cyan-400 font-bold pt-0.5 sm:pt-1 flex items-center justify-center gap-1.5">
            <span>✨</span>
            <span>點擊卡片可 3D 翻轉查看詳情與線上 Demo！</span>
          </p>
        </div>
      </template>
    </PageHeader>

    <!-- 學員作品成果牆 (支援 3D 翻轉卡片，由 PageHeader 統一引導) -->
    <ShowcaseSection hide-header />
  </div>
</template>

<script setup lang="ts">
import { useSeoMeta } from '@/composables/useSeoMeta'
import PageHeader from '@/components/layout/PageHeader.vue'
import ShowcaseSection from '@/components/sections/ShowcaseSection.vue'

useSeoMeta({
  title: '歷屆學員 Web 專題成果展示 ｜ 前後端分離實作作品集',
  description: '觀摩泰山職訓「前端網頁技術與AI應用」專班學員成果！所有專案皆為學員於 920 小時培訓期間「100% 獨立自主開發」之前後端分離＋資料庫 Web 專案，提供線上 Demo 與 GitHub 原始碼展示。非本科轉職工程師的真實實力驗證！',
  canonicalPath: '/showcase',
  robots: 'index, follow',
  jsonLd: {
    '@type': 'BreadcrumbList',
    'itemListElement': [
      {
        '@type': 'ListItem',
        'position': 1,
        'name': '首頁',
        'item': 'https://powerkaifu.github.io/wdaweb/'
      },
      {
        '@type': 'ListItem',
        'position': 2,
        'name': '學員專題成果',
        'item': 'https://powerkaifu.github.io/wdaweb/showcase'
      }
    ]
  }
})
</script>
