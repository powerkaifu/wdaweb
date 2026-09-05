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
				<p class="text-slate-400 mt-4 text-base sm:text-lg max-w-4xl xl:max-w-5xl mx-auto leading-relaxed text-pretty">
					技術不是一串需要背下來的英文單字。它們不是需要背下來的名詞，而是你完成作品時會真正用到的工具。你會依照學習階段，逐步接觸不同領域的技術。
				</p>
			</div>

			<!-- 手機端橫向滑動提示 (桌機隱藏) -->
			<div v-if="!hideHeader" class="flex sm:hidden items-center justify-center gap-2 text-base font-bold text-cyan-400 -mt-4 mb-4">
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
					class="tech-card card-subsurface-glow relative rounded-3xl p-5 sm:p-6 bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-xl shadow-slate-950/60 flex flex-col justify-between overflow-hidden will-change-transform cursor-default w-[78vw] max-w-[320px] shrink-0 snap-start sm:w-full sm:max-w-none sm:shrink"
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

						<p class="text-base text-slate-300 leading-relaxed text-pretty">
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
		</div>
	</section>
</template>

<script setup lang="ts">
import { useCmsStore } from '@/stores/useCmsStore'
import { useScrollStagger } from '@/composables/useScrollStagger'

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
