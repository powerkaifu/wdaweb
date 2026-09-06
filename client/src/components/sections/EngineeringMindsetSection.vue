<template>
	<section id="engineering-mindset" class="py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden">
		<!-- 背景微光 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-indigo-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 大區塊標題區 (標準一級 Section 規格) -->
			<div class="text-center max-w-5xl mx-auto mb-6 sm:mb-12 lg:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Engineering Mindset ｜ 工程思維核心</span>
				</div>
				<h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight text-balance">
					<span class="block">在 AI 時代，</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-300"
						>我們培養的是能完成產品的人</span
					>
				</h2>
				<p
					class="text-slate-400 mt-4 text-base sm:text-lg max-w-4xl xl:max-w-5xl mx-auto leading-relaxed text-pretty text-justify sm:text-center"
				>
					AI 能在幾秒內生成程式碼，卻無法替你定義需求、拆解架構與確保品質。我們更重視的，是培養理解需求、拆解模組、AI 協作、驗證除錯、系統整合的完整工程能力。
				</p>
			</div>

			<!-- 旗艦工程思維展台卡片 -->
			<div
				class="relative rounded-3xl p-6 sm:p-8 lg:p-10 bg-gradient-to-br from-slate-900/95 via-slate-900/85 to-slate-950/95 border border-cyan-500/30 hover:border-cyan-500/50 transition-all duration-300 backdrop-blur-xl shadow-2xl shadow-slate-950/70 overflow-hidden group"
			>
				<!-- 頂部高光流線 -->
				<div
					class="absolute top-0 inset-x-0 h-[2px] bg-gradient-to-r from-transparent via-cyan-400/50 to-transparent opacity-70 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
				></div>

				<!-- 背景科技光暈微光 -->
				<div
					class="absolute -top-24 -right-24 w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"
				></div>
				<div
					class="absolute -bottom-24 -left-24 w-80 h-80 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"
				></div>

				<div class="relative z-10 space-y-6">
					<!-- ========================================================================= -->
					<!-- 工程思維核心理念看板 (跨裝置自適應資訊量分流：手機2x2 / 平板雙欄 / 筆電橫向管線 / 桌機旗艦展台) -->
					<!-- ========================================================================= -->

					<!-- 1. 📱 手機端 (sm:hidden)：極致精煉，零長列表，5大心智微膠囊，高度僅約 120px -->
					<div class="sm:hidden p-4 rounded-2xl bg-slate-950/80 border border-cyan-500/30 shadow-lg space-y-2.5">
						<div class="space-y-1.5">
							<div class="flex items-center space-x-2 text-rose-300 font-semibold text-sm">
								<span
									class="w-5 h-5 rounded-full bg-rose-500/15 border border-rose-500/30 flex items-center justify-center text-xs flex-shrink-0"
									>✕</span
								>
								<span>不是培養「只會等 AI 幫忙寫」的人</span>
							</div>
							<div class="flex items-center space-x-2 text-cyan-300 font-extrabold text-base">
								<span
									class="w-5 h-5 rounded-full bg-cyan-500/20 border border-cyan-400/40 flex items-center justify-center text-xs text-cyan-300 flex-shrink-0"
									>✓</span
								>
								<span>而是培養「能真正完成產品」的人</span>
							</div>
						</div>
						<!-- 5 步心智緊湊流 -->
						<div class="pt-2 border-t border-slate-800/80 space-y-1.5">
							<div class="grid grid-cols-2 gap-1.5 text-xs font-mono font-bold">
								<div class="p-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">① 理解 ➔</span> 需求到底是什麼？
								</div>
								<div class="p-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">② 拆解 ➔</span> 這個問題怎麼拆？
								</div>
								<div class="p-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">③ 協作 ➔</span> 如何讓 AI 幫我加速？
								</div>
								<div class="p-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">④ 驗證 ➔</span> AI 做的是對的嗎？
								</div>
							</div>
							<div
								class="p-2 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-xs font-bold text-emerald-300 text-center shadow-sm"
							>
								⑤ 整合 ➔ 如何讓所有東西真正運作並交付產品？
							</div>
						</div>
					</div>

					<!-- 2. 📟 平板端 (hidden sm:block lg:hidden)：雙欄對比，留白舒適 -->
					<div class="hidden sm:block lg:hidden p-5 rounded-3xl bg-slate-950/80 border border-cyan-500/30 shadow-xl">
						<div class="grid grid-cols-2 gap-5 items-stretch">
							<div
								class="space-y-2.5 p-4 rounded-2xl bg-slate-900/70 border border-slate-800/80 flex flex-col justify-between"
							>
								<div>
									<div class="inline-flex items-center space-x-1.5 text-xs font-bold text-rose-400 font-mono mb-1">
										<span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
										<span>WE DO NOT TRAIN</span>
									</div>
									<h4 class="text-base font-extrabold text-white">
										不是培養：<br /><span class="text-rose-300">只會等 AI 幫我寫程式的人</span>
									</h4>
									<p class="text-xs text-slate-400 leading-relaxed mt-2">
										看不懂底層邏輯、出 Bug 只能反覆追問、無法把片段組合成真實系統。
									</p>
								</div>
								<div class="text-xs text-slate-300 pt-2 border-t border-slate-800/80 font-medium">
									⚠️ 缺乏自主除錯與整合力最先被淘汰
								</div>
							</div>

							<div
								class="space-y-2.5 p-4 rounded-2xl bg-cyan-950/20 border border-cyan-500/30 flex flex-col justify-between"
							>
								<div>
									<div class="inline-flex items-center space-x-1.5 text-xs font-bold text-cyan-400 font-mono mb-1">
										<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
										<span>5-STAGE ENGINEERING MINDSET</span>
									</div>
									<h4 class="text-base font-extrabold text-cyan-300">而是培養：能完成產品的人</h4>
									<div class="space-y-1.5 text-xs font-semibold text-slate-200 mt-2">
										<div
											class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80 flex items-center justify-between"
										>
											<span>① 理解</span><span class="text-slate-300 font-normal">需求到底是什麼？</span>
										</div>
										<div
											class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80 flex items-center justify-between"
										>
											<span>② 拆解</span><span class="text-slate-300 font-normal">這個問題怎麼拆？</span>
										</div>
										<div
											class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80 flex items-center justify-between"
										>
											<span>③ 協作</span><span class="text-slate-300 font-normal">如何讓 AI 幫我加速？</span>
										</div>
										<div
											class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80 flex items-center justify-between"
										>
											<span>④ 驗證</span><span class="text-slate-300 font-normal">AI 做的是對的嗎？(改/Debug)</span>
										</div>
									</div>
								</div>
								<div
									class="text-xs font-bold text-emerald-300 text-center bg-emerald-950/50 p-2 rounded-xl border border-emerald-500/40"
								>
									⑤ 整合 ➔ 讓所有東西真正運作，完成產品！
								</div>
							</div>
						</div>
					</div>

					<!-- 3. 💻 筆電端 (hidden lg:block xl:hidden)：橫向 5 步水平流水線，矮螢幕一覽無遺 -->
					<div
						class="hidden lg:block xl:hidden p-4 rounded-3xl bg-slate-950/80 border border-cyan-500/30 shadow-xl space-y-3"
					>
						<div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
							<div class="flex items-center space-x-2">
								<span
									class="px-2.5 py-0.5 rounded-full bg-rose-500/15 text-rose-300 border border-rose-500/30 text-xs font-bold font-mono"
									>不是培養</span
								>
								<span class="text-sm font-bold text-slate-300">只會等 AI 幫我寫程式的人</span>
							</div>
							<span class="text-xs font-mono text-cyan-400/80 font-bold">➔ 5 階段工程思維躍遷 ➔</span>
							<div class="flex items-center space-x-2">
								<span
									class="px-2.5 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-xs font-bold font-mono"
									>而是培養</span
								>
								<span class="text-sm font-extrabold text-white">能完成產品的現代工程師</span>
							</div>
						</div>
						<div class="grid grid-cols-5 gap-2 items-stretch text-center">
							<div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
								<div class="text-xs text-cyan-400 font-mono font-bold">① 理解</div>
								<div class="text-xs font-extrabold text-white my-1">需求到底是什麼？</div>
								<span class="text-xs text-slate-300">需求本質定義</span>
							</div>
							<div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
								<div class="text-xs text-cyan-400 font-mono font-bold">② 拆解</div>
								<div class="text-xs font-extrabold text-white my-1">這個問題怎麼拆？</div>
								<span class="text-xs text-slate-300">架構模組拆解</span>
							</div>
							<div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
								<div class="text-xs text-cyan-400 font-mono font-bold">③ 協作</div>
								<div class="text-xs font-extrabold text-white my-1">如何讓 AI 加速？</div>
								<span class="text-xs text-slate-300">精準提示協同</span>
							</div>
							<div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
								<div class="text-xs text-cyan-400 font-mono font-bold">④ 驗證</div>
								<div class="text-xs font-extrabold text-white my-1">AI 做的是對的嗎？</div>
								<span class="text-xs text-slate-300">修改與 Debug</span>
							</div>
							<div
								class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex flex-col justify-between shadow-sm shadow-emerald-500/20"
							>
								<div class="text-xs text-emerald-400 font-mono font-bold">⑤ 整合 🎯</div>
								<div class="text-xs font-black text-emerald-300 my-1">如何真正運作？</div>
								<span class="text-xs text-emerald-400 font-bold">完成商業產品</span>
							</div>
						</div>
					</div>

					<!-- 4. 🖥️ 桌機端 (hidden xl:block)：旗艦科技對照展台，次表面微光大器展開 -->
					<div class="hidden xl:block p-6 rounded-3xl bg-slate-950/85 border border-cyan-500/30 shadow-2xl">
						<div class="grid grid-cols-12 gap-6 items-stretch">
							<!-- 左側 4 欄：反思與警惕展台 -->
							<div
								class="col-span-4 p-5 rounded-2xl bg-slate-900/70 border border-slate-800/90 flex flex-col justify-between"
							>
								<div class="space-y-3">
									<div
										class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-rose-500/10 text-rose-300 border border-rose-500/30 text-xs font-bold font-mono"
									>
										<span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
										<span>WE DO NOT TRAIN</span>
									</div>
									<h4 class="text-xl font-extrabold text-white leading-snug">
										不是培養：<br />
										<span class="text-rose-300">「只會等 AI 幫我寫程式的人」</span>
									</h4>
									<ul class="space-y-2 text-sm text-slate-300">
										<li class="flex items-start space-x-2">
											<span class="text-rose-400 mt-0.5">✕</span>
											<span>看不懂 AI 產生的底層代碼邏輯</span>
										</li>
										<li class="flex items-start space-x-2">
											<span class="text-rose-400 mt-0.5">✕</span>
											<span>一遇報錯就反覆提問、陷入死循環</span>
										</li>
										<li class="flex items-start space-x-2">
											<span class="text-rose-400 mt-0.5">✕</span>
											<span>只能拼湊玩具，無法交付商業產品</span>
										</li>
									</ul>
								</div>
								<div class="text-xs text-slate-300 pt-3 border-t border-slate-800 font-medium">
									⚠️ 缺乏自主除錯與系統整合能力的求職者，最先被技術浪潮淘汰
								</div>
							</div>

							<!-- 右側 8 欄：5 階段心智自問工程管線 (5-Stage Mental Pipeline) -->
							<div
								class="col-span-8 p-5 rounded-2xl bg-cyan-950/20 border border-cyan-500/30 flex flex-col justify-between"
							>
								<div class="flex items-center justify-between mb-3">
									<div
										class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-xs font-bold font-mono"
									>
										<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
										<span>5-STAGE ENGINEERING MINDSET</span>
									</div>
									<span class="text-sm font-extrabold text-cyan-300">我們真正培養的 5 大核心工程心智</span>
								</div>

								<div class="grid grid-cols-5 gap-2.5 items-stretch text-center">
									<div
										class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors"
									>
										<span class="text-xs text-cyan-400 font-mono font-bold">① 理解</span>
										<div class="text-sm font-extrabold text-white my-2">需求到底是什麼？</div>
										<span class="text-xs text-slate-300">需求定義</span>
									</div>
									<div
										class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors"
									>
										<span class="text-xs text-cyan-400 font-mono font-bold">② 拆解</span>
										<div class="text-sm font-extrabold text-white my-2">這個問題怎麼拆？</div>
										<span class="text-xs text-slate-300">架構拆解</span>
									</div>
									<div
										class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors"
									>
										<span class="text-xs text-cyan-400 font-mono font-bold">③ 協作</span>
										<div class="text-sm font-extrabold text-white my-2">如何讓 AI 幫我加速？</div>
										<span class="text-xs text-slate-300">精準協同</span>
									</div>
									<div
										class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors"
									>
										<span class="text-xs text-cyan-400 font-mono font-bold">④ 驗證</span>
										<div class="text-sm font-extrabold text-white my-2">AI 做的是對的嗎？</div>
										<span class="text-xs text-slate-300">修改與 Debug</span>
									</div>
									<div
										class="p-3 rounded-xl bg-gradient-to-b from-emerald-950/60 to-slate-900 border border-emerald-500/50 flex flex-col justify-between shadow-lg shadow-emerald-950/40"
									>
										<span class="text-xs text-emerald-400 font-mono font-bold">⑤ 整合 🎯</span>
										<div class="text-sm font-black text-emerald-300 my-2">如何讓所有東西真正運作？</div>
										<span class="text-xs text-emerald-400 font-bold">完成產品的人</span>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- 底部心智理念收束引言 -->
					<div
						class="pt-4 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-sm sm:text-base font-mono"
					>
						<span class="text-slate-400">💡 核心理念：AI 決定開發速度，而你的工程思維決定產品上限</span>
						<span class="text-cyan-400 font-bold">🎯 培養獨立解決問題與系統交付的能力</span>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
// 純展示型工程心智核心大區塊，已內建四裝置精緻自適應
</script>
