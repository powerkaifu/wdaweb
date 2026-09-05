<template>
	<section id="path-comparison" class="py-24 sm:py-28 lg:py-32 bg-transparent relative overflow-hidden">
		<!-- 背景環境微光 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊前導標頭 (大器單行標題，中高齡友善大字) -->
			<div class="text-center max-w-4xl mx-auto mb-16">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-xs font-mono font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Explore Options ｜ 比較選擇</span>
				</div>
				<h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight text-balance">
					<span class="block sm:inline">不只有一條路，</span>
					<span
						class="block sm:inline mt-1 sm:mt-0 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400"
						>你可以怎麼開始？</span
					>
				</h2>
				<p
					class="text-slate-400 mt-4 text-base sm:text-lg max-w-4xl mx-auto leading-relaxed text-pretty text-justify sm:text-center"
				>
					如果你正在思考轉職，不一定只有「報名職訓」這一個答案。你也可以自學、使用 AI
					學習，或在工作中逐步累積能力。不同方法適合不同的人，真正重要的是：<span class="text-slate-200 font-bold"
						>你現在需要的是什麼？</span
					>
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div class="flex md:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4">
				<span>👈 左右滑動橫向比較 3 種學習路徑 👉</span>
			</div>

			<!-- 三種路徑對照 (手機版橫向 Snap 滑動比對，桌機維持大器 3 欄並排) -->
			<div
				id="path-comparison-grid"
				class="flex md:grid md:grid-cols-3 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 md:mx-0 md:px-0 gap-4 sm:gap-6 xl:gap-8 pb-4 md:pb-0"
			>
				<!-- 路徑 1：自學 ＋ AI -->
				<div
					class="path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default hover:border-blue-500/50 transition-[border-color,box-shadow] duration-300 w-[86vw] max-w-[360px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<!-- 標題與圖標 -->
						<div class="flex items-center justify-between mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-blue-500/15 border border-blue-500/40 text-blue-300 flex items-center justify-center text-2xl shadow-[0_0_16px_rgba(59,130,246,0.2)]"
							>
								💻
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-blue-500/10 text-blue-300 font-bold text-sm font-mono tracking-wider border border-blue-500/30"
							>
								SELF-TAUGHT
							</span>
						</div>

						<h3 class="text-xl sm:text-2xl font-extrabold text-white mb-4 tracking-tight">自學與 AI 協作開發</h3>

						<!-- 適合對象 -->
						<div class="mb-5 p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90">
							<div class="text-base font-bold text-blue-400 tracking-wide mb-2">適合對象</div>
							<ul class="space-y-1.5 text-base text-slate-300">
								<li class="flex items-start space-x-2">
									<span class="text-blue-400 mt-0.5">•</span>
									<span>自我約束與執行力極高</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-blue-400 mt-0.5">•</span>
									<span>已經清楚知道自己要學什麼</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-blue-400 mt-0.5">•</span>
									<span>善於自行搜尋資料與拆解問題</span>
								</li>
							</ul>
						</div>

						<!-- 核心優勢 -->
						<div class="mb-5 space-y-2">
							<div class="text-base font-bold text-emerald-400 tracking-wide">核心優點</div>
							<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify">
								時間彈性最高、經濟成本極低，可以完全依照自己的節奏前進，自由探索感興趣的技術。
							</p>
						</div>

						<!-- 需要面對 -->
						<div class="space-y-2">
							<div class="text-base font-bold text-amber-400 tracking-wide">需要面對的代價</div>
							<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
								沒有專人協助規劃完整學習路徑，遇到深層報錯或觀念盲點時需獨自苦思，容易學了很多破碎的知識點，卻難以產出架構完整且具競爭力的代表專題。
							</p>
						</div>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>路徑屬性</span>
						<span class="text-blue-400 font-bold">高自由度 · 需極高自律</span>
					</div>
				</div>

				<!-- 路徑 2：實體職訓 (高光焦點，cyan 主題) -->
				<div
					class="path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-gradient-to-b from-slate-900/95 via-slate-900/90 to-slate-950/95 backdrop-blur-xl border border-cyan-500/50 shadow-2xl shadow-cyan-950/50 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[86vw] max-w-[360px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<!-- 標題與圖標 -->
						<div class="flex items-center justify-between mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-cyan-500/20 border border-cyan-400/50 text-cyan-300 flex items-center justify-center text-2xl shadow-[0_0_20px_rgba(6,182,212,0.3)]"
							>
								🏫
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-cyan-500/20 text-cyan-300 font-bold text-sm font-mono tracking-wider border border-cyan-400/40"
							>
								RECOMMENDED PATH
							</span>
						</div>

						<h3 class="text-xl sm:text-2xl font-extrabold text-white mb-4 tracking-tight">全日制實體職訓</h3>

						<!-- 適合對象 -->
						<div class="mb-5 p-4 rounded-2xl bg-slate-950/90 border border-cyan-500/30">
							<div class="text-base font-bold text-cyan-400 tracking-wide mb-2">適合對象</div>
							<ul class="space-y-1.5 text-base text-slate-200">
								<li class="flex items-start space-x-2">
									<span class="text-cyan-400 mt-0.5">•</span>
									<span>希望有完整、有階梯的學習路徑</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-cyan-400 mt-0.5">•</span>
									<span>遇到卡關時需要老師即時釐清問題</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-cyan-400 mt-0.5">•</span>
									<span>希望全職集中時間，大量實作演練</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-cyan-400 mt-0.5">•</span>
									<span>想和一群志同道合的同儕並肩學習</span>
								</li>
							</ul>
						</div>

						<!-- 核心優勢 -->
						<div class="mb-5 space-y-2">
							<div class="text-base font-bold text-emerald-400 tracking-wide">核心優點</div>
							<p class="text-base text-slate-100 leading-relaxed text-pretty text-justify">
								勞動部自辦 <span class="inline-block">920 小時</span>系統化培訓，專屬<span class="inline-block"
									>雙螢幕實作教學</span
								>，每天高強度沉浸式編程，有專任老師與同學現場即時討論，確保每一位學員都能獨立產出完整<span
									class="inline-block"
									>專案作品集</span
								>。
							</p>
						</div>

						<!-- 需要面對 -->
						<div class="space-y-2">
							<div class="text-base font-bold text-amber-400 tracking-wide">需要面對的代價</div>
							<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
								需要全職投入整整半年的專注時間，需要跟上密集緊湊的課程進度與實作要求，這絕不是一條輕鬆速成的捷徑。
							</p>
						</div>
					</div>

					<div
						class="pt-5 mt-6 border-t border-cyan-500/30 flex items-center justify-between text-sm text-slate-200 font-mono"
					>
						<span>路徑屬性</span>
						<span class="text-cyan-300 font-bold">系統沉浸 · 充實紮實</span>
					</div>
				</div>

				<!-- 路徑 3：工作中學習 -->
				<div
					class="path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default hover:border-purple-500/50 transition-[border-color,box-shadow] duration-300 w-[86vw] max-w-[360px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<!-- 標題與圖標 -->
						<div class="flex items-center justify-between mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-purple-500/15 border border-purple-500/40 text-purple-300 flex items-center justify-center text-2xl shadow-[0_0_16px_rgba(168,85,247,0.2)]"
							>
								💼
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-purple-500/10 text-purple-300 font-bold text-sm font-mono tracking-wider border border-purple-500/30"
							>
								ON-THE-JOB
							</span>
						</div>

						<h3 class="text-xl sm:text-2xl font-extrabold text-white mb-4 tracking-tight">在工作中邊做邊學</h3>

						<!-- 適合對象 -->
						<div class="mb-5 p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90">
							<div class="text-base font-bold text-purple-400 tracking-wide mb-2">適合對象</div>
							<ul class="space-y-1.5 text-base text-slate-300">
								<li class="flex items-start space-x-2">
									<span class="text-purple-400 mt-0.5">•</span>
									<span>已經具備一定資訊或程式基礎</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-purple-400 mt-0.5">•</span>
									<span>身處相關領域，有機會接觸實際專案</span>
								</li>
								<li class="flex items-start space-x-2">
									<span class="text-purple-400 mt-0.5">•</span>
									<span>能從實際業務問題中自主學習反思</span>
								</li>
							</ul>
						</div>

						<!-- 核心優勢 -->
						<div class="mb-5 space-y-2">
							<div class="text-base font-bold text-emerald-400 tracking-wide">核心優點</div>
							<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify">
								身處最真實的商業開發情境，直接面對市場需求，累積具備即戰力的一手實務經驗。
							</p>
						</div>

						<!-- 需要面對 -->
						<div class="space-y-2">
							<div class="text-base font-bold text-amber-400 tracking-wide">需要面對的代價</div>
							<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
								對完全零基礎的轉職者門檻極高；日常工作的交付壓力與時程緊迫，可能大幅壓縮你從容打好底層基礎的學習時間。
							</p>
						</div>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>路徑屬性</span>
						<span class="text-purple-400 font-bold">實務連結 · 需既有門檻</span>
					</div>
				</div>
			</div>

			<!-- 誠懇決策收束橫幅 (三行層次結構) -->
			<div class="mt-14 max-w-5xl xl:max-w-6xl mx-auto text-center">
				<div class="p-5 sm:p-8 rounded-3xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md shadow-xl">
					<!-- 第 1 行：核心精神 -->
					<h4 class="text-xl sm:text-2xl font-extrabold text-white mb-3 tracking-tight text-balance">
						沒有哪一種方式一定最好
					</h4>

					<!-- 第 2 行：客觀對比 -->
					<p
						class="text-base sm:text-lg text-slate-300 leading-relaxed text-justify sm:text-center xl:whitespace-nowrap"
					>
						如果你已經知道自己要什麼，自學可能就足夠；如果你需要一個完整環境、老師、同儕與大量實作，職訓可能更適合。
					</p>

					<!-- 第 3 行：自主決定金句 -->
					<p class="mt-2.5 text-base sm:text-lg font-bold text-cyan-300 leading-relaxed xl:whitespace-nowrap">
						先理解自己的真實需要，再決定要走哪一條路。
					</p>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'

// 3 大學習路徑對比卡片統一由通用 Composable 調度
useScrollStagger('#path-comparison-grid .path-card', '#path-comparison', {
	yOffset: 28,
	duration: 0.85,
	stagger: 0.08,
	ease: 'power1.out',
	start: 'top 85%',
})
</script>
