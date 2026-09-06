<template>
	<section id="tracks-starting-points" class="py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden">
		<!-- 背景流光點綴 -->
		<div
			class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-emerald-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/4 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊標題 (大器單行標題，中高齡友善閱讀) -->
			<div class="text-center max-w-5xl mx-auto mb-6 sm:mb-12 lg:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
					<span>Starting Points ｜ 找到專屬起點</span>
				</div>
				<h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight text-balance">
					<span class="block">你的起點不同，</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400"
						>但不代表從零開始</span
					>
				</h2>
				<p
					class="text-slate-400 mt-4 text-base sm:text-lg max-w-none mx-auto leading-relaxed text-pretty text-left sm:text-center"
				>
					每個人走進教室時的背景都不一樣。過去的經驗不是空白，而是你在理解問題與完成作品時，最獨特的切入點。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (平板與桌機隱藏) -->
			<div class="flex sm:hidden items-center justify-center gap-2 text-base font-bold text-emerald-400 -mt-2 mb-4">
				<span>👈 左右滑動瀏覽 4 大起點軌道 👉</span>
			</div>

			<!-- 四大起點軌道 (手機版支援露邊橫向滑軌，桌機維持大器網格) -->
			<div
				id="tracks-cards-grid"
				class="flex sm:grid sm:grid-cols-2 xl:grid-cols-4 overflow-x-auto sm:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 sm:mx-0 sm:px-0 gap-4 sm:gap-6 pb-4 sm:pb-0"
			>
				<!-- 軌道 1 -->
				<div
					class="track-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default hover:border-cyan-500/50 transition-[border-color,box-shadow] duration-300 w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start sm:shrink"
				>
					<div>
						<div class="mb-3 sm:mb-3.5">
							<span
								class="inline-flex items-center space-x-2 px-3 sm:px-3.5 py-1 sm:py-1.5 rounded-2xl bg-cyan-500/10 text-cyan-300 border border-cyan-500/30 font-extrabold text-sm sm:text-base shadow-sm"
							>
								<span class="text-base sm:text-lg">🌱</span>
								<span>完全沒有程式背景</span>
							</span>
						</div>
						<h3 class="text-lg sm:text-xl font-extrabold text-white mb-2 sm:mb-2.5 tracking-tight">從零出發的轉職者</h3>
						<p class="text-base text-slate-200 leading-relaxed mb-3 sm:mb-4 text-pretty text-justify">
							<span class="sm:hidden block">零基礎別怕，天天實作演練，帶你建立扎實工程底氣。</span>
							<span class="hidden sm:inline">零基礎不用擔心。課程從最基礎的<span class="inline-block">網頁排版</span>，透過每日紮實的實作演練，帶你一步步建立扎實的<span class="inline-block">程式思維</span>。</span>
						</p>
					</div>
					<div
						class="hidden sm:block p-3 rounded-2xl bg-slate-950/70 border border-slate-800/90 text-sm 2xl:text-base font-bold text-cyan-300 xl:whitespace-nowrap overflow-hidden text-ellipsis"
					>
						💡 從第一行開始，也是一種開始
					</div>
				</div>

				<!-- 軌道 2 -->
				<div
					class="track-card card-subsurface-blue relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default hover:border-blue-500/50 transition-[border-color,box-shadow] duration-300 w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start sm:shrink"
				>
					<div>
						<div class="mb-3 sm:mb-3.5">
							<span
								class="inline-flex items-center space-x-2 px-3 sm:px-3.5 py-1 sm:py-1.5 rounded-2xl bg-blue-500/10 text-blue-300 border border-blue-500/30 font-extrabold text-sm sm:text-base shadow-sm"
							>
								<span class="text-base sm:text-lg">🔧</span>
								<span>想建立新專業</span>
							</span>
						</div>
						<h3 class="text-lg sm:text-xl font-extrabold text-white mb-2 sm:mb-2.5 tracking-tight">探索職涯可能性</h3>
						<p class="text-base text-slate-200 leading-relaxed mb-3 sm:mb-4 text-pretty text-justify">
							<span class="sm:hidden block">用半年的專注投入，為人生換一張能持續增值的技術底牌。</span>
							<span class="hidden sm:inline">為自己的職涯開拓新跑道。前端技能隨經驗持續增值，用半年的專注投入，為人生開啟具備技術底氣的新選擇。</span>
						</p>
					</div>
					<div
						class="hidden sm:block p-3 rounded-2xl bg-slate-950/70 border border-slate-800/90 text-sm 2xl:text-base font-bold text-blue-300 xl:whitespace-nowrap overflow-hidden text-ellipsis"
					>
						💡 把改變的念頭，化為每日累積
					</div>
				</div>

				<!-- 軌道 3 -->
				<div
					class="track-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default hover:border-purple-500/50 transition-[border-color,box-shadow] duration-300 w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start sm:shrink"
				>
					<div>
						<div class="mb-3 sm:mb-3.5">
							<span
								class="inline-flex items-center space-x-2 px-3 sm:px-3.5 py-1 sm:py-1.5 rounded-2xl bg-purple-500/10 text-purple-300 border border-purple-500/30 font-extrabold text-sm sm:text-base shadow-sm"
							>
								<span class="text-base sm:text-lg">🎨</span>
								<span>設計與視覺背景</span>
							</span>
						</div>
						<h3 class="text-lg sm:text-xl font-extrabold text-white mb-2.5 sm:mb-2.5 tracking-tight">設計、UI/UX 創作者</h3>
						<p class="text-base text-slate-200 leading-relaxed mb-3 sm:mb-4 text-pretty text-justify">
							<span class="sm:hidden block">懂美感再學會前端架構，親手把靜態設計稿變成活產品。</span>
							<span class="hidden sm:inline">發揮你的視覺美感優勢。學會<span class="inline-block">前端框架</span>與互動程式後，讓優秀設計不再停留在靜態稿，而是親手變成可運作的真實產品。</span>
						</p>
					</div>
					<div
						class="hidden sm:block p-3 rounded-2xl bg-slate-950/70 border border-slate-800/90 text-sm 2xl:text-base font-bold text-purple-300 xl:whitespace-nowrap overflow-hidden text-ellipsis"
					>
						💡 讓設計不只畫面，而是被實現
					</div>
				</div>

				<!-- 軌道 4 -->
				<div
					class="track-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default hover:border-emerald-500/50 transition-[border-color,box-shadow] duration-300 w-[78vw] sm:w-full max-w-[340px] md:max-w-none shrink-0 snap-start sm:shrink"
				>
					<div>
						<div class="mb-3 sm:mb-3.5">
							<span
								class="inline-flex items-center space-x-2 px-3 sm:px-3.5 py-1 sm:py-1.5 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 font-extrabold text-sm sm:text-base shadow-sm"
							>
								<span class="text-base sm:text-lg">💻</span>
								<span>曾接觸過程式</span>
							</span>
						</div>
						<h3 class="text-lg sm:text-xl font-extrabold text-white mb-2 sm:mb-2.5 tracking-tight">自學瓶頸或資訊相關</h3>
						<p class="text-base text-slate-200 leading-relaxed mb-3 sm:mb-4 text-pretty text-justify">
							<span class="sm:hidden block">告別零散碎片自學，用 920 小時把殘缺知識整合成實戰力。</span>
							<span class="hidden sm:inline">告別零散沒有順序的自學。透過<span class="inline-block"> 920 小時</span>系統化訓練，帶你將零散的語法與知識，逐步整合為能實際完成專案的能力。</span>
						</p>
					</div>
					<div
						class="hidden sm:block p-3 rounded-2xl bg-slate-950/70 border border-slate-800/90 text-sm 2xl:text-base font-bold text-emerald-300 xl:whitespace-nowrap overflow-hidden text-ellipsis"
					>
						💡 把零散的知識，整理成完整架構
					</div>
				</div>
			</div>

			<!-- 共同收束：拉向決策與自主判斷 (桌機 md: 顯示，手機端隱藏以減少垂直長度) -->
			<div class="hidden md:block mt-14 max-w-5xl xl:max-w-6xl mx-auto text-center">
				<div
					class="p-5 sm:p-7 rounded-3xl bg-slate-900/60 border border-slate-800/80 backdrop-blur-md shadow-xl text-pretty"
				>
					<p class="text-base sm:text-lg text-slate-200 leading-relaxed xl:whitespace-nowrap">
						<span class="text-emerald-400 font-bold">你不需要符合某一種標準答案，才有資格開始。</span>重要的是先了解自己的起點，再找到適合自己的學習方式。
					</p>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'

// 4 大職涯軌道卡片統一由通用 Composable 調度
useScrollStagger('#tracks-cards-grid .track-card', '#tracks-cards-grid', {
	yOffset: 28,
	duration: 0.85,
	stagger: 0.08,
	ease: 'power1.out',
	start: 'top 85%',
})
</script>
