<template>
  <!-- 方案一：AI Copilot 對話視窗 — 模擬 Cursor AI / GitHub Copilot 即時對話介面 -->
  <div
    class="relative w-full h-[395px] sm:h-[430px] lg:h-[440px] xl:h-[485px] 2xl:h-[500px] rounded-2xl sm:rounded-3xl overflow-hidden border border-purple-500/30 bg-slate-900/90 shadow-2xl shadow-purple-950/50 backdrop-blur-xl flex flex-col"
  >
    <!-- 背景流光發光層 -->
    <div class="absolute -top-24 -right-24 w-64 h-64 bg-purple-500/12 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 -left-24 w-64 h-64 bg-cyan-600/12 rounded-full blur-3xl pointer-events-none"></div>

    <!-- 1. Mac 風格視窗標題列 -->
    <div class="h-[42px] sm:h-[44px] lg:h-[48px] px-3 sm:px-4 lg:px-5 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between flex-shrink-0">
      <!-- 視窗控制按鈕 -->
      <div class="flex items-center space-x-1.5 sm:space-x-2 overflow-hidden mr-2">
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-red-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-amber-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-emerald-500/80 flex-shrink-0"></div>
        <span class="ml-1 sm:ml-2 text-xs lg:text-sm font-mono text-slate-400 font-semibold flex items-center space-x-1 truncate">
          <span class="text-purple-400 flex-shrink-0">🤖</span>
          <span class="truncate max-w-[110px] sm:max-w-none">AI 學習助教 — 泰山職訓</span>
        </span>
      </div>
      <!-- 狀態標籤 -->
      <div class="flex items-center space-x-1.5 sm:space-x-2 flex-shrink-0">
        <span class="relative flex h-2 w-2">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
        </span>
        <span class="text-xs lg:text-sm font-mono text-emerald-300 font-bold tracking-wide">線上 Online</span>
      </div>
    </div>

    <!-- 2. 對話訊息列表區 (可滾動視覺) -->
    <div class="flex-1 overflow-hidden px-3.5 sm:px-5 lg:px-5 xl:px-6 py-3 sm:py-4 space-y-3 sm:space-y-3.5 flex flex-col justify-end">

      <!-- 訊息泡泡容器（從下往上顯示最新的訊息） -->
      <div
        v-for="(msg, idx) in visibleMessages"
        :key="idx"
        class="flex items-end gap-2.5"
        :class="msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'"
      >
        <!-- 頭像 -->
        <div
          class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl flex items-center justify-center text-sm flex-shrink-0 font-bold"
          :class="msg.role === 'user'
            ? 'bg-gradient-to-tr from-slate-600 to-slate-700 text-slate-200'
            : 'bg-gradient-to-tr from-purple-600 to-cyan-600 text-white shadow-md shadow-purple-500/30'"
        >
          {{ msg.role === 'user' ? '你' : '🤖' }}
        </div>

        <!-- 訊息泡泡 -->
        <div
          class="max-w-[75%] px-3 py-2 sm:px-3.5 sm:py-2.5 rounded-2xl text-xs sm:text-sm leading-relaxed"
          :class="msg.role === 'user'
            ? 'bg-slate-700/80 text-slate-200 rounded-tr-sm'
            : 'bg-gradient-to-br from-purple-950/70 to-slate-900 border border-purple-500/20 text-slate-100 rounded-tl-sm'"
        >
          <!-- AI 訊息：支援逐字打字動畫 -->
          <template v-if="msg.role === 'assistant' && idx === visibleMessages.length - 1 && isTyping">
            <span>{{ typingDisplayText }}</span>
            <span class="inline-block w-1.5 h-3 sm:h-3.5 bg-purple-400 animate-pulse ml-0.5 align-middle"></span>
          </template>
          <template v-else>
            {{ msg.content }}
          </template>
        </div>
      </div>

      <!-- 思考中指示器 (AI 正在回應時顯示) -->
      <div v-if="showThinking" class="flex items-end gap-2.5">
        <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-gradient-to-tr from-purple-600 to-cyan-600 text-white flex items-center justify-center text-sm flex-shrink-0">🤖</div>
        <div class="px-3 py-2.5 rounded-2xl rounded-tl-sm bg-gradient-to-br from-purple-950/70 to-slate-900 border border-purple-500/20">
          <div class="flex items-center space-x-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-bounce" style="animation-delay:0ms"></span>
            <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-bounce" style="animation-delay:150ms"></span>
            <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-bounce" style="animation-delay:300ms"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 底部輸入列 -->
    <div class="h-[58px] sm:h-[62px] lg:h-[66px] px-3 sm:px-4 lg:px-5 bg-gradient-to-r from-slate-950 via-slate-900 to-purple-950/30 border-t border-purple-500/20 flex items-center space-x-2.5 sm:space-x-3 flex-shrink-0">
      <!-- 模擬輸入框 -->
      <div class="flex-1 h-9 sm:h-10 rounded-xl bg-slate-800/60 border border-slate-700/60 px-3 flex items-center overflow-hidden">
        <span class="text-xs sm:text-sm text-slate-500 truncate">{{ currentQuestion }}</span>
        <span class="inline-block w-1 h-3.5 sm:h-4 bg-slate-500 animate-pulse ml-1 flex-shrink-0"></span>
      </div>
      <!-- 傳送按鈕 -->
      <button
        type="button"
        @click="nextConversation"
        class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-br from-purple-600 to-cyan-600 hover:from-purple-500 hover:to-cyan-500 text-white flex items-center justify-center text-base shadow-md shadow-purple-500/30 hover:scale-105 active:scale-95 transition-all flex-shrink-0 cursor-pointer"
        title="切換下一組對話"
      >
        ↻
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

// 對話腳本庫（每組對話展示不同學習場景）
interface Message {
  role: 'user' | 'assistant'
  content: string
}

const conversations: { question: string; messages: Message[] }[] = [
  {
    question: '我完全沒寫過程式，可以來學嗎？',
    messages: [
      { role: 'user', content: '我完全沒寫過程式，可以來學嗎？' },
      { role: 'assistant', content: '當然！本課程從 HTML 第一行開始，0 基礎也能順利跟上。920 小時循序漸進，有老師全程陪伴，你只需要帶著想學的心就夠了 ✨' }
    ]
  },
  {
    question: '學完之後能找到工作嗎？',
    messages: [
      { role: 'user', content: '學完之後能找到工作嗎？' },
      { role: 'assistant', content: '我們的畢業學員透過期末 Demo Day 展示真實作品，多位已成功轉職前端工程師。課程結合 Vue 3、Django、AI 串接等熱門技術，技能樹完整！🚀' }
    ]
  },
  {
    question: '全額補助是怎麼申請的？',
    messages: [
      { role: 'user', content: '全額補助是怎麼申請的？' },
      { role: 'assistant', content: '透過台灣就業通報名，符合資格者可獲得全額免費培訓，期間還有每月生活津貼補助。詳細資格請點擊下方「立即查看招生期別」了解 💰' }
    ]
  }
]

const currentConvIdx = ref(0)
const visibleMessages = ref<Message[]>([])
const showThinking = ref(false)
const isTyping = ref(false)
const typingDisplayText = ref('')
const currentQuestion = ref(conversations[0].question)

let typingTimer: ReturnType<typeof setInterval> | null = null
let cycleTimer: ReturnType<typeof setTimeout> | null = null

// 逐字打字動畫
function typeText(text: string, onDone?: () => void) {
  if (typingTimer) clearInterval(typingTimer)
  typingDisplayText.value = ''
  isTyping.value = true
  let idx = 0
  typingTimer = setInterval(() => {
    if (idx < text.length) {
      typingDisplayText.value += text[idx]
      idx++
    } else {
      clearInterval(typingTimer!)
      typingTimer = null
      isTyping.value = false
      onDone?.()
    }
  }, 28)
}

// 播放一組對話
function playConversation(idx: number) {
  const conv = conversations[idx]
  currentQuestion.value = conv.question

  // 先清空，顯示用戶訊息
  visibleMessages.value = [conv.messages[0]]
  showThinking.value = false
  isTyping.value = false

  // 短暫延遲後出現「思考中」
  cycleTimer = setTimeout(() => {
    showThinking.value = true
    // 再延遲後開始打字輸出 AI 回應
    cycleTimer = setTimeout(() => {
      showThinking.value = false
      visibleMessages.value = [...conv.messages]
      typeText(conv.messages[1].content, () => {
        // 打字完成後 6 秒進入下一組
        cycleTimer = setTimeout(() => {
          nextConversation()
        }, 6000)
      })
    }, 1200)
  }, 900)
}

function nextConversation() {
  if (typingTimer) clearInterval(typingTimer)
  if (cycleTimer) clearTimeout(cycleTimer)
  currentConvIdx.value = (currentConvIdx.value + 1) % conversations.length
  playConversation(currentConvIdx.value)
}

onMounted(() => {
  playConversation(0)
})

onUnmounted(() => {
  if (typingTimer) clearInterval(typingTimer)
  if (cycleTimer) clearTimeout(cycleTimer)
})
</script>
