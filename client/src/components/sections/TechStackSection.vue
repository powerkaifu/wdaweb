<template>
	<section
		id="tech-stack"
		:class="[
			hideHeader
				? 'py-6 sm:py-10 bg-transparent relative'
				: 'py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden',
		]"
	>
		<!-- 背景光暈 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊標題 (僅在未隱藏標頭時渲染) -->
			<div v-if="!hideHeader" class="text-center max-w-4xl mx-auto mb-6 sm:mb-12 lg:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Development Tools ｜ 技術與工具</span>
				</div>
				<h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight text-balance">
					你會接觸到哪些技術？
				</h2>
				<p
					class="text-slate-400 mt-4 text-base sm:text-lg max-w-4xl xl:max-w-5xl mx-auto leading-relaxed text-pretty text-justify sm:text-center"
				>
					技術不是一串需要背下來的英文單字。它們不是需要背下來的名詞，而是你完成作品時會真正用到的工具。你會依照學習階段，逐步接觸不同領域的技術。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div
				v-if="!hideHeader"
				class="flex sm:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-2 mb-4"
			>
				<span>👈 左右滑動瀏覽 8 大核心技術 👉</span>
			</div>

			<!-- 1. 8 大核心技術卡片網格 (手機橫向滑軌，桌機 xl: 4 欄) -->
			<div
				id="tech-cards-grid"
				class="flex sm:grid sm:grid-cols-2 xl:grid-cols-4 overflow-x-auto sm:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 sm:mx-0 sm:px-0 gap-4 sm:gap-6 pb-4 sm:pb-0 mb-8"
			>
				<div
					v-for="(card, index) in store.techCards"
					:key="card.id"
					class="tech-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
				>
					<!-- 角落序號水印 (01~08) -->
					<div
						class="absolute -right-2 -bottom-4 text-6xl sm:text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						{{ String(index + 1).padStart(2, '0') }}
					</div>

					<div>
						<div class="flex items-center justify-between mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-slate-800 border border-slate-700/80 flex items-center justify-center text-2xl shadow-inner"
							>
								{{ getTechIcon(card.tech_name) }}
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-cyan-500/10 text-cyan-300 font-bold text-sm border border-cyan-500/30 tracking-wide"
							>
								{{ card.category_tab || '核心必修' }}
							</span>
						</div>

						<h3 class="text-xl font-extrabold text-white mb-2.5 tracking-tight">
							{{ card.tech_name }}
						</h3>

						<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
							{{ card.description }}
						</p>
					</div>

					<div
						class="pt-5 mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-slate-300 font-mono"
					>
						<span>核心能力</span>
						<span class="text-cyan-400 font-bold">專題實作</span>
					</div>
				</div>
			</div>

			<!-- 2. AI 輔助應用旗艦橫幅 (橫跨四欄寬度，滿幅對齊上方 8 大技術卡片網格，內含 3 大精緻場景卡片) -->
			<div class="mt-8 sm:mt-14 lg:mt-16 w-full">
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
						class="absolute -bottom-24 -left-24 w-80 h-80 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"
					></div>

					<div class="relative z-10 space-y-6">
						<!-- 頂部標籤與標題列 -->
						<div
							class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-5"
						>
							<div class="space-y-2">
								<div
									class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 text-xs font-bold font-mono tracking-wider"
								>
									<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
									<span>AI-ASSISTED DEVELOPMENT ｜ 現代人機協同</span>
								</div>
								<h3
									class="text-2xl sm:text-2xl lg:text-3xl font-extrabold text-white tracking-tight flex items-center gap-2.5 text-balance"
								>
									<span class="text-2xl sm:text-3xl flex-shrink-0">🤖</span>
									<span class="leading-snug"
										>AI 輔助應用：<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400"
											>讓 AI 成為你的專業開發副駕駛</span
										></span
									>
								</h3>
							</div>
						</div>

						<!-- 說明前導段落 (手機短金句 / 桌機完整論述) -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							寫程式不再死記語法。學會將生成式 AI 融入日常，把注意力集中在架構設計與真實體驗。
						</p>
						<p class="hidden sm:block text-base sm:text-lg text-slate-200 leading-relaxed text-pretty text-justify">
							寫程式不再是枯燥死記每一行語法。在課程中，你將學會如何將現代生成式 AI 工具融入日常開發流程。AI
							不是取代思考的捷徑，而是讓你能把寶貴注意力集中在「邏輯設計、架構規劃與使用者體驗」的強大助手。
						</p>

						<!-- ========================================================================= -->
						<!-- 工程思維核心理念看板 (跨裝置自適應資訊量分流：手機2x2 / 平板雙欄 / 筆電橫向管線 / 桌機旗艦展台) -->
						<!-- ========================================================================= -->

						<!-- 1. 📱 手機端 (sm:hidden)：極致精煉，零長列表，高度僅約 110px，杜絕滑動疲勞 -->
						<div class="sm:hidden p-4 rounded-2xl bg-slate-950/80 border border-cyan-500/30 shadow-lg space-y-2.5 my-2">
							<div class="space-y-1.5">
								<div class="flex items-center space-x-2 text-rose-300 font-semibold text-sm">
									<span class="w-5 h-5 rounded-full bg-rose-500/15 border border-rose-500/30 flex items-center justify-center text-xs flex-shrink-0">✕</span>
									<span>不是培養「只會等 AI 幫忙寫」的人</span>
								</div>
								<div class="flex items-center space-x-2 text-cyan-300 font-extrabold text-base">
									<span class="w-5 h-5 rounded-full bg-cyan-500/20 border border-cyan-400/40 flex items-center justify-center text-xs text-cyan-300 flex-shrink-0">✓</span>
									<span>而是培養「能完成產品」的工程師</span>
								</div>
							</div>
							<div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800/80 text-xs font-mono font-bold">
								<div class="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">1.</span>
									<span>🎯 需求拆解</span>
								</div>
								<div class="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">2.</span>
									<span>👁️ 判斷對錯</span>
								</div>
								<div class="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-200">
									<span class="text-cyan-400">3.</span>
									<span>🐞 獨立Debug</span>
								</div>
								<div class="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-xl bg-slate-900 border border-emerald-500/40 text-emerald-300">
									<span class="text-emerald-400">4.</span>
									<span>🚀 整合交付</span>
								</div>
							</div>
						</div>

						<!-- 2. 📟 平板端 (hidden sm:block lg:hidden)：雙欄對比，留白舒適 -->
						<div class="hidden sm:block lg:hidden p-5 rounded-3xl bg-slate-950/80 border border-cyan-500/30 shadow-xl my-3">
							<div class="grid grid-cols-2 gap-5 items-stretch">
								<div class="space-y-2.5 p-4 rounded-2xl bg-slate-900/70 border border-slate-800/80 flex flex-col justify-between">
									<div>
										<div class="inline-flex items-center space-x-1.5 text-xs font-bold text-rose-400 font-mono mb-1">
											<span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
											<span>WE DO NOT TRAIN</span>
										</div>
										<h4 class="text-base font-extrabold text-white">不是培養：<br /><span class="text-rose-300">只會等 AI 幫我寫程式的人</span></h4>
										<p class="text-xs text-slate-400 leading-relaxed mt-2">
											看不懂底層邏輯、出 Bug 只能反覆追問、無法把片段組合成真實系統。
										</p>
									</div>
									<div class="text-xs text-slate-300 pt-2 border-t border-slate-800/80 font-medium">
										⚠️ 缺乏自主除錯與整合力最先被淘汰
									</div>
								</div>

								<div class="space-y-2.5 p-4 rounded-2xl bg-cyan-950/20 border border-cyan-500/30 flex flex-col justify-between">
									<div>
										<div class="inline-flex items-center space-x-1.5 text-xs font-bold text-cyan-400 font-mono mb-1">
											<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
											<span>WE EMPOWER YOU</span>
										</div>
										<h4 class="text-base font-extrabold text-cyan-300">而是培養：能完成產品的人</h4>
										<div class="grid grid-cols-2 gap-1.5 text-xs font-semibold text-slate-200 mt-2">
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">🎯 知道做什麼</div>
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">🧩 知道怎麼拆</div>
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">👁️ 判斷對不對</div>
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">✏️ 能手動修改</div>
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">🐞 能自主Debug</div>
											<div class="p-1.5 rounded-lg bg-slate-900/90 border border-slate-800/80">🔌 能系統整合</div>
										</div>
									</div>
									<div class="text-xs font-bold text-emerald-300 text-center bg-emerald-950/50 p-2 rounded-xl border border-emerald-500/40">
										🚀 最終獨立完成商業級 Web 專案交付
									</div>
								</div>
							</div>
						</div>

						<!-- 3. 💻 筆電端 (hidden lg:block xl:hidden)：橫向 7 步水平流水線，零縱向浪費，矮螢幕一覽無遺 -->
						<div class="hidden lg:block xl:hidden p-4 rounded-3xl bg-slate-950/80 border border-cyan-500/30 shadow-xl space-y-3 my-3">
							<div class="flex items-center justify-between border-b border-slate-800/80 pb-2.5">
								<div class="flex items-center space-x-2">
									<span class="px-2.5 py-0.5 rounded-full bg-rose-500/15 text-rose-300 border border-rose-500/30 text-xs font-bold font-mono">不是培養</span>
									<span class="text-sm font-bold text-slate-300">只會等 AI 幫我寫程式的人</span>
								</div>
								<span class="text-xs font-mono text-cyan-400/80 font-bold">➔ 920H 完整工程思維養成 ➔</span>
								<div class="flex items-center space-x-2">
									<span class="px-2.5 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-xs font-bold font-mono">而是培養</span>
									<span class="text-sm font-extrabold text-white">能完成產品的現代工程師</span>
								</div>
							</div>
							<div class="grid grid-cols-7 gap-1.5 items-stretch text-center">
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">01</span>
									<div class="text-xs font-bold text-white my-1">知道做什麼</div>
									<span class="text-xs text-slate-300">需求定義</span>
								</div>
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">02</span>
									<div class="text-xs font-bold text-white my-1">知道怎麼拆</div>
									<span class="text-xs text-slate-300">架構拆解</span>
								</div>
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">03</span>
									<div class="text-xs font-bold text-white my-1">判斷對不對</div>
									<span class="text-xs text-slate-300">代碼審查</span>
								</div>
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">04</span>
									<div class="text-xs font-bold text-white my-1">能手動修改</div>
									<span class="text-xs text-slate-300">主導程式</span>
								</div>
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">05</span>
									<div class="text-xs font-bold text-white my-1">能深入Debug</div>
									<span class="text-xs text-slate-300">底層除錯</span>
								</div>
								<div class="p-2 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col justify-between">
									<span class="text-xs text-cyan-400 font-mono font-bold">06</span>
									<div class="text-xs font-bold text-white my-1">能系統整合</div>
									<span class="text-xs text-slate-300">前後端串接</span>
								</div>
								<div class="p-2 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex flex-col justify-between shadow-sm shadow-emerald-500/20">
									<span class="text-xs text-emerald-400 font-mono font-bold">Goal 🎯</span>
									<div class="text-xs font-black text-emerald-300 my-1">能完成產品</div>
									<span class="text-xs text-emerald-400 font-bold">獨立交付</span>
								</div>
							</div>
						</div>

						<!-- 4. 🖥️ 桌機端 (hidden xl:block)：旗艦科技對照展台，次表面微光大器展開 -->
						<div class="hidden xl:block p-6 rounded-3xl bg-slate-950/85 border border-cyan-500/30 shadow-2xl my-4">
							<div class="grid grid-cols-12 gap-6 items-stretch">
								<!-- 左側 4 欄：反思與警惕展台 -->
								<div class="col-span-4 p-5 rounded-2xl bg-slate-900/70 border border-slate-800/90 flex flex-col justify-between">
									<div class="space-y-3">
										<div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-rose-500/10 text-rose-300 border border-rose-500/30 text-xs font-bold font-mono">
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

								<!-- 右側 8 欄：7 步工程思維遞進鏈 (7-Step Engineering Pipeline) -->
								<div class="col-span-8 p-5 rounded-2xl bg-cyan-950/20 border border-cyan-500/30 flex flex-col justify-between">
									<div class="flex items-center justify-between mb-3">
										<div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-xs font-bold font-mono">
											<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
											<span>920H ENGINEERING MINDSET</span>
										</div>
										<span class="text-sm font-extrabold text-cyan-300">我們真正培養的 7 大工程能力鏈</span>
									</div>

									<div class="grid grid-cols-7 gap-2 items-stretch text-center">
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 1</span>
											<div class="text-sm font-extrabold text-white my-1.5">知道要做什麼</div>
											<span class="text-xs text-slate-300">需求定義</span>
										</div>
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 2</span>
											<div class="text-sm font-extrabold text-white my-1.5">知道怎麼拆問題</div>
											<span class="text-xs text-slate-300">架構拆解</span>
										</div>
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 3</span>
											<div class="text-sm font-extrabold text-white my-1.5">能判斷對不對</div>
											<span class="text-xs text-slate-300">代碼審查</span>
										</div>
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 4</span>
											<div class="text-sm font-extrabold text-white my-1.5">能自主修改</div>
											<span class="text-xs text-slate-300">主導程式</span>
										</div>
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 5</span>
											<div class="text-sm font-extrabold text-white my-1.5">能深入Debug</div>
											<span class="text-xs text-slate-300">底層除錯</span>
										</div>
										<div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800/90 flex flex-col justify-between hover:border-cyan-500/40 transition-colors">
											<span class="text-xs text-cyan-400 font-mono font-bold">Step 6</span>
											<div class="text-sm font-extrabold text-white my-1.5">能系統整合</div>
											<span class="text-xs text-slate-300">前後端串接</span>
										</div>
										<div class="p-3 rounded-xl bg-gradient-to-b from-emerald-950/60 to-slate-900 border border-emerald-500/50 flex flex-col justify-between shadow-lg shadow-emerald-950/40">
											<span class="text-xs text-emerald-400 font-mono font-bold">Goal 7 🎯</span>
											<div class="text-sm font-black text-emerald-300 my-1.5">能完成產品的人</div>
											<span class="text-xs text-emerald-400 font-bold">獨立商業交付</span>
										</div>
									</div>
								</div>
							</div>
						</div>

						<!-- 手機端橫向滑動提示 (桌機隱藏) -->
						<div class="flex md:hidden items-center justify-center gap-2 text-sm font-bold text-cyan-400 pt-1">
							<span>👈 左右滑動瀏覽 3 大 AI 協同場景 👉</span>
						</div>

						<!-- 3 大核心 AI 輔助應用卡片 (手機橫向滑軌避免堆疊 750px，桌機 3 欄並排大氣) -->
						<div
							class="flex md:grid md:grid-cols-3 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-2 px-2 md:mx-0 md:px-0 gap-3 sm:gap-5 pb-2 md:pb-0 pt-2"
						>
							<!-- 卡片 1 -->
							<div
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between w-[80vw] max-w-[290px] shrink-0 snap-start md:w-auto md:max-w-none md:shrink"
							>
								<div>
									<div class="text-2xl mb-2.5">💡</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">想法轉化為程式雛型</h4>
									<!-- 手機短金句 -->
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
										用精確 Prompt 讓 AI 快速生成版面與雛型，大幅縮短從零摸索的時間。
									</p>
									<!-- 桌機完整論述 -->
									<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
										學會用精確的 Prompt 描述需求，讓 AI 快速生成基礎頁面架構與樣式雛型，大幅縮短從零起步的摸索期。
									</p>
								</div>
								<div class="pt-3.5 mt-4 border-t border-slate-800/70 flex flex-wrap gap-2">
									<span
										class="px-3 py-1 rounded-lg bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-sm font-medium"
									>
										#加速起步
									</span>
									<span
										class="px-3 py-1 rounded-lg bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 text-sm font-medium"
									>
										#需求轉譯
									</span>
								</div>
							</div>

							<!-- 卡片 2 -->
							<div
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between w-[80vw] max-w-[290px] shrink-0 snap-start md:w-auto md:max-w-none md:shrink"
							>
								<div>
									<div class="text-2xl mb-2.5">🔍</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">報錯解讀與輔助除錯</h4>
									<!-- 手機短金句 -->
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
										看不懂報錯時請 AI 翻譯成白話、分析原因，提供多元解題思路。
									</p>
									<!-- 桌機完整論述 -->
									<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
										遇到看不懂的錯誤訊息時，學會請 AI 協助翻譯成人類白話，分析可能的報錯成因，提供多元解題思路。
									</p>
								</div>
								<div class="pt-3.5 mt-4 border-t border-slate-800/70 flex flex-wrap gap-2">
									<span
										class="px-3 py-1 rounded-lg bg-blue-500/15 text-blue-300 border border-blue-500/30 text-sm font-medium"
									>
										#白話報錯
									</span>
									<span
										class="px-3 py-1 rounded-lg bg-blue-500/15 text-blue-300 border border-blue-500/30 text-sm font-medium"
									>
										#快速定位
									</span>
								</div>
							</div>

							<!-- 卡片 3 -->
							<div
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between w-[80vw] max-w-[290px] shrink-0 snap-start md:w-auto md:max-w-none md:shrink"
							>
								<div>
									<div class="text-2xl mb-2.5">🛡️</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">批判審核與把關驗證</h4>
									<!-- 手機短金句 -->
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
										AI 也會犯錯。培養逐行審閱與除錯驗證能力，掌握專案最終主導權。
									</p>
									<!-- 桌機完整論述 -->
									<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
										AI 也會出錯。你將學會不盲信、不照抄，具備逐行審閱代碼、除錯與驗證的能力，牢牢掌握專案的最終主導權。
									</p>
								</div>
								<div class="pt-3.5 mt-4 border-t border-slate-800/70 flex flex-wrap gap-2">
									<span
										class="px-3 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 text-sm font-medium"
									>
										#主導權在人
									</span>
									<span
										class="px-3 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 text-sm font-medium"
									>
										#抗AI幻覺
									</span>
								</div>
							</div>
						</div>

						<!-- 底部核心共鳴收束引言 -->
						<div
							class="pt-4 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-sm sm:text-base font-mono"
						>
							<span class="text-slate-400">💡 核心工作流：人機協同 ➔ 提問 · 理解 · 驗證 · 修改</span>
							<span class="text-cyan-400 font-bold">✨ 培養與 AI 協同的工作習慣</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'
import { useCmsStore } from '@/stores/useCmsStore'

withDefaults(
	defineProps<{
		hideHeader?: boolean
	}>(),
	{
		hideHeader: false,
	},
)

const store = useCmsStore()

// 8 大技術棧卡片一氣呵成交錯波浪微升 (透過通用 Composable 統一調度生命週期與快取更新)
useScrollStagger(
	'#tech-cards-grid .tech-card',
	'#tech-stack',
	{
		yOffset: 28,
		duration: 0.85,
		stagger: 0.06,
		ease: 'power1.out',
		start: 'top 85%',
	},
	() => store.techCards.length,
)

function getTechIcon(name: string): string {
	if (name.includes('HTML') || name.includes('CSS')) return '🌐'
	if (name.includes('Tailwind') || name.includes('Bootstrap')) return '🎨'
	if (name.includes('Photoshop') || name.includes('Adobe') || name.includes('視覺')) return '🖌️'
	if (name.includes('JavaScript') || name.includes('ES6')) return '⚡'
	if (name.includes('Vue') || name.includes('Pinia')) return '💚'
	if (name.includes('API') || name.includes('Axios')) return '🔄'
	if (name.includes('Node') || name.includes('MongoDB')) return '🟩'
	if (name.includes('Git') || name.includes('GitHub')) return '🐙'
	return '🚀'
}
</script>
