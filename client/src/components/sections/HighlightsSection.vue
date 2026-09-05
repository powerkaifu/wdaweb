<template>
	<section id="highlights" class="py-16 sm:py-24 lg:py-32 bg-transparent relative overflow-hidden">
		<!-- 背景流光點綴 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊前導標題 -->
			<div class="text-center max-w-4xl mx-auto mb-10 sm:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-mono font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Physical Learning Experience ｜ 實體沉浸價值</span>
				</div>
				<h2
					class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-black text-white tracking-tight leading-tight text-balance"
				>
					<span class="block">當你真的卡住時，</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400"
						>差別在身邊有沒有能一起解題的人</span
					>
				</h2>
				<p class="text-slate-400 mt-4 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed text-pretty">
					自學可以走得很遠。但當你面對一個看不懂的錯誤訊息時，有人可以一起討論、有同學可以交流，往往能讓你少繞很多彎路。這也是實體學習最難被取代的地方。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div class="flex md:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4">
				<span>👈 左右滑動瀏覽 4 大實體價值 👉</span>
			</div>

			<div
				id="highlights-cards-grid"
				class="flex md:grid md:grid-cols-2 xl:grid-cols-4 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 md:mx-0 md:px-0 gap-4 sm:gap-6 pb-4 md:pb-0"
			>
				<!-- 1. 老師陪你拆解問題 (Cyan Theme) -->
				<div
					class="highlight-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[84vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div
						class="absolute -right-2 -bottom-4 text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						01
					</div>

					<div>
						<div class="flex items-center justify-between mb-6">
							<div
								class="w-12 h-12 rounded-2xl bg-cyan-500/15 border border-cyan-500/40 text-cyan-300 flex items-center justify-center text-2xl shadow-[0_0_20px_rgba(6,182,212,0.2)]"
							>
								👨‍🏫
							</div>
							<span
								class="px-3 py-1 rounded-xl bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 font-mono font-extrabold text-sm tracking-wider"
							>
								MENTOR
							</span>
						</div>

						<h3 class="text-xl font-extrabold text-white mb-3 tracking-tight">老師陪你拆解問題</h3>
						<p class="text-base text-slate-200 leading-relaxed text-pretty">
							遇到問題，不必一個人對著錯誤訊息反覆猜測。不是直接告訴你答案，而是協助你理解「為什麼會錯、問題出在哪裡」，練習拆解問題的思維，而不是只找到一個暫時運作的答案。
						</p>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>思維訓練</span>
						<span class="text-cyan-400 font-bold">理解原因而非死背</span>
					</div>
				</div>

				<!-- 2. 專屬雙螢幕實作環境 (Blue Theme) -->
				<div
					class="highlight-card card-subsurface-blue relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[84vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div
						class="absolute -right-2 -bottom-4 text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						02
					</div>

					<div>
						<div class="flex items-center justify-between mb-6">
							<div
								class="w-12 h-12 rounded-2xl bg-blue-500/15 border border-blue-500/40 text-blue-300 flex items-center justify-center text-2xl shadow-[0_0_20px_rgba(59,130,246,0.2)]"
							>
								🖥️
							</div>
							<span
								class="px-3 py-1 rounded-xl bg-blue-500/10 text-blue-300 border border-blue-500/30 font-mono font-extrabold text-sm tracking-wider"
							>
								2X MONITORS
							</span>
						</div>

						<h3 class="text-xl font-extrabold text-white mb-3 tracking-tight">
							專屬<span class="inline-block">雙螢幕實作環境</span>
						</h3>
						<p class="text-base text-slate-200 leading-relaxed text-pretty">
							降低實作與切換的摩擦。一邊看示範、一邊寫程式、查資料與測試結果能同時進行。讓學習當下就親手實作，徹底擺脫「看影片覺得懂、開編輯器一片空白」的困境。
						</p>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>降低阻力</span>
						<span class="text-blue-400 font-bold">即時實作反饋</span>
					</div>
				</div>

				<!-- 3. 同儕一起學習成長 (Purple Theme) -->
				<div
					class="highlight-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[84vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div
						class="absolute -right-2 -bottom-4 text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						03
					</div>

					<div>
						<div class="flex items-center justify-between mb-6">
							<div
								class="w-12 h-12 rounded-2xl bg-purple-500/15 border border-purple-500/40 text-purple-300 flex items-center justify-center text-2xl shadow-[0_0_20px_rgba(168,85,247,0.2)]"
							>
								🤝
							</div>
							<span
								class="px-3 py-1 rounded-xl bg-purple-500/10 text-purple-300 border border-purple-500/30 font-mono font-extrabold text-sm tracking-wider"
							>
								PEER LEARNING
							</span>
						</div>

						<h3 class="text-xl font-extrabold text-white mb-3 tracking-tight">同儕一起學習成長</h3>
						<p class="text-base text-slate-200 leading-relaxed text-pretty">
							你不需要一個人面對每一次卡關。在班級中，你會發現「原來別人也會卡住」，並開始練習把自己的問題說清楚。同儕並肩討論、互相提點，往往比孤軍奮戰更容易突破盲點。
						</p>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>心理支持</span>
						<span class="text-purple-400 font-bold">同儕共同突破</span>
					</div>
				</div>

				<!-- 4. 920 小時集中沉浸 (Emerald Theme) -->
				<div
					class="highlight-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[84vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div
						class="absolute -right-2 -bottom-4 text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						04
					</div>

					<div>
						<div class="flex items-center justify-between mb-6">
							<div
								class="w-12 h-12 rounded-2xl bg-emerald-500/15 border border-emerald-500/40 text-emerald-300 flex items-center justify-center text-2xl shadow-[0_0_20px_rgba(16,185,129,0.2)]"
							>
								⏳
							</div>
							<span
								class="px-3 py-1 rounded-xl bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 font-mono font-extrabold text-sm tracking-wider"
							>
								920 HOURS
							</span>
						</div>

						<h3 class="text-xl font-extrabold text-white mb-3 tracking-tight">
							<span class="inline-block">920 小時</span>集中沉浸
						</h3>
						<p class="text-base text-slate-200 leading-relaxed text-pretty">
							零散自學往往缺乏大局觀。<span class="inline-block">920 小時</span
							>給你一段足夠長、足夠專注的時間，暫時放下外界干擾，把零碎的語法知識，真正沉澱為能獨立做出完整專案的實戰能力。
						</p>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>專注累積</span>
						<span class="text-emerald-400 font-bold">零散知識轉為實戰</span>
					</div>
				</div>
			</div>

			<!-- 每天與人一起學習 ｜ 實體交流與協作底蘊 (靈魂人文橫幅) -->
			<div class="mt-14 sm:mt-16 max-w-5xl xl:max-w-6xl mx-auto">
				<div
					class="relative rounded-3xl p-5 sm:p-8 lg:p-10 bg-gradient-to-br from-slate-900/95 via-slate-900/80 to-slate-950/95 border border-slate-800/90 backdrop-blur-xl shadow-2xl shadow-slate-950/70 overflow-hidden"
				>
					<!-- 背景微光點綴 -->
					<div
						class="absolute -top-20 -right-20 w-64 h-64 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"
					></div>
					<div
						class="absolute -bottom-20 -left-20 w-64 h-64 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"
					></div>

					<div class="relative z-10 space-y-6">
						<!-- 標題列與標籤 -->
						<div
							class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-5"
						>
							<h3
								class="text-2xl sm:text-2xl lg:text-3xl font-extrabold text-white tracking-tight flex items-start sm:items-center gap-2.5 sm:gap-3 text-balance"
							>
								<span class="text-2xl sm:text-3xl flex-shrink-0 mt-0.5 sm:mt-0">💬</span>
								<span class="leading-snug sm:leading-tight">
									<span class="block sm:inline">每天與人一起學習<span class="hidden sm:inline">，</span></span><span class="block sm:inline">是職訓很不一樣的地方</span>
								</span>
							</h3>
							<span
								class="hidden sm:inline-flex items-center px-3.5 py-1 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 text-xs font-mono font-bold tracking-wider w-fit"
							>
								HUMAN COLLABORATION
							</span>
						</div>

						<!-- 內文兩段 (保持 text-base sm:text-lg 大字，行高 1.8 舒緩，老花眼與中高齡友善) -->
						<div class="space-y-4 text-base sm:text-lg leading-relaxed text-pretty">
							<p class="text-slate-200">
								自學可以自己找答案，AI 也可以立即提供解答；但實體學習多了一個重要的過程：<strong
									class="text-cyan-300 font-bold"
									>與真實的人一起討論問題。</strong
								>
							</p>
							<p class="text-slate-300">
								你不只是練習怎麼說明自己的問題，也要學著仔細聆聽別人在問什麼，理解對方真正卡住的地方，再想辦法用對方聽得懂的方式解釋。老師與學員每天面對面交流，在一次次提問、討論與解釋中教學相長。
							</p>
						</div>

						<!-- 雙核心價值收束 (在同一個容器內，左右兩欄對稱呈現) -->
						<div
							class="p-5 sm:p-6 rounded-2xl bg-slate-950/60 border border-slate-800/80 grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6"
						>
							<!-- 左側項目 1 -->
							<div class="flex items-start gap-3">
								<div
									class="w-1.5 h-5 rounded-full bg-cyan-400 flex-shrink-0 mt-1 shadow-[0_0_8px_rgba(6,182,212,0.6)]"
								></div>
								<p class="text-base sm:text-lg font-bold text-slate-100 leading-relaxed text-pretty">
									不只是學習技術，也是練習如何表達、聆聽、理解與協作。
								</p>
							</div>

							<!-- 右側項目 2 -->
							<div
								class="flex items-start gap-3 border-t md:border-t-0 md:border-l border-slate-800/80 pt-3.5 md:pt-0 md:pl-6"
							>
								<div
									class="w-1.5 h-5 rounded-full bg-purple-400 flex-shrink-0 mt-1 shadow-[0_0_8px_rgba(168,85,247,0.6)]"
								></div>
								<p class="text-base sm:text-lg font-bold text-slate-100 leading-relaxed text-pretty">
									這些能力，也是在真實職場與團隊中不可或缺的核心能力。
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { createScrollStagger } from '@/utils/motion'
import { nextTick, onMounted, onUnmounted } from 'vue'

let scrollTriggerCtx: ReturnType<typeof createScrollStagger> | null = null

onMounted(() => {
	nextTick(() => {
		// 4 張核心優勢卡片統一由全域工廠函式調度 (嚴格與全站 power1.out 絲滑手感 100% 對齊)
		scrollTriggerCtx = createScrollStagger('#highlights-cards-grid .highlight-card', '#highlights-cards-grid', {
			yOffset: 28,
			duration: 0.85,
			stagger: 0.08,
			ease: 'power1.out',
			start: 'top 85%',
		})
	})
})

onUnmounted(() => {
	if (scrollTriggerCtx) scrollTriggerCtx.revert()
})
</script>
