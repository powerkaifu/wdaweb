<template>
  <section id="community" :class="hideHeader ? 'py-12 bg-slate-950 relative overflow-hidden' : 'py-24 bg-slate-950 relative overflow-hidden'">
    <!-- 頂部 Discord 藍紫與電光青環境微暈 -->
    <div class="absolute -top-32 right-10 w-96 h-96 bg-[#5865F2]/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-32 left-10 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
      <div v-if="!hideHeader" class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-bold uppercase tracking-wider">
          Community & Discord
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white mt-4 tracking-tight">
          Discord 線上即時諮詢社群
        </h2>
        <p class="text-slate-400 mt-4 text-base sm:text-lg">
          隨時加入官方 Discord 頻道，直接向講師與結訓學長姐發問交流！
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center w-full mx-auto">
        <!-- 左側：即時問答卡片與一鍵加入按鈕 -->
        <div class="lg:col-span-6 space-y-6">
          <div class="p-6 sm:p-7 rounded-3xl bg-indigo-950/40 backdrop-blur-md border border-indigo-500/30 shadow-xl shadow-indigo-950/30">
            <div class="flex items-center space-x-3 mb-4">
              <span class="text-2xl sm:text-3xl leading-none flex-shrink-0">💬</span>
              <h3 class="text-xl font-extrabold text-white tracking-tight">
                即時線上問答
              </h3>
            </div>
            <p class="text-base text-slate-300 leading-relaxed text-pretty">
              不知道自己適不適合參訓？想了解上課氛圍？加入 Discord 即可即時詢問。
            </p>
          </div>

          <a
            :href="store.settings?.discord_invite_url || 'https://discord.gg/TrerFKG'"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="立即加入官方 Discord 伺服器進行線上即時諮詢（另開新分頁）"
            class="block w-full py-4 rounded-2xl text-center font-bold text-white bg-[#5865F2] hover:bg-[#4752C4] shadow-xl shadow-indigo-500/25 hover:-translate-y-0.5 active:scale-95 transition-all focus-visible:ring-2 focus-visible:ring-indigo-400 focus:outline-none text-base"
          >
            🚀 立即加入 Discord 伺服器 ↗
          </a>
        </div>

        <!-- 右側：Discord 官方伺服器 Widget (加大寬度至 6 欄，寬敞大器) -->
        <div class="lg:col-span-6">
          <div class="rounded-3xl overflow-hidden border border-slate-800 bg-slate-900 p-2 shadow-2xl relative min-h-[400px] flex items-center justify-center">
            <!-- 骨架屏 Skeleton Loader -->
            <div
              v-if="!isLoaded"
              class="absolute inset-2 rounded-2xl bg-slate-800/80 p-6 flex flex-col justify-between animate-pulse z-10"
            >
              <div class="space-y-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 rounded-full bg-slate-700"></div>
                  <div class="space-y-2 flex-1">
                    <div class="h-4 bg-slate-700 rounded w-1/3"></div>
                    <div class="h-3 bg-slate-700/60 rounded w-1/4"></div>
                  </div>
                </div>
                <div class="space-y-2 pt-4">
                  <div class="h-3 bg-slate-700/50 rounded w-full"></div>
                  <div class="h-3 bg-slate-700/50 rounded w-5/6"></div>
                  <div class="h-3 bg-slate-700/50 rounded w-2/3"></div>
                </div>
              </div>
              <div class="text-center text-xs text-slate-500 font-medium">
                ⚡ 正在連線至 Discord 官方伺服器...
              </div>
            </div>

            <!-- Discord Widget iframe (WCAG 4.1.2 合規：具備 title 屬性) -->
            <iframe
              :src="`https://discord.com/widget?id=${store.settings?.discord_server_id || '463880731828158464'}&theme=dark`"
              title="Discord 官方社群伺服器在線狀態與頻道小工具"
              width="100%"
              height="400"
              allowtransparency="true"
              frameborder="0"
              sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"
              class="rounded-2xl transition-opacity duration-500"
              :class="isLoaded ? 'opacity-100' : 'opacity-0'"
              @load="isLoaded = true"
            ></iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import { createScrollStagger } from '@/utils/motion'
import { useCmsStore } from '@/stores/useCmsStore'

withDefaults(
  defineProps<{
    hideHeader?: boolean
  }>(),
  {
    hideHeader: false
  }
)

const store = useCmsStore()
const isLoaded = ref(false)
let scrollTriggerCtx: ReturnType<typeof createScrollStagger> | null = null

onMounted(() => {
  nextTick(() => {
    // Discord 社群卡片與 Widget 統一由全域工廠函式調度 (100% 全站標準一致)
    scrollTriggerCtx = createScrollStagger(
      '#community .grid > div',
      '#community',
      { stagger: 0.08 }
    )
  })
})

onUnmounted(() => {
  if (scrollTriggerCtx) scrollTriggerCtx.revert()
})
</script>

