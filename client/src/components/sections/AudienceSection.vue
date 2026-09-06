<template>
	<section
		id="audience-resonance"
		class="py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden"
	>
		<!-- 背景流光點綴 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 受眾心聲共鳴標頭 -->
			<div class="text-center max-w-5xl xl:max-w-6xl mx-auto mb-6 sm:mb-12 lg:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Facing Reality ｜ 面對問題</span>
				</div>
				<h2 class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-black text-white tracking-tight leading-tight lg:whitespace-nowrap text-balance">
					<span class="block sm:inline">你正在面對的，</span><span
						class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400 block sm:inline"
						>也許不只是「要不要學程式」</span
					>
				</h2>
				<p class="text-slate-400 mt-4 text-base sm:text-lg max-w-none mx-auto leading-relaxed text-pretty text-justify sm:text-center xl:whitespace-nowrap">
					踏入陌生的科技領域，害怕跟不上、害怕選錯方向，其實很正常。這些確實是現在許多轉職者正在面對的真實問題。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div class="flex md:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4">
				<span>👈 左右滑動瀏覽 3 大轉職困惑 👉</span>
			</div>

			<!-- 三大對話式反思卡片 (手機露邊橫向滑軌，桌機 md: 3 欄) -->
			<div
				id="resonance-cards-grid"
				class="flex md:grid md:grid-cols-3 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 md:mx-0 md:px-0 gap-4 sm:gap-6 pb-4 md:pb-0"
			>
				<!-- 卡片 1 -->
				<div
					class="resonance-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden hover:border-cyan-500/50 transition-[border-color,box-shadow] duration-300 cursor-default w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start md:shrink"
				>
					<div>
						<!-- 提問者標籤 -->
						<div class="flex items-center space-x-3 mb-3 sm:mb-4">
							<div
								class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-cyan-500/15 border border-cyan-500/40 text-cyan-300 flex items-center justify-center text-lg sm:text-xl shadow-[0_0_16px_rgba(6,182,212,0.2)] flex-shrink-0"
							>
								❓
							</div>
							<div class="text-xs sm:text-sm font-mono font-bold text-cyan-400 uppercase tracking-wider">
								COMMON DOUBT 01
							</div>
						</div>
						<h3
							class="text-lg xl:text-xl font-extrabold text-white mb-2.5 sm:mb-3 tracking-tight 2xl:whitespace-nowrap"
						>
							完全沒寫過程式，我真的學得會嗎？
						</h3>
						<!-- 手機端隱藏引言框 -->
						<div
							class="hidden sm:block p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90 mb-4 text-base text-slate-300 font-normal leading-relaxed text-justify"
						>
							“看著滿螢幕的英文程式碼，總覺得是離自己非常遙遠的世界……”
						</div>
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify">
							<!-- 手機端穿透金句 -->
							<span class="sm:hidden block">
								從最基礎排版教起、每日動手實作，重點在於願不願意花時間把不會變成會。
							</span>
							<!-- 桌機端完整論述 -->
							<span class="hidden sm:inline">
								學習程式不需要一開始就懂所有事情。課程從網頁最基礎的結構與排版教起，親手看見每一行程式碼如何產生變化，循序建立扎實手感。<br />
								<span class="text-cyan-300 font-bold mt-2.5 block text-base sm:text-lg">
									真正需要確認的，不是「我現在會不會」，而是「我願不願意花時間，把不會變成會」。
								</span>
							</span>
						</p>
					</div>
					<div
						class="pt-3.5 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-xs sm:text-sm text-slate-300 font-mono"
					>
						<span>學習心態</span>
						<span class="text-cyan-400 font-bold"> 時間投入 · 循序打底 </span>
					</div>
				</div>

				<!-- 卡片 2 -->
				<div
					class="resonance-card card-subsurface-blue relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start md:shrink"
				>
					<div>
						<div class="flex items-center space-x-3 mb-3 sm:mb-4">
							<div
								class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-blue-500/15 border border-blue-500/40 text-blue-300 flex items-center justify-center text-lg sm:text-xl shadow-[0_0_16px_rgba(59,130,246,0.2)] flex-shrink-0"
							>
								🤖
							</div>
							<div class="text-xs sm:text-sm font-mono font-bold text-blue-400 uppercase tracking-wider">
								COMMON DOUBT 02
							</div>
						</div>
						<h3
							class="text-lg xl:text-xl font-extrabold text-white mb-2.5 sm:mb-3 tracking-tight 2xl:whitespace-nowrap"
						>
							現在才學寫程式，會不會馬上被 AI 取代？
						</h3>
						<!-- 手機端隱藏引言框 -->
						<div
							class="hidden sm:block p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90 mb-4 text-base text-slate-300 font-normal leading-relaxed text-justify"
						>
							“新聞天天都在報 AI 能一秒寫出網頁，現在投入還有競爭力嗎……”
						</div>
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify">
							<!-- 手機端穿透金句 -->
							<span class="sm:hidden block">
								AI 讓生成變容易，但架構思維、獨立除錯與系統判斷力更加關鍵。
							</span>
							<!-- 桌機端完整論述 -->
							<span class="hidden sm:inline">
								AI 讓產生程式碼變得容易，但同時也讓架構思維、判斷合理性、除錯與整體系統能力變得更加重要。課程不只教「怎麼寫」，而是教你「理解自己正在做什麼」，讓 AI 成為最強協同副駕駛。<br />
								<span class="text-blue-300 font-bold mt-2.5 block text-base sm:text-lg">
									AI 讓生成變容易，但讓理解、判斷與架構能力更加關鍵。
								</span>
							</span>
						</p>
					</div>
					<div
						class="pt-3.5 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-xs sm:text-sm text-slate-300 font-mono"
					>
						<span>未來趨勢</span>
						<span class="text-blue-400 font-bold"> 人機協作 · 核心理解 </span>
					</div>
				</div>

				<!-- 卡片 3 -->
				<div
					class="resonance-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start md:shrink"
				>
					<div>
						<div class="flex items-center space-x-3 mb-3 sm:mb-4">
							<div
								class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-purple-500/15 border border-purple-500/40 text-purple-300 flex items-center justify-center text-lg sm:text-xl shadow-[0_0_16px_rgba(168,85,247,0.2)] flex-shrink-0"
							>
								🏫
							</div>
							<div class="text-xs sm:text-sm font-mono font-bold text-purple-400 uppercase tracking-wider">
								COMMON DOUBT 03
							</div>
						</div>
						<h3
							class="text-lg xl:text-xl font-extrabold text-white mb-2.5 sm:mb-3 tracking-tight 2xl:whitespace-nowrap"
						>
							自學資源這麼多，為什麼需要來職訓？
						</h3>
						<!-- 手機端隱藏引言框 -->
						<div
							class="hidden sm:block p-4 rounded-2xl bg-slate-950/70 border border-slate-800/90 mb-4 text-base text-slate-300 font-normal leading-relaxed text-justify"
						>
							“看線上教學好像都懂，自己開編輯器卻一行都寫不出來……”
						</div>
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify">
							<!-- 手機端穿透金句 -->
							<span class="sm:hidden block">
								你缺的不是更多免費教材，而是卡關有人即時討論的實體環境。
							</span>
							<!-- 桌機端完整論述 -->
							<span class="hidden sm:inline">
								網路上有成千上萬的免費教學與影音。真正值得思考的是：你現在缺的到底是一套新教材，還是缺一個能讓你排除干擾、遇到卡關有人即時討論、並能持續走完半年的實體環境？<br />
								<span class="text-purple-300 font-bold mt-2.5 block text-base sm:text-lg">
									你缺的是更多教材，還是一個能讓你持續走下去的學習環境？
								</span>
							</span>
						</p>
					</div>
					<div
						class="pt-3.5 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-xs sm:text-sm text-slate-300 font-mono"
					>
						<span>實體價值</span>
						<span class="text-purple-400 font-bold"> 專注環境 · 即時討論 </span>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'

// 3 大內在共鳴卡片統一由通用 Composable 調度
useScrollStagger(
	'#resonance-cards-grid .resonance-card',
	'#resonance-cards-grid',
	{
		yOffset: 28,
		duration: 0.85,
		stagger: 0.08,
		ease: 'power1.out',
		start: 'top 85%',
	}
)
</script>
