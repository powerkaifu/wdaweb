<template>
  <div class="flex-grow">
    <!-- 標準化頂部 Header -->
    <PageHeader
      badge="真實學員專題成果"
      title="歷屆學員專題成果牆"
      theme="blue"
    >
      <template #subtitle>
        <p class="text-slate-300 text-base sm:text-lg max-w-5xl mx-auto leading-relaxed text-center">
          所有專案皆為學員於 920 小時培訓期間，<span class="text-cyan-400 font-bold">100% 獨立開發的前後端分離＋資料庫 Web 專案</span>。歷經一個月專題實戰，從期初企劃報告到期末成果展，完整淬鍊實戰能力！
        </p>
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
  description: '觀摩泰山職訓「前端網頁技術與AI應用」專班學員成果！所有專案皆為學員於 920 小時培訓期間，100% 獨立開發的前後端分離＋資料庫 Web 專案。歷經一個月專題實戰，從期初企劃報告到期末成果展，完整淬鍊實戰能力！提供線上 Demo 與 GitHub 原始碼展示。非本科轉職工程師的真實實力驗證！',
  canonicalPath: '/showcase',
  robots: 'index, follow',
  jsonLd: {
    '@type': 'BreadcrumbList',
    'itemListElement': [
      {
        '@type': 'ListItem',
        'position': 1,
        'name': '首頁',
        'item': 'https://wdaweb.github.io/frontend/'
      },
      {
        '@type': 'ListItem',
        'position': 2,
        'name': '學員專題成果',
        'item': 'https://wdaweb.github.io/frontend/showcase'
      }
    ]
  }
})
</script>
