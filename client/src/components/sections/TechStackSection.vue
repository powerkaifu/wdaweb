<template>
	<section
		id="tech-stack"
		:class="[
			hideHeader
				? 'py-8 sm:py-12 bg-transparent relative'
				: 'py-16 sm:py-24 lg:py-32 bg-transparent relative overflow-hidden',
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
			<div v-if="!hideHeader" class="text-center max-w-4xl mx-auto mb-10 sm:mb-14">
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
				class="flex sm:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4"
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
			<div class="mt-12 sm:mt-16 w-full">
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

							<span
								class="hidden lg:inline-flex items-center px-4 py-1.5 rounded-full bg-slate-800/80 border border-slate-700/80 text-sm font-mono text-slate-300 self-start sm:self-auto"
							>
								Claude · ChatGPT · Cursor
							</span>
						</div>

						<!-- 說明前導段落 (維持 text-base sm:text-lg 大字，行高 1.8 舒緩，兩端切齊) -->
						<p class="text-base sm:text-lg text-slate-200 leading-relaxed text-pretty text-justify">
							寫程式不再是枯燥死記每一行語法。在課程中，你將學會如何將現代生成式 AI 工具融入日常開發流程。AI
							不是取代思考的捷徑，而是讓你能把寶貴注意力集中在「邏輯設計、架構規劃與使用者體驗」的強大助手。
						</p>

						<!-- 3 大核心 AI 輔助應用卡片 (桌機 3 欄並排，空間充裕大氣，內容精煉不冗長) -->
						<div class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-5 pt-2">
							<!-- 卡片 1 -->
							<div
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between"
							>
								<div>
									<div class="text-2xl mb-2.5">💡</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">想法轉化為程式雛型</h4>
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
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
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between"
							>
								<div>
									<div class="text-2xl mb-2.5">🔍</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">報錯解讀與輔助除錯</h4>
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
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
								class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80 hover:border-cyan-500/40 transition-colors flex flex-col justify-between"
							>
								<div>
									<div class="text-2xl mb-2.5">🛡️</div>
									<h4 class="text-lg font-bold text-white mb-2 tracking-tight">批判審核與把關驗證</h4>
									<p class="text-base text-slate-300 leading-relaxed text-pretty text-justify">
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
