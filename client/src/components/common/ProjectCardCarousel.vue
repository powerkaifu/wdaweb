<template>
  <!-- 方案三：學員成果作品 3D 卡牌輪播 — 直接用真實截圖說話 -->
  <div
    class="relative w-full h-[395px] sm:h-[430px] lg:h-[440px] xl:h-[485px] 2xl:h-[500px] rounded-2xl sm:rounded-3xl overflow-hidden border border-emerald-500/25 bg-slate-900/85 shadow-2xl shadow-emerald-950/40 backdrop-blur-xl flex flex-col"
  >
    <!-- 背景流光發光層 -->
    <div class="absolute -top-20 -right-20 w-56 h-56 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-20 -left-20 w-56 h-56 bg-cyan-600/10 rounded-full blur-3xl pointer-events-none"></div>

    <!-- 1. 頂部標題列 (Mac 風格) -->
    <div class="h-[42px] sm:h-[44px] lg:h-[48px] px-3 sm:px-4 lg:px-5 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between flex-shrink-0">
      <div class="flex items-center space-x-1.5 sm:space-x-2 overflow-hidden mr-2">
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-red-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-amber-500/80 flex-shrink-0"></div>
        <div class="w-2.5 h-2.5 sm:w-3 sm:h-3 lg:w-3.5 lg:h-3.5 rounded-full bg-emerald-500/80 flex-shrink-0"></div>
        <span class="ml-1 sm:ml-2 text-xs lg:text-sm font-mono text-slate-400 font-semibold flex items-center space-x-1 truncate">
          <span class="text-emerald-400 flex-shrink-0">🏆</span>
          <span class="truncate max-w-[120px] sm:max-w-none">學員專題成果展覽廳</span>
        </span>
      </div>
      <!-- 頁碼指示器 -->
      <div class="flex items-center space-x-1.5 flex-shrink-0">
        <span
          v-for="(_, idx) in projects"
          :key="idx"
          class="w-1.5 h-1.5 rounded-full transition-all duration-300"
          :class="idx === currentIdx ? 'bg-emerald-400 w-3' : 'bg-slate-700'"
        ></span>
      </div>
    </div>

    <!-- 2. 卡片展示主體 -->
    <div class="flex-1 relative overflow-hidden p-3 sm:p-4 lg:p-4 xl:p-5">
      <!-- 卡片層疊視覺（背景第 2 張）-->
      <div
        class="absolute inset-x-4 sm:inset-x-5 bottom-3 sm:bottom-4 h-[82%] rounded-2xl bg-slate-800/60 border border-slate-700/40 shadow-lg transform scale-[0.97] translate-y-2"
        aria-hidden="true"
      ></div>
      <!-- 卡片層疊視覺（背景第 3 張）-->
      <div
        class="absolute inset-x-7 sm:inset-x-8 bottom-2 sm:bottom-3 h-[80%] rounded-2xl bg-slate-800/40 border border-slate-700/30 shadow-md transform scale-[0.94] translate-y-3"
        aria-hidden="true"
      ></div>

      <!-- 主卡片 (帶 3D 懸浮過渡動畫) -->
      <Transition name="card-slide" mode="out-in">
        <div
          :key="currentIdx"
          class="relative h-full rounded-2xl overflow-hidden border border-slate-700/80 bg-slate-900 shadow-xl shadow-slate-950/60 flex flex-col group cursor-pointer"
          @click="nextCard"
        >
          <!-- 作品截圖 -->
          <div class="relative flex-1 overflow-hidden bg-slate-800 min-h-0">
            <img
              :src="currentProject.cover_image_url"
              :alt="currentProject.image_alt"
              class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-700 ease-out"
              @error="handleImgError"
              loading="lazy"
              decoding="async"
            />
            <!-- 圖片上的漸層遮罩（底部資訊區） -->
            <div class="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-slate-900/95 to-transparent pointer-events-none"></div>
            <!-- 右上角技術標籤 -->
            <div class="absolute top-2.5 right-2.5 flex items-center space-x-1.5">
              <span class="px-2 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 backdrop-blur-sm">
                Vue 3
              </span>
              <span class="px-2 py-0.5 rounded-full text-xs font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 backdrop-blur-sm">
                Django
              </span>
            </div>
            <!-- 點擊提示 -->
            <div class="absolute top-2.5 left-2.5 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              <span class="px-2 py-1 rounded-lg text-xs font-bold bg-slate-900/80 text-slate-300 backdrop-blur-sm border border-slate-700/60">
                下一個 →
              </span>
            </div>
          </div>

          <!-- 底部作品資訊 -->
          <div class="px-3 sm:px-4 py-2.5 sm:py-3 flex-shrink-0 bg-slate-900/95 border-t border-slate-800">
            <div class="flex items-center justify-between">
              <div class="min-w-0 flex-1 mr-2">
                <div class="font-bold text-sm sm:text-base text-white truncate">
                  {{ currentProject.project_name }}
                </div>
                <div class="text-xs text-slate-400 mt-0.5">
                  <span class="text-emerald-400 font-semibold">{{ currentProject.student_name }}</span>
                  <span class="text-slate-600 mx-1.5">·</span>
                  <span>{{ currentProject.batch_tag }} 期結業作品</span>
                </div>
              </div>
              <!-- Demo 按鈕 -->
              <a
                :href="currentProject.demo_url"
                target="_blank"
                rel="noopener noreferrer"
                @click.stop
                class="px-2.5 sm:px-3 py-1.5 rounded-xl bg-emerald-500/15 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30 text-xs font-bold flex-shrink-0 transition-all hover:scale-105 flex items-center space-x-1"
              >
                <span>Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <!-- 3. 底部統計列 -->
    <div class="h-[48px] sm:h-[52px] px-3 sm:px-4 lg:px-5 bg-gradient-to-r from-slate-950 via-slate-900 to-emerald-950/30 border-t border-emerald-500/15 flex items-center justify-between flex-shrink-0">
      <div class="flex items-center space-x-3 sm:space-x-4 text-xs font-mono">
        <span class="text-emerald-400 font-bold">{{ currentIdx + 1 }} / {{ projects.length }}</span>
        <span class="text-slate-600">·</span>
        <span class="text-slate-400">第一期畢業作品展</span>
      </div>
      <div class="text-xs font-mono text-slate-500 flex items-center space-x-1.5">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span>點擊卡片切換</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useCmsStore } from '@/stores/useCmsStore'

const cmsStore = useCmsStore()
const currentIdx = ref(0)
const brokenImages = ref<Set<number>>(new Set())

// 取前 6 筆有圖片的作品，避免輪播過長
const projects = computed(() => {
  const all = cmsStore.projects.filter(p => p.demo_url)
  // 最多顯示 8 筆
  return all.slice(0, 8)
})

const currentProject = computed(() => projects.value[currentIdx.value] || {
  id: 0,
  project_name: '學員成果作品',
  student_name: '第一期學員',
  batch_tag: '第一',
  cover_image_url: './projects/project_1.webp',
  image_alt: '學員作品截圖',
  demo_url: '#',
  github_url: '',
  view_count: 0,
  is_featured: false,
  sort_order: 0
})

function handleImgError() {
  const id = currentProject.value?.id
  if (id !== undefined) {
    brokenImages.value.add(id)
  }
}

function nextCard() {
  currentIdx.value = (currentIdx.value + 1) % Math.max(1, projects.value.length)
}

let autoTimer: ReturnType<typeof setInterval> | null = null

onMounted(() => {
  // 每 5 秒自動輪播到下一張
  autoTimer = setInterval(nextCard, 5000)
})

onUnmounted(() => {
  if (autoTimer) clearInterval(autoTimer)
})
</script>

<style scoped>
/* 卡片切換過渡動畫：左滑進入 */
.card-slide-enter-active,
.card-slide-leave-active {
  transition: all 0.38s cubic-bezier(0.4, 0, 0.2, 1);
}
.card-slide-enter-from {
  opacity: 0;
  transform: translateX(30px) scale(0.97);
}
.card-slide-leave-to {
  opacity: 0;
  transform: translateX(-30px) scale(0.97);
}
</style>
