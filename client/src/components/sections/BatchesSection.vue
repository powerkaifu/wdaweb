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
        <p class="text-slate-400 mt-4 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed text-center">
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
                <p class="mt-1 text-xs sm:text-sm text-slate-300 leading-relaxed text-justify">
                  {{ notice.subline }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 期別卡片網格清單 (平板單欄居中限寬，桌機雙欄大器舒展) -->
      <div id="batches-cards-grid" class="grid grid-cols-1 lg:grid-cols-2 gap-8 xl:gap-10 max-w-2xl lg:max-w-[1360px] mx-auto w-full">
        <div
          v-for="(batch, index) in (sortedBatches.length > 0 ? sortedBatches : store.batches)"
          :key="batch.id"
          :id="isCelebrationBatch(batch) ? 'batch-card-celebration' : undefined"
          class="batch-card group relative rounded-3xl p-4 sm:p-8 lg:p-11 backdrop-blur-xl border transition-all duration-300 flex flex-col justify-between overflow-hidden transform-gpu cursor-default w-full"
          :class="[
            isBatchEnded(batch)
              ? (isCelebrationBatch(batch)
                  ? 'border-emerald-500/60 bg-slate-900/90 shadow-2xl shadow-emerald-950/50 ring-1 ring-emerald-500/30'
                  : 'bg-slate-950/45 border-slate-800/40 opacity-60 hover:opacity-85 grayscale-[40%] hover:grayscale-0 shadow-none')
              : 'card-subsurface-glow bg-slate-900/70 hover:bg-slate-900/90 border-slate-800/90 shadow-xl shadow-slate-950/60'
          ]"
        >
          <!-- 頂部流光光暈線 (結訓慶典榮耀班級常駐顯現翡翠光輝，活躍班級 Hover 顯現) -->
          <div
            v-if="isCelebrationBatch(batch) && isBatchEnded(batch)"
            class="absolute top-0 left-0 right-0 h-[2.5px] bg-gradient-to-r from-transparent via-emerald-400 to-transparent shadow-[0_0_12px_rgba(16,185,129,0.8)] pointer-events-none"
          ></div>
          <div
            v-else-if="!isBatchEnded(batch)"
            class="absolute top-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-cyan-400 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
          ></div>

          <!-- 角落序號水印 (01, 02) -->
          <div
            class="absolute -right-2 -bottom-4 text-7xl font-mono font-black select-none pointer-events-none transition-colors"
            :class="isBatchEnded(batch) ? (isCelebrationBatch(batch) ? 'text-emerald-500/15' : 'text-slate-900/50') : 'text-slate-800/20 group-hover:text-cyan-500/10'"
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
              <div class="relative px-0.5 min-[400px]:px-2 sm:px-4">
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

                      <!-- 結訓慶典專屬：聲納波紋擴散光環 (Sonar Ripple Pulse) -->
                      <span
                        v-if="sIndex + 1 === 5 && getStepStatus(batch, 5) === 'completed' && isCelebrationBatch(batch)"
                        class="absolute inset-0 rounded-full bg-emerald-400 animate-ping opacity-35 pointer-events-none"
                      ></span>
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

              <!-- 生命週期動態焦點看板 (單行大器展示，自適應字級防折行) -->
              <div class="mt-4 pt-3.5 border-t border-slate-800/80 text-xs sm:text-sm lg:text-base flex items-center text-slate-200 min-w-0">
                <div class="flex items-center space-x-2 min-w-0 overflow-hidden">
                  <span class="flex-shrink-0 text-sm sm:text-base">{{ getLifecycleDetailNotice(batch).icon }}</span>
                  <span class="leading-relaxed font-medium whitespace-nowrap overflow-hidden text-ellipsis">{{ getLifecycleDetailNotice(batch).text }}</span>
                </div>
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
            <!-- 1. 報名中 -->
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

            <!-- 2. 圓滿結訓 (優先判定！水平置中顯示「本期已圓滿結訓」並內嵌「送上祝賀」按鈕) -->
            <div
              v-else-if="isBatchEnded(batch)"
              class="w-full py-2.5 sm:py-3 px-4 rounded-2xl bg-gradient-to-r from-emerald-950/80 via-slate-900/95 to-emerald-950/80 border border-emerald-500/50 shadow-lg shadow-emerald-950/40 flex flex-wrap items-center justify-center gap-3 sm:gap-4.5 text-base lg:text-lg select-none"
            >
              <div class="flex items-center space-x-2 text-emerald-300 font-bold tracking-wide text-sm sm:text-base lg:text-lg">
                <span class="text-lg sm:text-xl">🎓</span>
                <span>本期已圓滿結訓</span>
              </div>

              <!-- 🎉 送上祝賀互動按鈕 (與文字一同水平置中呈現) -->
              <button
                v-if="isCelebrationBatch(batch)"
                type="button"
                @click.stop="triggerCongratulations($event)"
                title="點擊為結訓學員送上祝賀星塵禮花"
                class="inline-flex items-center space-x-1.5 px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-xl text-xs sm:text-sm font-bold text-white bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 active:scale-95 transition-all shadow-md shadow-emerald-500/30 cursor-pointer select-none group/btn shrink-0"
              >
                <span class="text-sm sm:text-base group-hover/btn:scale-125 transition-transform">🎉</span>
                <span>送上祝賀</span>
                <span class="font-mono bg-emerald-950/90 px-2 py-0.5 rounded text-xs text-emerald-200 border border-emerald-400/40 font-semibold">{{ celebrationCount }}</span>
              </button>
            </div>

            <!-- 3. 正全力培訓衝刺中 -->
            <div
              v-else-if="isBatchTraining(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-emerald-400/90 bg-slate-900/90 border border-emerald-500/30 shadow-inner flex items-center justify-center space-x-2 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 text-emerald-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <span>🎓 本期正全力培訓衝刺中</span>
            </div>

            <!-- 4. 甄試結束待開訓 -->
            <div
              v-else-if="isBatchScreeningOrPreparing(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-cyan-300 bg-slate-900/90 border border-cyan-500/30 shadow-inner flex flex-wrap items-center justify-center gap-1.5 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 text-cyan-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span class="text-center">✨ 甄試結束 · 待開訓 ({{ batch.training_start_date }} 開課)</span>
            </div>

            <!-- 5. 尚未開放報名 -->
            <div
              v-else-if="isBatchUpcoming(batch)"
              class="w-full py-3.5 sm:py-4 px-3 rounded-2xl text-center font-semibold text-purple-300/90 bg-slate-900/90 border border-purple-500/30 shadow-inner flex items-center justify-center space-x-2 select-none text-base lg:text-lg"
            >
              <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>⏳ 尚未開放報名（敬請期待）</span>
            </div>

            <!-- 6. 報名截止 -->
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
import { ref, computed, toRef, onMounted, onUnmounted, nextTick, watch } from 'vue'
import confetti from 'canvas-confetti'
import { gsap } from '@/utils/motion'
import { useScrollStagger } from '@/composables/useScrollStagger'
import { useBatchTimeline } from '@/composables/useBatchTimeline'
import { useCmsStore } from '@/stores/useCmsStore'
import {
  isBatchEnded as rawIsBatchEnded,
  isBatchTraining as rawIsBatchTraining,
  isBatchClosed,
  isBatchEnrolling,
  isBatchScreeningOrPreparing,
  isBatchUpcoming,
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
  isCelebrationBatch,
  getFastStatusPill,
  getLifecycleLineWidth,
  getStepNodeClass,
  getStepTextClass,
  getTrainingProgress,
  getLifecycleDetailNotice,
  isCelebrationSimulated
} = useBatchTimeline(() => store.batches)

function isBatchEnded(batch: AdmissionBatch): boolean {
  if (isCelebrationSimulated.value && batch.id === 1) return true
  return rawIsBatchEnded(batch)
}

function isBatchTraining(batch: AdmissionBatch): boolean {
  if (isBatchEnded(batch)) return false
  return rawIsBatchTraining(batch)
}

// ===========================================================================
// 🎉 結訓榮耀慶典系統 (A + B + C 方案融合：量子禮花 + 祝福互動 + 榮耀光艙)
// ===========================================================================

// 方案 B：祝賀祝福計數器 (預設溫暖基底 68 次，支援持久化儲存)
const celebrationCount = ref<number>(68)
try {
  const saved = localStorage.getItem('wdaweb_grad_cheer_count')
  if (saved) {
    celebrationCount.value = Math.max(68, Number(saved) || 68)
  }
} catch (e) {}

// 當前是否有任何班級處於結訓慶典守護中（最新結訓班級，直到新期別出現交棒）
const hasCelebrationBatch = computed(() => {
  const list = sortedBatches.value.length > 0 ? sortedBatches.value : store.batches
  return list.some(b => isCelebrationBatch(b) && isBatchEnded(b))
})

// 方案 A：第 1 期卡片兩側精準定錨・微光星塵禮花 (聚焦於卡片兩側，不遮擋全螢幕)
function fireGraduationConfetti() {
  // 符合全站暗黑科技之高雅配色：電光青、翡翠綠、天藍、星輝金、高能白
  const colors = ['#06b6d4', '#10b981', '#38bdf8', '#fbbf24', '#ffffff']

  // 動態精確抓取第 1 期卡片的視窗幾何座標 (BoundingClientRect)
  const cardEl = document.getElementById('batch-card-celebration') || document.querySelector('.batch-card')
  let leftX = 0.22
  let rightX = 0.48
  let originY = 0.65

  if (cardEl) {
    const rect = cardEl.getBoundingClientRect()
    // 依卡片實際寬高，定錨於卡片左緣與右緣內縮 15px 處
    leftX = Math.max(0.05, Math.min(0.95, (rect.left + 15) / window.innerWidth))
    rightX = Math.max(0.05, Math.min(0.95, (rect.right - 15) / window.innerWidth))
    // 發射高度定錨在卡片中下部 65% 處
    originY = Math.max(0.15, Math.min(0.85, (rect.top + rect.height * 0.65) / window.innerHeight))
  }

  // 卡片左側向上內側拋射弧線 (聚焦於卡片左上方，大號飽滿星塵禮花)
  confetti({
    particleCount: 48,
    angle: 68,
    spread: 46,
    startVelocity: 35,
    origin: { x: leftX, y: originY },
    colors,
    ticks: 220,
    gravity: 1.02,
    scalar: 1.45,
    shapes: ['circle', 'square'],
    disableForReducedMotion: true
  })

  // 卡片右側向上內側拋射弧線 (聚焦於卡片右上方，大號飽滿星塵禮花)
  confetti({
    particleCount: 48,
    angle: 112,
    spread: 46,
    startVelocity: 35,
    origin: { x: rightX, y: originY },
    colors,
    ticks: 220,
    gravity: 1.02,
    scalar: 1.45,
    shapes: ['circle', 'square'],
    disableForReducedMotion: true
  })
}

// 方案 B：點擊按鈕主動送祝福 (游標專屬飽滿星塵爆發)
function triggerCongratulations(event: MouseEvent) {
  celebrationCount.value++
  try {
    localStorage.setItem('wdaweb_grad_cheer_count', String(celebrationCount.value))
  } catch (e) {}

  const rect = (event.currentTarget as HTMLElement)?.getBoundingClientRect()
  const x = rect ? (rect.left + rect.width / 2) / window.innerWidth : 0.5
  const y = rect ? (rect.top + rect.height / 2) / window.innerHeight : 0.5

  confetti({
    particleCount: 45,
    spread: 72,
    origin: { x, y },
    colors: ['#10b981', '#06b6d4', '#fbbf24', '#38bdf8', '#ffffff'],
    ticks: 190,
    gravity: 0.95,
    scalar: 1.35,
    disableForReducedMotion: true
  })
}

// 方案 A 入場自動施放守護 (每 session 僅自發施放一次，絕不擾民)
let confettiObserver: IntersectionObserver | null = null

onMounted(() => {
  nextTick(() => {
    if (hasCelebrationBatch.value && typeof IntersectionObserver !== 'undefined') {
      const gridEl = document.getElementById('batches-cards-grid')
      if (gridEl) {
        confettiObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const hasFired = sessionStorage.getItem('wdaweb_grad_confetti_auto_fired')
              if (!hasFired) {
                sessionStorage.setItem('wdaweb_grad_confetti_auto_fired', 'true')
                setTimeout(() => {
                  fireGraduationConfetti()
                }, 350)
              }
              confettiObserver?.disconnect()
            }
          })
        }, { threshold: 0.25 })
        confettiObserver.observe(gridEl)
      }
    }
  })
})

onUnmounted(() => {
  if (confettiObserver) {
    confettiObserver.disconnect()
    confettiObserver = null
  }
})

// 動效管理：僅在首頁有標頭滾動時啟用 ScrollTrigger；在獨立招生頁面由外層 page transition 驅動，維持 100% 穩定立即可見
if (!props.hideHeader) {
  useScrollStagger(
    '#batches-cards-grid .batch-card',
    '#batches-cards-grid',
    { stagger: 0.1 },
    () => store.batches.length
  )
}
</script>

