<template>
  <!-- 外層容器：手機最小尺寸自適應高度 h-[395px] sm:h-[430px] lg:h-[475px] xl:h-[500px]，圓角 rounded-2xl sm:rounded-3xl -->
  <div
    class="relative w-full h-[395px] sm:h-[430px] lg:h-[475px] xl:h-[500px] rounded-2xl sm:rounded-3xl overflow-hidden border border-cyan-500/30 bg-slate-900/90 shadow-2xl shadow-cyan-950/50 backdrop-blur-xl flex flex-col justify-between"
  >
    <!-- 背景流光發光層 -->
    <div class="absolute -top-24 -right-24 w-64 h-64 bg-cyan-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 -left-24 w-64 h-64 bg-blue-600/15 rounded-full blur-3xl pointer-events-none"></div>

    <!-- 1. Mac 風格視窗頂部標題列 (固定高度 42px sm:44px lg:48px，左右內距 px-3 sm:px-4 lg:px-5) -->
    <div class="h-[42px] sm:h-[44px] lg:h-[48px] px-3 sm:px-4 lg:px-5 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between flex-shrink-0">
      <!-- 視窗控制按鈕 -->
      <div class="flex items-center space-x-1.5 sm:space-x-2 overflow-hidden mr-2">
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-red-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-amber-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-emerald-500/80 flex-shrink-0"></div>
        <span class="ml-1 sm:ml-2 text-xs lg:text-sm font-mono text-slate-400 font-semibold flex items-center space-x-1 truncate">
          <span class="text-cyan-400 flex-shrink-0">⚡</span>
          <span class="truncate max-w-[110px] xs:max-w-[160px] sm:max-w-none">AIChatWidget.vue</span>
        </span>
      </div>

      <!-- AI 狀態標籤 (超窄螢幕簡約自適應) -->
      <div class="flex items-center space-x-1.5 sm:space-x-2 flex-shrink-0">
        <span class="relative flex h-2 w-2">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-cyan-500"></span>
        </span>
        <span class="text-xs lg:text-sm font-mono text-cyan-300 font-bold tracking-wide">
          <span class="hidden xs:inline">AI Agent: </span>Generating
        </span>
      </div>
    </div>

    <!-- 2. AI Prompt 提示詞終端機指令列 (固定高度 38px sm:40px lg:44px) -->
    <div class="h-[38px] sm:h-[40px] lg:h-[44px] px-3 sm:px-4 lg:px-5 bg-slate-950/50 border-b border-slate-800/80 flex items-center space-x-2 text-xs lg:text-sm font-mono flex-shrink-0 overflow-hidden">
      <span class="text-purple-400 font-bold flex-shrink-0">✨ Prompt:</span>
      <span class="text-slate-200 truncate flex-1">{{ currentScenario.prompt }}</span>
      <span class="inline-block w-1.5 sm:w-2 h-3.5 sm:h-4 bg-cyan-400 animate-pulse flex-shrink-0"></span>
    </div>

    <!-- 3. VS Code 語法高亮即時代碼區域 (手機版 h-[235px] 內距 p-3.5，桌機 h-[300px]~[320px] 內距 p-6) -->
    <div class="h-[235px] sm:h-[268px] lg:h-[300px] xl:h-[320px] p-3.5 sm:p-5 lg:p-6 font-mono text-xs lg:text-sm leading-relaxed text-slate-300 bg-slate-900/60 overflow-hidden flex flex-col justify-between flex-shrink-0">
      <div class="space-y-0.5 sm:space-y-1 lg:space-y-1.5 overflow-hidden">
        <div class="text-slate-500 truncate">// 前端網頁技術 × AI 智能串聯實戰架構</div>
        <div class="truncate">
          <span class="text-purple-400">&lt;script</span>
          <span class="text-cyan-400"> setup</span>
          <span class="text-cyan-400"> lang=</span><span class="text-emerald-300">"ts"</span><span class="text-purple-400">&gt;</span>
        </div>
        <div class="pl-3 sm:pl-4 lg:pl-5 truncate">
          <span class="text-purple-400">import</span>
          <span class="text-slate-200"> { ref, onMounted } </span>
          <span class="text-purple-400">from</span>
          <span class="text-emerald-300"> 'vue'</span>
        </div>
        <div class="pl-3 sm:pl-4 lg:pl-5 truncate">
          <span class="text-purple-400">import</span>
          <span class="text-slate-200"> { useAiAssistant } </span>
          <span class="text-purple-400">from</span>
          <span class="text-emerald-300"> '@/stores/ai'</span>
        </div>
        <div class="pl-3 sm:pl-4 lg:pl-5 text-cyan-300 font-semibold truncate">
          <span class="text-blue-400">const</span>
          <span class="text-white"> { streamResponse } </span>
          <span class="text-purple-400">=</span>
          <span class="text-yellow-300"> useAiAssistant</span>()
        </div>
        <div class="pl-3 sm:pl-4 lg:pl-5 text-slate-400 truncate">
          <span class="text-blue-400">const</span>
          <span class="text-white"> msg </span>
          <span class="text-purple-400">=</span>
          <span class="text-yellow-300"> ref</span>(<span class="text-emerald-300">"{{ typingText }}"</span>)
        </div>
        <div class="truncate">
          <span class="text-purple-400">&lt;/script&gt;</span>
        </div>
      </div>

      <!-- 底部狀態列 (手機最小尺寸精簡自適應) -->
      <div class="pt-2 sm:pt-2.5 lg:pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs lg:text-sm text-slate-400 flex-shrink-0">
        <div class="flex items-center space-x-1.5 sm:space-x-3 truncate mr-2">
          <span>Vue 3.5</span>
          <span>•</span>
          <span class="hidden xs:inline">TypeScript</span>
          <span class="xs:hidden">TS</span>
          <span>•</span>
          <span class="truncate">Tailwind</span>
        </div>
        <div class="text-cyan-400 font-bold flex-shrink-0">
          ⚡ 920h 全端即戰力
        </div>
      </div>
    </div>

    <!-- 4. 即時互動生成預覽小卡 (固定高度 76px sm:78px lg:83px xl:88px，左右內距 px-3 sm:px-4 lg:px-5) -->
    <div class="h-[76px] sm:h-[78px] lg:h-[83px] xl:h-[88px] px-3 sm:px-4 lg:px-5 bg-gradient-to-r from-slate-950 via-slate-900 to-cyan-950/40 border-t border-cyan-500/30 flex items-center justify-between flex-shrink-0 overflow-hidden">
      <div class="flex items-center space-x-2.5 sm:space-x-3 lg:space-x-3.5 truncate flex-1 mr-2 sm:mr-3">
        <div class="w-8 h-8 sm:w-9 sm:h-9 lg:w-10 lg:h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white text-sm sm:text-base lg:text-lg shadow-md shadow-cyan-500/30 flex-shrink-0">
          🤖
        </div>
        <div class="truncate">
          <div class="text-xs lg:text-sm font-bold text-white flex items-center space-x-1.5">
            <span class="truncate">泰山職訓 AI 助教</span>
            <span class="px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 text-xs font-semibold flex-shrink-0">即時預覽</span>
          </div>
          <div class="text-xs lg:text-sm text-slate-300 mt-0.5 truncate">
            {{ currentScenario.previewMessage }}
          </div>
        </div>
      </div>

      <button
        type="button"
        @click="triggerNextScenario"
        title="點擊切換下一個實戰場景"
        class="px-2.5 sm:px-3 lg:px-4 py-1.5 lg:py-2 rounded-xl bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-xs lg:text-sm font-semibold transition-all hover:scale-105 active:scale-95 flex-shrink-0 cursor-pointer"
      >
        <span class="sm:hidden">切換 ↻</span>
        <span class="hidden sm:inline">切換範例 ↻</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

// 前端 ＋ AI 實戰場景展示清單
const scenarios = [
  {
    prompt: '用 Vue 3 建立 AI 智能對話與即時串流前端組件...',
    typingText: '你好！我是泰山職訓 AI 前端助手，準備好探索 920h 完整實戰了嗎？',
    previewMessage: '⚡ 已完成 Vue 3 + AI 流式串接前端組件生成！'
  },
  {
    prompt: '實作 Pinia 狀態管理 ＋ Tailwind 深色科技風儀表板...',
    typingText: '成功載入全域狀態管理與響應式深色科技介面！',
    previewMessage: '🎨 已渲染 100% 響應式現代前端 Dashboard！'
  },
  {
    prompt: '串接 Claude & OpenAI API 實作即時代碼分析與自動生成...',
    typingText: '串接 LLM API 成功，即時解析程式碼並提供最佳化建議！',
    previewMessage: '🚀 前端工程師必備之 AI 全端輔助開發流程！'
  }
]

const currentScenarioIndex = ref(0)
const currentScenario = computed(() => scenarios[currentScenarioIndex.value])
const typingText = ref('')
let typingTimer: ReturnType<typeof setInterval> | null = null
let cycleTimer: ReturnType<typeof setInterval> | null = null

function typeWriterEffect(text: string) {
  if (typingTimer) clearInterval(typingTimer)
  typingText.value = ''
  let idx = 0
  typingTimer = setInterval(() => {
    if (idx < text.length) {
      typingText.value += text[idx]
      idx++
    } else {
      clearInterval(typingTimer)
    }
  }, 35)
}

function triggerNextScenario() {
  currentScenarioIndex.value = (currentScenarioIndex.value + 1) % scenarios.length
  typeWriterEffect(currentScenario.value.typingText)
}

onMounted(() => {
  typeWriterEffect(currentScenario.value.typingText)
  // 每 8 秒自動輪播下一個實戰場景
  cycleTimer = setInterval(() => {
    triggerNextScenario()
  }, 8000)
})

onUnmounted(() => {
  if (typingTimer) clearInterval(typingTimer)
  if (cycleTimer) clearInterval(cycleTimer)
})
</script>
