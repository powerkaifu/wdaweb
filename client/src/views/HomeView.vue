<template>
	<div>
		<!-- 1. Hero 首頁動態輪播與核心價值定錨 (回歸人性的溫暖開場) -->
		<HeroCarousel />

		<!-- 2. 受眾心聲共鳴 (你心中可能也有這些猶豫……這些不安，我們都懂) -->
		<AudienceSection />

		<!-- 3. 四大起點圖譜 (你的起點不同，但不代表從零開始) -->
		<TracksSection />

		<!-- 4. 不只有一條路，你可以怎麼開始？ (自學+AI vs 實體職訓 vs 工作中學習 橫向決策輔助) -->
		<PathComparisonSection />

		<!-- 5. 實體沉浸價值 ｜ 當你真的卡住時 (解決問題視角：拆問題/雙螢幕/同儕/920h) -->
		<HighlightsSection />

		<!-- 6. 核心技術工具 (你會接觸到哪些技術) -->
		<TechStackSection />

		<!-- 7. 從第一行程式碼開始，一步一步完成自己的作品 (四階段能力蛻變路徑) -->
		<LearningPathSection />

		<!-- 8. 他們也是從第一行開始 (學員成果心理信任橋樑，定稿版核心章節) -->
		<section class="py-10 sm:py-20 lg:py-28 bg-slate-950/50 text-center relative overflow-hidden">
			<!-- 柔和微光 -->
			<div
				class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[250px] bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"
			></div>

			<div class="max-w-5xl xl:max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4 sm:space-y-6 relative z-10">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm"
				>
					<span>Student Showcase ｜ 學員專題成果</span>
				</div>

				<h2 class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-black text-white tracking-tight leading-tight">
					<span class="block">你不需要先相信自己一定能做到。</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-emerald-400"
						>先看看曾經和你一樣的人，最後做出了什麼。</span
					>
				</h2>

				<p class="text-slate-300 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed text-pretty text-justify sm:text-center">
					每一個作品的開始，都不是一個完整的工程師，而是一個願意從不熟悉的第一行開始學習的人。
				</p>

				<div class="pt-2">
					<router-link
						to="/showcase"
						class="inline-flex items-center space-x-2 px-8 py-3.5 rounded-2xl text-base font-bold text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/40 hover:-translate-y-0.5 active:scale-95 transition-all"
					>
						<span>查看歷屆學員專題成果</span>
						<span>→</span>
					</router-link>
				</div>
			</div>
		</section>

		<!-- 9. 結訓真實收穫 ｜ 你最後真正帶走的，不只是一張結訓證明 -->
		<OutcomesSection />

		<!-- 10. 教學環境與設施 ｜ 接下來的半年，你會在這樣的地方學習 -->
		<FacilitiesSection />

		<!-- 11. 誠懇安心行動召喚：自主決定與三大入口 -->
		<section
			class="py-12 sm:py-24 lg:py-32 bg-gradient-to-b from-slate-950/60 via-slate-900/40 to-slate-950 text-center relative overflow-hidden"
		>
			<!-- 柔和環境光暈 -->
			<div
				class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"
			></div>

			<div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 space-y-5 sm:space-y-7 relative z-10">
				<div
					class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 text-sm font-bold uppercase tracking-wider shadow-sm"
				>
					<span>Make Your Choice ｜ 自主決定</span>
				</div>

				<h2 class="text-2xl sm:text-3xl lg:text-4xl xl:text-5xl font-black text-white tracking-tight leading-tight">
					<span class="block">轉職從來不是一個輕鬆的決定。</span>
					<span class="block mt-1 sm:mt-1.5 text-slate-100">你不需要現在就做決定，</span>
					<span
						class="block mt-1 sm:mt-1.5 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-400 to-emerald-400"
						>先看清楚、想明白，再跨出屬於你的下一步。</span
					>
				</h2>

				<!-- 手機短金句 -->
				<p class="text-slate-300 text-base leading-relaxed text-pretty text-justify sm:hidden">
					920 小時不是速成捷徑，而是一步步扎實做出的學習旅程。先看清楚、想明白，再做最適合你的選擇。
				</p>
				<!-- 桌機完整論述 -->
				<p class="hidden sm:block text-slate-300 text-base sm:text-lg max-w-4xl xl:max-w-5xl mx-auto leading-relaxed text-pretty text-justify sm:text-center">
					<span class="block"
						>920 小時不是一條速成的捷徑，而是一段從陌生、練習、卡關，到逐漸理解與完成作品的學習旅程。</span
					>
					<span class="block mt-1 sm:mt-1.5 text-slate-200">先了解課程、看看學員作品、比較不同的學習方式，再判斷這是不是適合你的選擇。</span>
				</p>

				<!-- 三大安心入口按鈕群 (三大入口：期別時程 / 學員作品 / Discord 諮詢) -->
				<div class="pt-3 sm:pt-4 flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4">
					<router-link
						to="/admission"
						class="w-full sm:w-auto px-7 py-3.5 sm:px-8 sm:py-4 rounded-2xl font-bold text-base text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/40 hover:-translate-y-0.5 active:scale-95 transition-all inline-flex items-center justify-center space-x-2"
					>
						<span>查看最新招生期別與時程</span>
						<span>→</span>
					</router-link>

					<router-link
						to="/showcase"
						class="w-full sm:w-auto px-7 py-3.5 sm:px-8 sm:py-4 rounded-2xl font-bold text-base text-cyan-300 bg-slate-900/90 hover:bg-slate-850 border border-cyan-500/40 hover:border-cyan-400 shadow-lg hover:text-white transition-all inline-flex items-center justify-center space-x-2"
					>
						<span>先看看歷屆學員作品集</span>
						<span>→</span>
					</router-link>

					<router-link
						to="/community"
						class="w-full sm:w-auto px-7 py-3.5 sm:px-8 sm:py-4 rounded-2xl font-bold text-base text-slate-200 bg-slate-900/90 hover:bg-slate-850 border border-slate-700/90 hover:border-slate-600 shadow-lg hover:text-white transition-all inline-flex items-center justify-center space-x-2"
					>
						<span>加入 Discord 線上諮詢</span>
					</router-link>
				</div>

				<!-- 誠懇收束金句 -->
				<div class="pt-5 sm:pt-8 text-center">
					<p class="text-base sm:text-xl lg:text-2xl text-slate-200 font-bold leading-relaxed tracking-tight">
						<span class="block sm:inline">如果你決定開始，</span><span class="text-cyan-300 font-extrabold block sm:inline">我們願意陪你把第一步走得更扎實。</span>
					</p>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup lang="ts">
import { useSeoMeta } from '@/composables/useSeoMeta'
import AudienceSection from '@/components/sections/AudienceSection.vue'
import FacilitiesSection from '@/components/sections/FacilitiesSection.vue'
import HeroCarousel from '@/components/sections/HeroCarousel.vue'
import HighlightsSection from '@/components/sections/HighlightsSection.vue'
import LearningPathSection from '@/components/sections/LearningPathSection.vue'
import OutcomesSection from '@/components/sections/OutcomesSection.vue'
import PathComparisonSection from '@/components/sections/PathComparisonSection.vue'
import TechStackSection from '@/components/sections/TechStackSection.vue'
import TracksSection from '@/components/sections/TracksSection.vue'

useSeoMeta({
  title: '泰山職訓「前端網頁技術與AI應用」招生專班 ｜ 勞動部自辦 920h 全額免費培訓',
  description: '勞動部泰山職訓場「前端網頁技術與AI應用」培訓專班！920 小時實體密集培訓，一人獨立雙螢幕實作工位，完整涵蓋 Vue 3、TypeScript、AI 開發工具整合與專案作品集。待業民眾經甄試錄取享 100% 全額免費受訓與生活津貼補助，正式報名請至台灣就業通官方網站。諮詢專線：(02) 2901-8274。',
  canonicalPath: '/',
  robots: 'index, follow'
})
</script>
