<template>
  <!-- 方案一：AI Copilot 對話視窗 — 模擬 Cursor / ChatGPT 即時對話訊息串流 -->
  <div
    class="relative w-full h-[395px] sm:h-[430px] lg:h-[440px] xl:h-[485px] 2xl:h-[500px] rounded-2xl sm:rounded-3xl overflow-hidden border border-cyan-500/35 bg-slate-900/90 shadow-2xl shadow-cyan-950/40 backdrop-blur-xl flex flex-col justify-between"
  >
    <!-- 背景流光發光層 -->
    <div class="absolute -top-24 -right-24 w-64 h-64 bg-cyan-500/12 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 -left-24 w-64 h-64 bg-blue-600/12 rounded-full blur-3xl pointer-events-none"></div>

    <!-- 1. Mac 風格視窗標題列 -->
    <div class="h-[42px] sm:h-[44px] lg:h-[48px] px-3 sm:px-4 lg:px-5 bg-slate-950/85 border-b border-slate-800 flex items-center justify-between flex-shrink-0 z-20">
      <!-- 視窗控制按鈕 -->
      <div class="flex items-center space-x-1.5 sm:space-x-2 overflow-hidden mr-2">
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-red-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-amber-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-emerald-500/80 flex-shrink-0"></div>
        <span class="ml-1 sm:ml-2 text-xs lg:text-sm font-mono text-slate-400 font-semibold flex items-center space-x-1.5 truncate">
          <span class="text-cyan-400 flex-shrink-0">🤖</span>
          <span class="truncate max-w-[120px] xs:max-w-[160px] sm:max-w-none">AI 學習助教 — 泰山職訓問答</span>
        </span>
      </div>

      <!-- 狀態標籤與當前輪數統計 -->
      <div class="flex items-center space-x-2 sm:space-x-3 flex-shrink-0">
        <span class="hidden xs:inline-flex text-xs font-mono px-2 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">
          題庫 {{ currentDisplayRound }}/{{ conversations.length }}
        </span>
        <div class="flex items-center space-x-1.5">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span class="text-xs lg:text-sm font-mono text-emerald-300 font-bold tracking-wide">
            <span class="hidden sm:inline">線上 </span>Live
          </span>
        </div>
      </div>
    </div>

    <!-- 2. 對話訊息列表區（無限往上移動滾動，不清空畫面） -->
    <div class="relative flex-1 overflow-hidden">
      <!-- 頂部平滑消隱遮罩：往上滾動的歷史訊息優雅漸漸融入深色背景 -->
      <div class="absolute inset-x-0 top-0 h-8 bg-gradient-to-b from-slate-900 via-slate-900/60 to-transparent pointer-events-none z-10"></div>

      <!-- 滾動容器 -->
      <div
        ref="scrollContainerRef"
        class="h-full overflow-y-auto px-3.5 sm:px-5 lg:px-5 xl:px-6 py-4 space-y-3 sm:space-y-4 scroll-smooth custom-scrollbar"
      >
        <!-- 訊息串列 -->
        <TransitionGroup name="chat-msg" tag="div" class="space-y-3 sm:space-y-4">
          <div
            v-for="(msg, idx) in chatHistory"
            :key="msg.id"
            class="flex items-start gap-2.5"
            :class="msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'"
          >
            <!-- 頭像 -->
            <div
              class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl flex items-center justify-center text-xs sm:text-sm flex-shrink-0 font-bold shadow-md select-none mt-0.5"
              :class="msg.role === 'user'
                ? 'bg-gradient-to-tr from-slate-600 to-slate-700 text-slate-200'
                : 'bg-gradient-to-tr from-cyan-500 to-blue-600 text-white shadow-cyan-500/30'"
            >
              {{ msg.role === 'user' ? '你' : '🤖' }}
            </div>

            <!-- 訊息泡泡 -->
            <div
              class="max-w-[82%] sm:max-w-[78%] px-3.5 py-2.5 sm:px-4 sm:py-3 rounded-2xl text-xs sm:text-sm leading-relaxed tracking-wide shadow-sm"
              :class="msg.role === 'user'
                ? 'bg-slate-700/85 text-slate-100 rounded-tr-sm border border-slate-600/50'
                : 'bg-gradient-to-br from-slate-900 via-slate-900/95 to-cyan-950/40 border border-cyan-500/30 text-slate-200 rounded-tl-sm'"
            >
              <!-- 提問人 / AI 助教標籤 -->
              <div
                class="text-xs font-mono font-semibold mb-1 select-none flex items-center gap-1.5"
                :class="msg.role === 'user' ? 'text-slate-400 justify-end' : 'text-cyan-300'"
              >
                <span>{{ msg.role === 'user' ? '轉職諮詢訪客' : '泰山職訓 AI 助教' }}</span>
                <span v-if="msg.tag" class="px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-200 text-xs font-normal">
                  {{ msg.tag }}
                </span>
              </div>

              <!-- 內容顯示：AI 最新一條訊息支援打字串流光標 -->
              <div class="whitespace-pre-line text-slate-200">
                <template v-if="msg.role === 'assistant' && msg.id === currentTypingMsgId">
                  <span>{{ typingDisplayText }}</span>
                  <span class="inline-block w-1.5 h-3.5 sm:h-4 bg-cyan-400 animate-pulse ml-0.5 align-middle"></span>
                </template>
                <template v-else>
                  {{ msg.content }}
                </template>
              </div>
            </div>
          </div>
        </TransitionGroup>

        <!-- 思考中脈衝指示器 (AI 正在運算回應時推進畫面) -->
        <div v-if="showThinking" class="flex items-start gap-2.5">
          <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 text-white flex items-center justify-center text-xs sm:text-sm flex-shrink-0 shadow-md shadow-cyan-500/30 select-none mt-0.5">
            🤖
          </div>
          <div class="px-3.5 py-2.5 rounded-2xl rounded-tl-sm bg-gradient-to-br from-slate-900 to-cyan-950/40 border border-cyan-500/30">
            <div class="flex items-center space-x-1.5 py-0.5">
              <span class="text-xs font-mono text-cyan-300 mr-1.5">AI 思考回覆中</span>
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-bounce" style="animation-delay:0ms"></span>
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-bounce" style="animation-delay:160ms"></span>
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-bounce" style="animation-delay:320ms"></span>
            </div>
          </div>
        </div>

        <!-- 滾動定錨底部哨兵元素 -->
        <div ref="bottomAnchorRef" class="h-1"></div>
      </div>
    </div>

    <!-- 3. 底部輸入模擬列 -->
    <div class="h-[56px] sm:h-[60px] lg:h-[64px] px-3 sm:px-4 lg:px-5 bg-gradient-to-r from-slate-950 via-slate-900 to-cyan-950/40 border-t border-cyan-500/25 flex items-center space-x-2.5 sm:space-x-3 flex-shrink-0 z-20">
      <!-- 模擬輸入框（動態顯示下一題提示） -->
      <div class="flex-1 h-9 sm:h-10 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 px-3 flex items-center overflow-hidden transition-colors">
        <span class="text-cyan-400 font-mono text-xs mr-1.5 font-bold select-none">💬</span>
        <span class="text-xs sm:text-sm text-slate-300 truncate font-sans">{{ currentQuestionPreview }}</span>
        <span class="inline-block w-1.5 h-3.5 sm:h-4 bg-cyan-400 animate-pulse ml-1 flex-shrink-0"></span>
      </div>

      <!-- 下一題按鈕（手動加速快轉） -->
      <button
        type="button"
        @click="fastForwardNext"
        class="h-9 sm:h-10 px-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white flex items-center justify-center space-x-1.5 text-xs font-bold shadow-md shadow-cyan-500/30 hover:scale-105 active:scale-95 transition-all flex-shrink-0 cursor-pointer"
        title="立即跳至下一個民眾關心議題"
      >
        <span>下一題</span>
        <span class="text-sm leading-none">→</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick, onMounted, onUnmounted } from 'vue'

// 對話訊息模型
interface ChatMessage {
  id: string
  role: 'user' | 'assistant'
  content: string
  tag?: string
}

// 題庫模型
interface QAItem {
  tag: string
  question: string
  answer: string
}

// ── 豐富多元的課程特色與民眾核心關切題庫（共 16 大精選問答）──────────
const conversations: QAItem[] = [
  {
    tag: '零基礎轉職',
    question: '我完全沒有程式底子、不是理工科系，真的學得會嗎？',
    answer: '完全可以！課程從 HTML/CSS 最基礎的第一行語法教起。專業講師全程實體授課指導，遇到問題當場看螢幕解題，920 小時循序漸進，帶你從零開始獨立完成前後端專題作品！✨'
  },
  {
    tag: '政府補助',
    question: '政府全額補助學費是真的嗎？受訓期間還有生活津貼？',
    answer: '是真的！符合非自願離職、中高齡、特定對象或待業者身分，學費 100% 由政府全額補助。符合就業保險法規者，每月還能請領原投保薪資 60% 的職訓生活津貼，安心學習無負擔！💰'
  },
  {
    tag: '920h實作',
    question: '為什麼訓練時數長達 920 小時？和一般短期課程有什麼不同？',
    answer: '920 小時不只是學語法，而是透過系統化實作，從前端、後端 API、資料庫到 AI 輔助開發與專題，逐步培養完成完整網站與專案的能力。🔥'
  },
  {
    tag: 'AI輔助開發',
    question: '現在 AI 寫程式這麼厲害，學網頁會不會被 AI 取代？',
    answer: 'AI 能幫你寫程式，但不能代替你理解需求、設計架構與完成產品。本專班教你運用 AI 輔助開發、做架構設計、除錯與 API 串聯，培養與 AI 協作完成產品的能力。🤖'
  },
  {
    tag: '一人雙螢幕',
    question: '泰山職訓場的教學環境與電腦設備好嗎？',
    answer: '非常完善！每位學員享有專屬工作位，配置高效能主機與「一人雙螢幕」，一邊寫 Code 一邊即時看瀏覽器渲染。冷氣空調教室、高速光纖網路，打造專業工程師沉浸式實體學習環境！🖥️'
  },
  {
    tag: '就業出路',
    question: '結訓後的就業出路有哪些方向？',
    answer: '結訓後具備完整的前端與專案作品集，可投遞應徵前端網頁工程師、Web 全端助理工程師、UI/UX 前端開發者等職缺，憑扎實的實案成果在求職市場展現實力！🎯'
  },
  {
    tag: '專題作品',
    question: '結訓時每個人都會有自己的獨立專題作品嗎？',
    answer: '是的！課程包含完整的專題實作階段。每位學員都會獨立從需求規劃、資料庫設計到前後端雲端部署，完成具備公開網址與 GitHub 原始碼的個人代表作，面試直接秀給主管看！🏆'
  },
  {
    tag: '全端資料庫',
    question: '除了前端 Vue 3，還會學到後端與資料庫技術嗎？',
    answer: '會的！課程包含 Node.js 執行環境、RESTful API 設計與 MongoDB NoSQL 資料庫塑模與操作，讓你不只是單純切版，而是擁有打通「前端介面 ➔ API 串接 ➔ 資料庫存取」完整閉環架構的全端思維！🌐'
  },
  {
    tag: '破除年齡焦慮',
    question: '我已經 35 歲以上或 40 歲了，跨領域轉職軟體業會太晚嗎？',
    answer: '歷屆都有許多 30 歲、40 歲以上學員順利轉職成功！企業在乎的是你能否解決問題與主動學習的態度，920 小時累積的實戰作品加上過去職場累積的溝通成熟度，往往是你的獨特加分優勢！💪'
  },
  {
    tag: '甄試指南',
    question: '報名後需要筆試或口試嗎？該如何準備甄試？',
    answer: '報名截止後會有筆試（網頁設計丙級試題）與面試（評估學習動機、就業決心與出席穩定度）。展現誠懇積極的轉職態度與全力以赴的準備，錄取機會非常高！📋'
  },
  {
    tag: '師資指導',
    question: '如果上課遇到 Bug 卡關、跟不上進度時怎麼辦？',
    answer: '實體班最大的價值就是講師在現場隨時指導！卡關時老師直接看你的螢幕解惑。下課與週末還有專屬 Discord 班級社群，同學互相交流討論，絕不讓你孤軍奮戰！🤝'
  },
  {
    tag: '交通地理',
    question: '泰山訓練場的位置在哪裡？通勤交通方便嗎？',
    answer: '位於新北市泰山區貴子里致遠新村 55 之 1 號（近輔仁大學）。可搭乘捷運新莊線至「輔大站」或機場捷運「泰山貴和站」，轉乘公車即可抵達，訓練場亦備有汽機車停車場方便通勤！🚌'
  },
  {
    tag: '文組跨考',
    question: '我是文組、商科或設計背景，邏輯不好也能學嗎？',
    answer: '完全不用擔心！程式開發如同學習一種結構嚴謹的新語言，文組的文字組織力、商科的商業邏輯、設計的美學感受，在前端領域都是非常亮眼的特質，往年很多最優秀的學員都是跨領域出身！🎨'
  },
  {
    tag: '生活津貼金額',
    question: '非自願離職者領取的職訓生活津貼金額大概是多少？',
    answer: '依《就業保險法》規定，非自願離職者經公立就業服務機構推介參訓，受訓期間每月按退保前 6 個月平均月投保薪資的 60% 發給，最長發給 6 個月，讓你在 920 小時培訓期間無經濟後顧之憂！💵'
  },
  {
    tag: '最新技術棧',
    question: '課程中前端技術棧包含哪些最新工具？',
    answer: '涵蓋現代前端必備核心：HTML5/CSS3、JavaScript ES6+、Vue 3 Composition API、TypeScript 強型別、Tailwind CSS、Pinia 狀態管理、Vite 建置工具與 Git 版本控制，緊跟當前業界招募主流標準！⚡'
  },
  {
    tag: '出勤與請假規範',
    question: '上課時間是如何安排的？請假會有時數限制嗎？',
    answer: '週一至週五白天（8:10~16:35）實體授課，請假時數不得超過總訓練時數的 10%（約 92 小時），確保每位學員都能扎實吸收完整的 920 小時專業課程！⏰'
  }
]

// ── 狀態管理 ────────────────────────────────────────────────────────
const chatHistory = ref<ChatMessage[]>([])
const scrollContainerRef = ref<HTMLElement | null>(null)
const bottomAnchorRef = ref<HTMLElement | null>(null)

const showThinking = ref(false)
const currentTypingMsgId = ref<string | null>(null)
const typingDisplayText = ref('')
const currentQuestionPreview = ref('')
const currentDisplayRound = ref(1)

// 洗牌抽樣隊列（不重複顯示直至全部抽完，再重啟新一輪）
let unvisitedIndices: number[] = []
let activeTimer: ReturnType<typeof setTimeout> | null = null
let typingInterval: ReturnType<typeof setInterval> | null = null

// 隨機不重複取得下一個問題索引
function getNextIndex(): number {
  if (unvisitedIndices.length === 0) {
    // 重新產生完整索引陣列 [0, 1, 2, ..., N-1]
    unvisitedIndices = Array.from({ length: conversations.length }, (_, i) => i)
    // Fisher-Yates 洗牌演算法
    for (let i = unvisitedIndices.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[unvisitedIndices[i], unvisitedIndices[j]] = [unvisitedIndices[j], unvisitedIndices[i]]
    }
  }
  // 計算當前輪次已展示題數（1 ~ N）
  currentDisplayRound.value = conversations.length - unvisitedIndices.length + 1
  return unvisitedIndices.pop()!
}

// 平滑自動捲動到底部，推動畫面向上推進
function scrollToBottom(smooth = true) {
  nextTick(() => {
    if (scrollContainerRef.value) {
      scrollContainerRef.value.scrollTo({
        top: scrollContainerRef.value.scrollHeight,
        behavior: smooth ? 'smooth' : 'auto'
      })
    }
  })
}

// 逐字打字動畫
function streamText(fullText: string, onDone: () => void) {
  if (typingInterval) clearInterval(typingInterval)
  typingDisplayText.value = ''
  let charIdx = 0

  typingInterval = setInterval(() => {
    if (charIdx < fullText.length) {
      typingDisplayText.value += fullText[charIdx]
      charIdx++
      // 隨字數推進保持視窗往下捲動
      if (charIdx % 3 === 0) {
        scrollToBottom(false)
      }
    } else {
      if (typingInterval) clearInterval(typingInterval)
      typingInterval = null
      scrollToBottom(true)
      onDone()
    }
  }, 24)
}

// 推進一輪新的問答（不刷新既有畫面，只往上堆疊）
function triggerNextQA() {
  clearTimers()

  const qIndex = getNextIndex()
  const qa = conversations[qIndex]

  // 1. 底部輸入框顯示即將發送的問題
  currentQuestionPreview.value = qa.question

  // 延遲 600ms 送出提問，模擬訪客輸入完送出
  activeTimer = setTimeout(() => {
    const userMsgId = `user-${Date.now()}`
    chatHistory.value.push({
      id: userMsgId,
      role: 'user',
      content: qa.question,
      tag: qa.tag
    })

    // 防爆保護：如果歷史訊息過多（> 18 則），移除最前頭最早的 2 則以保證極致效能
    if (chatHistory.value.length > 18) {
      chatHistory.value.splice(0, 2)
    }

    scrollToBottom(true)

    // 2. 顯示 AI 正在思考
    activeTimer = setTimeout(() => {
      showThinking.value = true
      scrollToBottom(true)

      // 3. 思考 1.1 秒後，AI 開始生成回覆
      activeTimer = setTimeout(() => {
        showThinking.value = false

        const aiMsgId = `ai-${Date.now()}`
        currentTypingMsgId.value = aiMsgId

        chatHistory.value.push({
          id: aiMsgId,
          role: 'assistant',
          content: qa.answer,
          tag: qa.tag
        })

        scrollToBottom(true)

        // 4. 打字機串流輸出
        streamText(qa.answer, () => {
          currentTypingMsgId.value = null

          // 打字完成後，留出 5.5 秒讓使用者舒適閱讀，隨後自動觸發下一則（不刷新，一直往上跑）
          activeTimer = setTimeout(() => {
            triggerNextQA()
          }, 5500)
        })
      }, 1100)
    }, 700)
  }, 600)
}

// 手動快速切換到下一題
function fastForwardNext() {
  clearTimers()
  // 若當前正在打字，將當前訊息補齊
  if (currentTypingMsgId.value) {
    const activeMsg = chatHistory.value.find(m => m.id === currentTypingMsgId.value)
    if (activeMsg) {
      // 找到答案直接填入
      const found = conversations.find(c => c.answer.startsWith(typingDisplayText.value.slice(0, 8)))
      if (found) {
        activeMsg.content = found.answer
      }
    }
    currentTypingMsgId.value = null
  }
  showThinking.value = false
  triggerNextQA()
}

function clearTimers() {
  if (activeTimer) {
    clearTimeout(activeTimer)
    activeTimer = null
  }
  if (typingInterval) {
    clearInterval(typingInterval)
    typingInterval = null
  }
}

onMounted(() => {
  // 初次掛載時先預先置入一組歷史對話，讓視窗有對話感
  const firstIdx = getNextIndex()
  const firstQA = conversations[firstIdx]

  chatHistory.value.push(
    {
      id: 'init-1',
      role: 'user',
      content: firstQA.question,
      tag: firstQA.tag
    },
    {
      id: 'init-2',
      role: 'assistant',
      content: firstQA.answer,
      tag: firstQA.tag
    }
  )

  scrollToBottom(false)

  // 3.5 秒後自然推進下一題，開始滾動
  activeTimer = setTimeout(() => {
    triggerNextQA()
  }, 3500)
})

onUnmounted(() => {
  clearTimers()
})
</script>

<style scoped>
/* 專屬極致暗黑低調滾動條 */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(6, 182, 212, 0.25);
  border-radius: 9999px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(6, 182, 212, 0.5);
}

/* 訊息進入過渡動畫：由下往上平滑推入 */
.chat-msg-enter-active {
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
.chat-msg-enter-from {
  opacity: 0;
  transform: translateY(18px) scale(0.98);
}
.chat-msg-leave-active {
  transition: all 0.25s ease-out;
}
.chat-msg-leave-to {
  opacity: 0;
  transform: translateY(-12px);
}
</style>
