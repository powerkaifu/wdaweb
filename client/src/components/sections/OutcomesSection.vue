<template>
	<section
		id="outcomes"
		class="py-10 sm:py-16 lg:py-24 xl:py-28 bg-transparent relative overflow-hidden"
	>
		<!-- 背景環境光暈 -->
		<div
			class="absolute top-1/2 left-1/3 -translate-y-1/2 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl pointer-events-none"
		></div>
		<div
			class="absolute top-1/2 right-1/3 -translate-y-1/2 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl pointer-events-none"
		></div>

		<div class="max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 relative z-10 w-full">
			<!-- 區塊前導標題 -->
			<div class="text-center max-w-4xl mx-auto mb-6 sm:mb-12 lg:mb-14">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm mb-3"
				>
					<span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping"></span>
					<span>Real Takeaways ｜ 結訓真實收穫</span>
				</div>
				<h2 class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-black text-white tracking-tight leading-tight text-balance">
					<span class="block sm:inline">你最後真正帶走的，</span>
					<span
						class="block sm:inline mt-1 sm:mt-0 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-emerald-400"
						>不只是一張結訓證明</span
					>
				</h2>
				<p class="text-slate-400 mt-4 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed text-pretty text-left sm:text-center">
					<span class="inline-block">920 小時</span>的學習，目的不是讓你記住更多技術名詞，而是希望你離開教室後，仍然帶著可以繼續使用的實戰能力。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div class="flex md:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-2 mb-4">
				<span>👈 左右滑動瀏覽 6 大真實收穫 👉</span>
			</div>

			<!-- 6 大真實收穫網格 (手機橫向滑軌，桌機 md: 2 欄 / lg: 3 欄) -->
			<div
				id="outcomes-cards-grid"
				class="flex md:grid md:grid-cols-2 lg:grid-cols-3 overflow-x-auto md:overflow-x-visible snap-x snap-mandatory scroll-smooth no-scrollbar -mx-4 px-4 md:mx-0 md:px-0 gap-4 sm:gap-6 pb-4 md:pb-0"
			>
				<!-- 收穫 1 -->
				<div
					class="outcome-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🌐</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">真正做出屬於自己的作品</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							獨立完成可向面試官展示、說得出架構細節與選型理由的專案代表作。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-200 leading-relaxed text-pretty text-justify">
							不只是套用模板或完成課堂作業，而是真正獨立完成可以向面試官展示、說得出架構細節與技術選型原因的專案代表作。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-slate-800/80 text-base font-bold text-cyan-400">
						✓ 擁有專屬專案代表作
					</div>
				</div>

				<!-- 收穫 2 -->
				<div
					class="outcome-card card-subsurface-blue relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🔍</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">建立拆解與解決問題的能力</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							面對 Bug 不盲猜答案，學會從 Console 定位根因，具備獨立除錯思維。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-200 leading-relaxed text-pretty text-justify">
							遇到問題與 Bug 時，不再只盲目問「答案是什麼」，而是學會從程式碼與 Console 分析「問題到底發生在哪裡」，具備獨立除錯的思維。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-slate-800/80 text-base font-bold text-blue-400">
						✓ 具備獨立除錯思維
					</div>
				</div>

				<!-- 收穫 3 -->
				<div
					class="outcome-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🤖</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">理解如何與 AI 深度協作</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							建立人機協同循環，把 AI 當成倍增效率的副駕駛而非盲抄工具。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-200 leading-relaxed text-pretty text-justify">
							不把 AI 當成複製貼上的萬能答案機，而是建立「提問 ➔ 理解 ➔ 驗證 ➔ 修改 ➔ 除錯」的人機協同循環，讓 AI 成為實戰加速器。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-slate-800/80 text-base font-bold text-purple-400">
						✓ 人機協同判斷力
					</div>
				</div>

				<!-- 收穫 4 -->
				<div
					class="outcome-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🏗️</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">建立前端與系統整合基礎</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							掌握元件、狀態、API、資料庫與部署協同運作的系統全貌。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-200 leading-relaxed text-pretty text-justify">
							清楚知道一個完整系統不是只有排版畫面，而是由前端元件、狀態資料、後端 API、資料庫與部署流程共同協同運作的全貌。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-slate-800/80 text-base font-bold text-emerald-400">
						✓ 系統全貌架構思維
					</div>
				</div>

				<!-- 收穫 5 -->
				<div
					class="outcome-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🤝</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">認識一起學習成長的夥伴</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-200 leading-relaxed text-pretty text-justify sm:hidden">
							半年朝夕相處的同學，將成為業界交流、內推與互相支持的同行夥伴。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-200 leading-relaxed text-pretty text-justify">
							半年朝夕相處的同學，未來可能成為你在軟體業界交流情報、彼此推薦與互相支持的同行者。這是孤軍自學難以複製的人脈資產。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-slate-800/80 text-base font-bold text-amber-400">
						✓ 累積第一批軟體業人脈
					</div>
				</div>

				<!-- 收穫 6 (靈魂總結卡片：特殊微光突顯) -->
				<div
					class="outcome-card card-subsurface-glow relative rounded-3xl p-5 sm:p-7 bg-gradient-to-br from-cyan-950/40 via-slate-900/90 to-slate-900/80 backdrop-blur-xl border border-cyan-500/40 shadow-xl shadow-cyan-950/40 flex flex-col justify-between overflow-hidden cursor-default w-[78vw] sm:w-[320px] max-w-[340px] shrink-0 snap-start md:w-full md:max-w-none md:shrink"
				>
					<div>
						<div class="flex items-center gap-2.5 mb-2.5 sm:mb-3">
							<span class="text-2xl sm:text-3xl shrink-0">🧭</span>
							<h3 class="text-xl font-extrabold text-white tracking-tight">更清楚自己是否適合走這條路</h3>
						</div>
						<!-- 手機短金句 -->
						<p class="text-base text-slate-100 leading-relaxed text-pretty text-justify sm:hidden">
							六個月後，你將清楚看清自己擅長什麼、喜歡什麼，明確下一步的方向。
						</p>
						<!-- 桌機完整論述 -->
						<p class="hidden sm:block text-base text-slate-100 leading-relaxed text-pretty text-justify">
							不是每個人結訓後都會走向相同道路。六個月後，你未必會得到唯一的標準答案；但你應該比現在更知道自己喜歡什麼、擅長什麼，以及下一步可以往哪裡走。
						</p>
					</div>
					<div class="pt-4 mt-4 sm:mt-5 border-t border-cyan-500/30 text-base font-extrabold text-cyan-300">
						✨ 最誠實、最寶貴的人生收穫
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script setup lang="ts">
import { useScrollStagger } from '@/composables/useScrollStagger'

// 6 大核心收穫卡片統一由通用 Composable 調度
useScrollStagger('#outcomes-cards-grid .outcome-card', '#outcomes-cards-grid', {
	yOffset: 28,
	duration: 0.85,
	stagger: 0.08,
	ease: 'power1.out',
	start: 'top 85%',
})
</script>
