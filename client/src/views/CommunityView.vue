<template>
  <div class="flex-grow">
    <!-- 1. 全站標準化頂部 Header (與其他所有頁面完全一致，支援 GSAP SplitText 逐字升起) -->
    <PageHeader
      badge="即時線上互動"
      title="Discord 線上即時諮詢社群"
      subtitle="泰山職訓前端專班專屬 Discord 社群，提供課前諮詢、技術交流與學長姐轉職心得分享。"
      theme="indigo"
    />

    <!-- 2. Discord 線上即時社群 Widget (支援骨架屏動效) 與加入引導，由 PageHeader 統一引導 -->
    <CommunitySection hide-header />

    <!-- 3. 下方輔助電話諮詢管道 (全站標準底層橫幅) -->
    <section class="py-20 sm:py-24 bg-slate-900/30 border-t border-slate-800/60 text-center relative overflow-hidden">
      <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 space-y-4">
        <div class="max-w-3xl mx-auto space-y-4">
          <h3 class="text-2xl sm:text-3xl font-black text-white tracking-tight">也歡迎直接來電洽詢</h3>
          <p class="text-slate-300 text-base">
            週一至週五 08:30 ~ 17:00 由專人為您解答報名與受訓流程相關問題。
          </p>
          <div class="pt-2">
            <a
              :href="`tel:${store.settings?.contact_phone || '0229018274'}`"
              class="inline-flex items-center justify-center px-8 py-4 rounded-2xl font-bold text-base text-white bg-slate-800 hover:bg-slate-700 border border-slate-700 hover:border-indigo-500/40 hover:-translate-y-0.5 active:scale-95 transition-all space-x-2 shadow-xl shadow-slate-950/60"
            >
              <span>📞 招生諮詢專線：{{ store.settings?.contact_phone || '(02) 2901-8274' }}</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useSeoMeta } from '@/composables/useSeoMeta'
import PageHeader from '@/components/layout/PageHeader.vue'
import CommunitySection from '@/components/sections/CommunitySection.vue'
import { useCmsStore } from '@/stores/useCmsStore'

const store = useCmsStore()

useSeoMeta({
  title: 'Discord 線上諮詢社群 ｜ 招生專線與交通指南',
  description: '加入泰山職訓「前端網頁技術與AI應用」專屬 Discord 線上即時諮詢社群！提供課前疑難排解、在訓學長姐心得分享與轉職交流。亦可於週一至週五來電專線：(02) 2901-8274，訓練場地址：新北市泰山區貴子里致遠新村 55 之 1 號。',
  canonicalPath: '/community',
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
        'name': 'Discord 線上諮詢',
        'item': 'https://powerkaifu.github.io/wdaweb/community'
      }
    ]
  }
})
</script>
