<template>
  <section
    id="batches"
    class="relative overflow-hidden w-full max-w-[100vw]"
    :class="[
      hideHeader
        ? 'pt-8 pb-20 sm:pb-24 bg-transparent'
        : 'py-24 bg-transparent'
    ]"
  >
    <!-- 頂部與底部環境發光微暈 (加入 pointer-events-none 與嚴格局限) -->
    <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl pointer-events-none"></div>

    <div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full overflow-hidden">
      <!-- 區塊標題 (僅在首頁等未隱藏標頭時渲染) -->
      <div v-if="!hideHeader" class="text-center max-w-5xl mx-auto mb-14">
        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3">
          <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
          <span>Admission Batches ｜ 招生期別</span>
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight">
          招生期別與報名
        </h2>
        <p class="text-slate-400 mt-4 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed">
          把握政府自辦 100% 全額補助參訓機會，點擊「立即線上報名」直通台灣就業通官方報名系統。
        </p>

        <!-- 即時報名狀態指示看板 (讓民眾一眼秒懂當前報名狀態) -->
        <div class="mt-6 max-w-3xl mx-auto w-full px-2">
          <div
            class="relative rounded-2xl p-4 sm:p-5 border backdrop-blur-xl transition-all duration-300 overflow-hidden shadow-xl"
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
                  class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold font-mono tracking-wide"
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
                <p class="mt-1 text-xs sm:text-sm text-slate-300 leading-relaxed">
                  {{ notice.subline }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 期別卡片網格清單 (大器寬闊排版，空間充裕舒展，杜絕緊湊壓迫) -->
      <div id="batches-cards-grid" class="grid grid-cols-1 lg:grid-cols-2 gap-8 xl:gap-10 max-w-[1360px] mx-auto w-full">
        <div
          v-for="(batch, index) in sortedBatches"
          :key="batch.id"
          class="batch-card group relative rounded-3xl p-4 sm:p-8 lg:p-11 backdrop-blur-xl border transition-all duration-300 flex flex-col justify-between overflow-hidden will-change-transform transform-gpu cursor-default w-full"
          :class="[
            isBatchEnded(batch)
              ? 'bg-slate-950/45 border-slate-800/40 opacity-60 hover:opacity-85 grayscale-[40%] hover:grayscale-0 shadow-none'
              : 'card-subsurface-glow bg-slate-900/70 hover:bg-slate-900/90 border-slate-800/90 shadow-xl shadow-slate-950/60'
          ]"
        >
          <!-- 頂部流光光暈線 (僅活躍班級 Hover 時優雅顯現) -->
          <div
            v-if="!isBatchEnded(batch)"
            class="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
          ></div>

          <!-- 角落序號水印 (01, 02) -->
          <div
            class="absolute -right-2 -bottom-4 text-7xl font-mono font-black select-none pointer-events-none transition-colors"
            :class="isBatchEnded(batch) ? 'text-slate-900/50' : 'text-slate-800/20 group-hover:text-cyan-500/10'"
          >
            {{ String(index + 1).padStart(2, '0') }}
          </div>

          <!-- 上方資訊區 -->
          <div>
            <!-- 0.5 秒瞬間定錨狀態標籤 (求職者一眼秒懂開課與報名狀態) -->
            <div class="mb-3.5">
              <span
                class="inline-flex items-center space-x-1.5 px-3.5 py-1.5 rounded-full text-xs font-bold tracking-wide"
                :class="getFastStatusPill(batch).class"
              >
                <span>{{ getFastStatusPill(batch).label }}</span>
              </span>
            </div>

            <h3
              class="text-xl sm:text-2xl lg:text-3xl font-extrabold mb-5 flex items-center space-x-2.5 transition-colors break-words"
              :class="[
                isBatchEnded(batch)
                  ? 'text-slate-500 group-hover:text-slate-400'
                  : (isBatchClosed(batch) && !isBatchScreeningOrPreparing(batch) ? 'text-slate-200 group-hover:text-cyan-300' : 'text-white group-hover:text-cyan-300')
              ]"
            >
              <span>{{ batch.batch_name }}</span>
            </h3>

            <!-- 即時報名人數與熱度進度條 (Social Proof) -->
            <div v-if="batch.applicants_count !== undefined && batch.applicants_count !== null" class="mb-5 p-3.5 sm:p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90 shadow-inner">
              <div class="flex items-center justify-between text-xs sm:text-sm font-semibold mb-2">
                <span class="text-slate-300 font-medium">報名人數</span>
                <span
                  class="font-mono font-bold"
                  :class="isBatchEnded(batch) ? 'text-slate-400' : 'text-cyan-400'"
                >
                  已報名 {{ batch.applicants_count }} 人 / 招訓 {{ batch.planned_trainees || 24 }} 名
                </span>
              </div>
              <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
                <div
                  class="h-full rounded-full transition-all duration-1000"
                  :class="isBatchEnded(batch) ? 'bg-slate-700' : 'bg-gradient-to-r from-cyan-500 to-emerald-400 shadow-[0_0_8px_rgba(6,182,212,0.5)]'"
                  :style="{ width: `${Math.min(100, Math.round(((batch.applicants_count || 0) / (batch.planned_trainees || 24)) * 100))}%` }"
                ></div>
              </div>
            </div>

            <!-- 課程生命週期 5 階段流程步進軸 (Course Lifecycle Stepper) -->
            <div class="mb-7 p-3.5 sm:p-6 rounded-2xl bg-slate-950/80 border border-slate-800/90 shadow-inner overflow-hidden">
              <!-- 5 階段節點步進軸 (直線與圓心 100% 絕對幾何居中) -->
              <div class="relative px-1 sm:px-4">
                <!-- 圓圈與導軌線專用排 (高度固定 h-7，導軌線嚴格穿過圓心) -->
                <div class="relative h-7 flex items-center justify-between">
                  <!-- 導軌專屬通道 (left-3.5 至 right-3.5：嚴格鎖定在第 1 個與第 5 個圓心之間，永不右溢) -->
                  <div class="absolute left-3.5 right-3.5 top-1/2 -translate-y-1/2 h-0.5 overflow-hidden -z-0">
                    <!-- 背景灰色導軌線 -->
                    <div class="w-full h-full bg-slate-800"></div>
                    <!-- 走過的發光進度線 (結訓時為沉靜暗灰，活躍時為青綠流光) -->
                    <div
                      class="absolute left-0 top-0 h-full transition-all duration-700"
                      :class="isBatchEnded(batch) ? 'bg-slate-700' : 'bg-gradient-to-r from-emerald-500 to-cyan-400 shadow-[0_0_8px_rgba(6,182,212,0.6)]'"
                      :style="{ width: getLifecycleLineWidth(batch) }"
                    ></div>
                  </div>

                  <!-- 5 個圓圈節點 (直徑 28px，中心正好在 14px) -->
                  <div
                    v-for="(step, sIndex) in lifecycleSteps"
                    :key="step.key"
                    class="relative z-10 w-7 h-7 flex items-center justify-center flex-shrink-0"
                  >
                    <!-- 100% 實心遮光底座 (徹底阻斷後方導軌線與進度條穿透) -->
                    <div class="absolute inset-0 rounded-full bg-slate-950"></div>

                    <!-- 節點圓圈本體 (100% 實心不透明) -->
                    <div
                      class="relative z-10 w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold font-mono transition-all duration-300"
                      :class="getStepNodeClass(batch, sIndex + 1)"
                    >
                      <span v-if="getStepStatus(batch, sIndex + 1) === 'completed'">✓</span>
                      <span v-else>{{ sIndex + 1 }}</span>
                    </div>
                  </div>
                </div>

                <!-- 5 個文字標籤專用排 (垂直完全對齊上方圓圈) -->
                <div class="flex items-center justify-between mt-2.5">
                  <div
                    v-for="(step, sIndex) in lifecycleSteps"
                    :key="step.key"
                    class="w-7 flex justify-center"
                  >
                    <span
                      class="text-xs sm:text-sm font-semibold transition-colors duration-300 whitespace-nowrap text-center select-none"
                      :class="getStepTextClass(batch, sIndex + 1)"
                    >
                      {{ step.label }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- 生命週期動態焦點看板 -->
              <div class="mt-4 pt-3.5 border-t border-slate-800/80 text-sm sm:text-base flex items-start sm:items-center space-x-2 text-slate-200">
                <span class="flex-shrink-0 mt-0.5 sm:mt-0">{{ getLifecycleDetailNotice(batch).icon }}</span>
                <span class="leading-relaxed font-medium">{{ getLifecycleDetailNotice(batch).text }}</span>
              </div>
            </div>

            <div class="space-y-4 text-base text-slate-300 mb-8">
              <!-- 報名期間 (手機版直式/橫式自適應) -->
              <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3.5 border-b border-slate-800/80 gap-1 sm:gap-0">
                <span class="text-slate-400 flex items-center space-x-1.5 text-base">
                  <span>📅 報名起訖期間</span>
                </span>
                <div class="text-left sm:text-right">
                  <span
                    class="font-medium font-mono text-base"
                    :class="isBatchClosed(batch) ? 'text-slate-300' : 'text-white'"
                  >
                    {{ batch.enroll_start_date }} ～ {{ batch.enroll_end_date }}
                  </span>
                </div>
              </div>

              <!-- 甄試日期 (若有，手機版自適應不擠出) -->
              <div v-if="batch.screening_date" class="flex flex-col sm:flex-row sm:items-center justify-between pb-3.5 border-b border-slate-800/80 gap-1 sm:gap-0">
                <span class="text-slate-400 flex items-center space-x-1.5 text-base">
                  <span>📝 甄試辦理日期</span>
                </span>
                <div class="text-left sm:text-right flex items-center flex-wrap gap-1.5">
                  <span class="font-medium font-mono text-slate-200 text-base">
                    {{ batch.screening_date }}
                  </span>
                  <span v-if="isBatchScreeningOrPreparing(batch)" class="text-sm px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold">{{ isScreeningEnded(batch) ? '已甄試完畢' : '今日甄試中' }}</span>
                </div>
              </div>

              <!-- 訓練期間 (時程清單末項，手機版自適應) -->
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 sm:gap-0">
                <span class="text-slate-400 text-base">🚀 正式訓練期間</span>
                <div class="text-left sm:text-right">
                  <span
                    class="font-medium font-mono text-base"
                    :class="isBatchTraining(batch) ? 'text-emerald-300 font-bold' : isBatchScreeningOrPreparing(batch) ? 'text-cyan-300 font-bold' : 'text-white'"
                  >
                    {{ batch.training_start_date }} ～ {{ batch.training_end_date }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- 下方行動按鈕區 -->
          <div class="pt-4 border-t border-slate-800/80">
            <a
              v-if="isBatchEnrolling(batch)"
              :href="batch.apply_url"
              target="_blank"
              rel="noopener noreferrer"
              @click="store.trackBatchClick(batch.id)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-bold text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/30 hover:shadow-cyan-500/50 hover:-translate-y-0.5 active:scale-95 transition-all duration-200 flex items-center justify-center space-x-2 text-base lg:text-lg cursor-pointer"
            >
              <span>🔥 立即至<span class="inline-block">台灣就業通</span>報名</span>
              <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </a>
            <div
              v-else-if="isBatchTraining(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-emerald-400/90 bg-slate-900/90 border border-emerald-500/30 shadow-inner flex items-center justify-center space-x-2 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 text-emerald-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <span>🎓 本期正全力培訓衝刺中</span>
            </div>
            <div
              v-else-if="isBatchScreeningOrPreparing(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-cyan-300 bg-slate-900/90 border border-cyan-500/30 shadow-inner flex flex-wrap items-center justify-center gap-1.5 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 text-cyan-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span class="text-center">✨ 甄試結束 · 待開訓 ({{ batch.training_start_date }} 開課)</span>
            </div>
            <div
              v-else-if="isBatchUpcoming(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-purple-300/90 bg-slate-900/90 border border-purple-500/30 shadow-inner flex items-center justify-center space-x-2 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>⏳ 尚未開放報名（敬請期待）</span>
            </div>
            <div
              v-else
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-slate-400 bg-slate-900/90 border border-slate-800 shadow-inner flex items-center justify-center space-x-2 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636" />
              </svg>
              <span>⛔ 本期報名已截止受理</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 錯過本期之轉化與諮詢引導列 (打破死胡同，留住潛在學員) -->
      <div class="mt-12 p-5 sm:p-6 rounded-3xl bg-slate-900/60 backdrop-blur-xl border border-slate-800/80 max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-5 shadow-xl shadow-slate-950/40 w-full overflow-hidden">
        <div class="flex items-start sm:items-center space-x-3 text-slate-300 text-sm w-full sm:w-auto">
          <span class="text-2xl shrink-0">💡</span>
          <div class="text-left">
            <span class="font-bold text-white block sm:inline">錯過本期報名？</span>
            <span class="text-slate-400 block sm:inline">新一年度開班規劃中，歡迎預先諮詢掌握第一手快訊！</span>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-2.5 shrink-0 w-full sm:w-auto sm:flex sm:space-x-3 justify-end">
          <a
            :href="`tel:${(store.settings?.contact_phone || '(02) 2901-8274').replace(/[^0-9]/g, '')}`"
            class="px-3.5 py-2.5 rounded-xl text-sm font-bold text-cyan-300 bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 transition-all flex items-center justify-center space-x-1 shadow-sm active:scale-95"
          >
            <span>📞 招生專線</span>
          </a>
          <a
            :href="store.settings?.discord_invite_url || 'https://discord.gg/TrerFKG'"
            target="_blank"
            rel="noopener noreferrer"
            class="px-3.5 py-2.5 rounded-xl text-sm font-bold text-indigo-300 bg-indigo-500/10 hover:bg-indigo-500/20 border border-indigo-500/30 transition-all flex items-center justify-center space-x-1 shadow-sm active:scale-95"
          >
            <span>💬 官方 Discord</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, toRef, onMounted, nextTick, watch } from 'vue'
import { gsap } from '@/utils/motion'
import { useScrollStagger } from '@/composables/useScrollStagger'
import { useBatchTimeline } from '@/composables/useBatchTimeline'
import { useCmsStore } from '@/stores/useCmsStore'
import {
  isBatchEnded,
  isBatchTraining,
  isBatchClosed,
  getBatchEnrollmentNotice
} from '@/utils/batchStatus'

const props = withDefaults(
  defineProps<{
    hideHeader?: boolean
  }>(),
  {
    hideHeader: false
  }
)

const store = useCmsStore()
const notice = computed(() => getBatchEnrollmentNotice(store.batches))

// 招生期別 5 階段時序與生命週期演算 Composable (SoC & SRP)
const {
  lifecycleSteps,
  sortedBatches,
  getStepStatus,
  isScreeningEnded,
  getFastStatusPill,
  getLifecycleLineWidth,
  getStepNodeClass,
  getStepTextClass,
  getTrainingProgress,
  getLifecycleDetailNotice
} = useBatchTimeline(toRef(store, 'batches'))

// 動效管理
if (!props.hideHeader) {
  // 首頁滾動微升進場：統一由全域 Composable 調度
  useScrollStagger(
    '#batches-cards-grid .batch-card',
    '#batches-cards-grid',
    { stagger: 0.1 },
    () => store.batches.length
  )
} else {
  // 獨立分頁模式：直接以柔順動畫入場
  const playEnter = () => {
    nextTick(() => {
      gsap.fromTo(
        '#batches-cards-grid .batch-card',
        { y: 20, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.7, stagger: 0.08, ease: 'power1.out', clearProps: 'transform,opacity' }
      )
    })
  }
  onMounted(playEnter)
  watch(() => store.batches.length, playEnter)
}
</script>

