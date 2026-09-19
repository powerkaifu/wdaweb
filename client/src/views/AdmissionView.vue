<template>
  <div class="flex-grow">
    <!-- 標準化頂部 Header -->
    <PageHeader
      badge="官方自辦職前訓練"
      title="招生期別與報名"
      theme="cyan"
    >
      <template #subtitle>
        <div class="max-w-4xl mx-auto leading-relaxed space-y-1.5 sm:space-y-2 text-center px-1">
          <p class="text-slate-300 text-[clamp(12px,3.8vw,16px)] sm:text-base lg:text-lg whitespace-nowrap overflow-hidden text-ellipsis sm:overflow-visible">
            本專班為勞動部自辦訓練，待業民眾享 100% 全額免費培訓。
          </p>
          <p class="text-slate-300 text-[clamp(12px,3.8vw,16px)] sm:text-base lg:text-lg whitespace-nowrap overflow-hidden text-ellipsis sm:overflow-visible">
            請直接點擊下方期別連結至「台灣就業通」官方網站完成報名。
          </p>
        </div>
      </template>

      <!-- 即時期別報名狀態指示看板 (讓民眾一眼秒懂當前報名狀態) -->
      <template #extra>
        <div class="mt-5 max-w-xl mx-auto w-full px-2 sm:px-0">
          <div
            class="relative rounded-2xl p-3.5 sm:p-4.5 border backdrop-blur-xl transition-all duration-300 overflow-hidden shadow-xl"
            :class="notice.isOpen
              ? 'bg-emerald-950/40 border-emerald-500/40 shadow-emerald-950/50'
              : 'bg-slate-900/85 border-amber-500/30 shadow-slate-950/60'"
          >
            <!-- 頂部流光微線 -->
            <div
              class="absolute top-0 inset-x-0 h-[1px] bg-gradient-to-r from-transparent"
              :class="notice.isOpen ? 'via-emerald-400/50 to-transparent' : 'via-amber-400/40 to-transparent'"
            ></div>

            <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3 sm:gap-4 text-left">
              <!-- 狀態標籤 Pill Badge -->
              <div class="flex-shrink-0">
                <span
                  class="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold tracking-wide"
                  :class="notice.isOpen
                    ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
                    : 'bg-amber-500/15 text-amber-300 border border-amber-500/30'"
                >
                  <span
                    class="w-2 h-2 rounded-full mr-1.5"
                    :class="notice.isOpen ? 'bg-emerald-400 animate-ping' : 'bg-amber-400'"
                  ></span>
                  {{ notice.badgeText }}
                </span>
              </div>

              <!-- 核心標題與引導說明 -->
              <div class="flex-grow">
                <div
                  class="text-base sm:text-lg font-bold tracking-tight"
                  :class="notice.isOpen ? 'text-white' : 'text-amber-200'"
                >
                  {{ notice.headline }}
                </div>
                <p class="mt-1 text-sm sm:text-base text-slate-300 leading-relaxed">
                  {{ notice.subline }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </PageHeader>

    <!-- 期別卡片 (支援一鍵複製代碼與倒數計時，由 PageHeader 統一引導) -->
    <BatchesSection hide-header />

    <!-- 報名流程與甄試指南 (防呆提醒與行政指引) -->
    <section class="py-12 sm:py-16 bg-slate-950/60 border-t border-slate-800/80">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8 sm:mb-10">
          <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs sm:text-sm font-bold uppercase tracking-wider mb-2">
            <span>Official Guide ｜ 報名須知</span>
          </div>
          <h3 class="text-xl sm:text-2xl lg:text-3xl font-black text-white tracking-tight">
            報名流程與甄試必讀指南
          </h3>
          <p class="text-slate-400 text-sm sm:text-base mt-2 max-w-2xl mx-auto">
            正式報名一律透過勞動部「台灣就業通」官方系統，請詳閱以下 4 步驟確保權益。
          </p>
        </div>

        <!-- 4 步驟卡片網格 -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <!-- Step 1 -->
          <div class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800/90 flex flex-col justify-between">
            <div>
              <div class="text-xs font-mono font-bold text-cyan-400 mb-2">STEP 01</div>
              <h4 class="text-base font-bold text-white mb-2">確認身分與推介單</h4>
              <p class="text-sm text-slate-300 leading-relaxed">
                一般待業者可直接線上報名；<strong class="text-amber-300 font-bold">非自願離職者</strong>請務必於報名截止日前，先親赴就服站開立「職訓推介單」。
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800/60 text-xs text-slate-400">
              ✓ 津貼請領關鍵手續
            </div>
          </div>

          <!-- Step 2 -->
          <div class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800/90 flex flex-col justify-between">
            <div>
              <div class="text-xs font-mono font-bold text-blue-400 mb-2">STEP 02</div>
              <h4 class="text-base font-bold text-white mb-2">台灣就業通線上報名</h4>
              <p class="text-sm text-slate-300 leading-relaxed">
                登入台灣就業通會員，搜尋課程代碼（第 1 期 159268、第 2 期 159269），點選線上送出報名。
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800/60 text-xs text-slate-400">
              ✓ 官方唯一合法報名管道
            </div>
          </div>

          <!-- Step 3 -->
          <div class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800/90 flex flex-col justify-between">
            <div>
              <div class="text-xs font-mono font-bold text-purple-400 mb-2">STEP 03</div>
              <h4 class="text-base font-bold text-white mb-2">參加公開甄試</h4>
              <p class="text-sm text-slate-300 leading-relaxed">
                筆試 50%（基礎電腦常識選擇題，不考代碼）＋ 口試 50%（評估參訓動機與轉職決心），零基礎免驚慌。
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800/60 text-xs text-slate-400">
              ✓ 著重學習決心與態度
            </div>
          </div>

          <!-- Step 4 -->
          <div class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800/90 flex flex-col justify-between">
            <div>
              <div class="text-xs font-mono font-bold text-emerald-400 mb-2">STEP 04</div>
              <h4 class="text-base font-bold text-white mb-2">錄取報到與開訓</h4>
              <p class="text-sm text-slate-300 leading-relaxed">
                接獲錄取通知後依規定報到。享有 100% 全額免費受訓、專屬雙螢幕工位與完整 920 小時實戰培訓。
              </p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-800/60 text-xs text-slate-400">
              ✓ 邁向專業前端工程師
            </div>
          </div>
        </div>

        <!-- 諮詢提示 -->
        <div class="mt-8 text-center">
          <p class="text-xs sm:text-sm text-slate-400">
            ※ 若對報名資格、非自願離職身分或甄試流程有任何疑問，歡迎隨時致電招生專線：
            <a href="tel:0229018274" class="text-cyan-400 font-bold hover:underline">(02) 2901-8274</a>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useSeoMeta } from '@/composables/useSeoMeta'
import { useCmsStore } from '@/stores/useCmsStore'
import { getBatchEnrollmentNotice } from '@/utils/batchStatus'
import PageHeader from '@/components/layout/PageHeader.vue'
import BatchesSection from '@/components/sections/BatchesSection.vue'

const store = useCmsStore()
const notice = computed(() => getBatchEnrollmentNotice(store.batches))


useSeoMeta({
  title: '招生期別與報名時程 ｜ 泰山職訓前端課程 ｜ 台灣就業通線上報名代碼',
  description: '【政府全額補助前端課程報名】泰山職訓「前端網頁技術與AI應用」專班最新招生期別、報名起訖日、甄試時程與開課日期。第 1 期課程代碼 159268、第 2 期課程代碼 159269。待業者享 100% 全額免費培訓與職訓生活津貼補助，請直接點選連結至台灣就業通官方網站報名。招生專線：(02) 2901-8274。',
  canonicalPath: '/admission',
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
        'name': '招生期別與報名',
        'item': 'https://wdaweb.github.io/frontend/admission'
      }
    ]
  }
})
</script>
