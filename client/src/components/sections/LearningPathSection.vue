<template>
	<section id="learning-path" class="py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden">
		<!-- 背景環境柔和光暈 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊標題 (大器單行標題，中高齡友善閱讀) -->
			<div class="text-center max-w-4xl mx-auto mb-6 sm:mb-12 lg:mb-16">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Learning Journey ｜ 漸進式實踐路徑</span>
				</div>
				<h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight">
					<span class="block">從第一行程式碼開始，</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-emerald-400"
						>一步一步完成自己的作品</span
					>
				</h2>
				<p class="text-slate-400 mt-4 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed text-pretty text-justify sm:text-center">
					<span class="block"
						>920 小時，從「看不懂」到「知道自己正在做什麼」，一步步累積能真正做出作品的實戰能力。</span
					>
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div class="flex sm:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-2 mb-4">
				<span>👈 左右滑動瀏覽 4 階段實踐路徑 👉</span>
			</div>

			<!-- 4 階段學習歷程卡片網格 (手機橫向微滑軌，桌機 xl: 4 欄) -->
			<div
				id="learning-path-cards"
				class="flex sm:grid sm:grid-cols-2 xl:grid-cols-4 overflow-x-auto sm:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 sm:mx-0 sm:px-0 gap-4 sm:gap-6 pb-4 sm:pb-0 relative z-10"
			>
				<!-- 階段 1 -->
				<div
					class="learning-path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden hover:border-cyan-500/50 transition-[border-color,box-shadow] duration-300 cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
				>
					<!-- 角落序號水印 -->
					<div
						class="absolute -right-2 -bottom-4 text-6xl sm:text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						01
					</div>

					<div>
						<div class="flex items-center justify-between mb-4 sm:mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-2xl shadow-inner"
							>
								🧱
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-cyan-500/10 text-cyan-300 font-bold text-sm font-mono tracking-wider border border-cyan-500/30"
							>
								PHASE 01
							</span>
						</div>

						<div class="text-sm sm:text-base font-bold text-cyan-400 tracking-wider mb-1">
							Stage 01 ｜ 從看不懂開始
						</div>
						<h3 class="text-xl font-extrabold text-white mb-2 sm:mb-3 tracking-tight">開始理解網頁運作</h3>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
							從 HTML/CSS/JS 開始，理解畫面與互動原理，從看不懂到知道每行代碼在做什麼。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
							從 HTML、CSS 與 JavaScript 開始。理解網頁如何建立、文字與畫面如何排列、互動如何發生。從「滿螢幕看不懂」慢慢走向「知道每一行程式碼正在做什麼」。
						</p>
					</div>

					<div
						class="pt-4 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-cyan-300 font-semibold"
					>
						<span>核心能力</span>
						<span>HTML · CSS · JS 底層</span>
					</div>
				</div>

				<!-- 階段 2 -->
				<div
					class="learning-path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden hover:border-blue-500/50 transition-[border-color,box-shadow] duration-300 cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
				>
					<!-- 角落序號水印 -->
					<div
						class="absolute -right-2 -bottom-4 text-6xl sm:text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						02
					</div>

					<div>
						<div class="flex items-center justify-between mb-4 sm:mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-2xl shadow-inner"
							>
								🚀
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-blue-500/10 text-blue-300 font-bold text-sm font-mono tracking-wider border border-blue-500/30"
							>
								PHASE 02
							</span>
						</div>

						<div class="text-sm sm:text-base font-bold text-blue-400 tracking-wider mb-1">
							Stage 02 ｜ 從會寫到會組織
						</div>
						<h3 class="text-xl font-extrabold text-white mb-2 sm:mb-3 tracking-tight">學會組織前端系統</h3>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
							進入 Vue 3 元件化與狀態管理，不只寫出功能，更學會組織好維護的前端系統。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
							進入 Vue 3 現代前端框架。不只是把零散功能寫出來，而是開始理解元件化、狀態流與架構設計，學習如何把越來越複雜的功能整理成容易維護的前端系統。
						</p>
					</div>

					<div
						class="pt-4 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-blue-300 font-semibold"
					>
						<span>核心能力</span>
						<span>Vue 3 · 組件架構 · Pinia</span>
					</div>
				</div>

				<!-- 階段 3 -->
				<div
					class="learning-path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden hover:border-purple-500/50 transition-[border-color,box-shadow] duration-300 cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
				>
					<!-- 角落序號水印 -->
					<div
						class="absolute -right-2 -bottom-4 text-6xl sm:text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						03
					</div>

					<div>
						<div class="flex items-center justify-between mb-4 sm:mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center text-2xl shadow-inner"
							>
								💼
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-purple-500/10 text-purple-300 font-bold text-sm font-mono tracking-wider border border-purple-500/30"
							>
								PHASE 03
							</span>
						</div>

						<div class="text-sm sm:text-base font-bold text-purple-400 tracking-wider mb-1">
							Stage 03 ｜ 從前端走向完整系統
						</div>
						<h3 class="text-xl font-extrabold text-white mb-2 sm:mb-3 tracking-tight">串接真實資料流</h3>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
							串接 REST API 與資料庫，貫通前後端資料流，具備處理真實業務邏輯的能力。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
							學習前後端資料串接、REST API 與資料庫設計。開始理解前端介面、後端伺服器與資料庫如何真正串在一起，建立能處理真實資料與商業邏輯的完整專案。
						</p>
					</div>

					<div
						class="pt-4 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-purple-300 font-semibold"
					>
						<span>核心能力</span>
						<span>REST API · Node.js · 資料庫</span>
					</div>
				</div>

				<!-- 階段 4 -->
				<div
					class="learning-path-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden hover:border-emerald-500/50 transition-[border-color,box-shadow] duration-300 cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
				>
					<!-- 角落序號水印 -->
					<div
						class="absolute -right-2 -bottom-4 text-6xl sm:text-7xl font-mono font-black text-slate-800/20 select-none pointer-events-none"
					>
						04
					</div>

					<div>
						<div class="flex items-center justify-between mb-4 sm:mb-5">
							<div
								class="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-2xl shadow-inner"
							>
								🤖
							</div>
							<span
								class="px-3.5 py-1 rounded-2xl bg-emerald-500/10 text-emerald-300 font-bold text-sm font-mono tracking-wider border border-emerald-500/30"
							>
								PHASE 04
							</span>
						</div>

						<div class="text-sm sm:text-base font-bold text-emerald-400 tracking-wider mb-1">
							Stage 04 ｜ 從自己寫，到與 AI 協作
						</div>
						<h3 class="text-xl font-extrabold text-white mb-2 sm:mb-3 tracking-tight">人機協作與實戰交付</h3>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify sm:hidden">
							具備對 AI 提問、審核與除錯的判斷力，結合 Git 流程將 AI 轉化為真實生產力。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-300 leading-relaxed text-pretty text-justify">
							AI 可以幫你快速產生程式碼，但你需要逐漸具備提問、審核、除錯與架構判斷的能力。並透過 Git/GitHub 團隊協同流程，將 AI 工具轉化為真實生產力。
						</p>
					</div>

					<div
						class="pt-4 sm:pt-5 mt-4 sm:mt-6 border-t border-slate-800/80 flex items-center justify-between text-sm text-emerald-300 font-semibold"
					>
						<span>核心能力</span>
						<span>AI 協同 · 除錯驗證 · Git</span>
					</div>
				</div>
			</div>

			<!-- 核心理念總結金句 -->
			<div class="mt-6 sm:mt-12 max-w-3xl mx-auto text-center">
				<div class="p-5 sm:p-6 rounded-2xl bg-slate-900/50 border border-slate-800/80 text-pretty">
					<p class="text-base sm:text-lg text-slate-200 font-medium leading-relaxed">
						💡 <span class="text-cyan-300 font-bold">目標不是讓你記住更多語法，而是讓你逐漸知道自己正在做什麼。</span>
					</p>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'

// 4 階段學習歷程卡片統一由通用 Composable 調度
useScrollStagger('#learning-path-cards .learning-path-card', '#learning-path', {
	yOffset: 28,
	duration: 0.85,
	stagger: 0.08,
	ease: 'power1.out',
	start: 'top 85%',
})
</script>
