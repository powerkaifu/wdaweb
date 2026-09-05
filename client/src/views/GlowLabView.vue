<template>
  <div class="min-h-screen bg-transparent text-slate-100 relative overflow-x-hidden">
    
    <!-- ========================================================================= -->
    <!-- 1. 純粹無側邊欄・由上而下垂直測試工作台 (Top-to-Bottom Studio Flow) -->
    <!-- ========================================================================= -->
    <main class="relative z-10 max-w-[1536px] mx-auto px-4 sm:px-6 lg:px-8 2xl:px-12 pt-24 sm:pt-28 pb-16 space-y-20">

      <!-- ======================================================================= -->
      <!-- 頂部：實驗室標頭與一鍵返回官網 (Studio Header) -->
      <!-- ======================================================================= -->
      <section class="flex flex-col md:flex-row md:items-center justify-between gap-6 p-8 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-2xl shadow-2xl shadow-cyan-950/40">
        <div class="space-y-3 max-w-2xl">
          <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>KAIFU DESIGN & MOTION LAB ｜ 視覺動效工作台</span>
          </div>

          <h1 class="text-3xl sm:text-4xl font-black text-white tracking-tight">
            Kaifu 視覺與動效實驗室
          </h1>

          <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
            由上而下逐區切換測試，點選設定自動全域持久化儲存，點擊返回招生官網立即生效！
          </p>
        </div>

        <!-- 頂部快速跳轉按鈕 -->
        <div class="flex flex-col sm:flex-row gap-3 flex-shrink-0">
          <router-link
            to="/"
            class="px-6 py-3.5 rounded-2xl font-bold text-xs sm:text-sm text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:scale-105 active:scale-95 transition-all text-center flex items-center justify-center space-x-2 group"
          >
            <span class="group-hover:-translate-x-1 transition-transform">←</span>
            <span>返回招生官網（即刻生效）</span>
          </router-link>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 01：導覽列設計風格測試與選擇 (Navbar Styles Selection) -->
      <!-- ======================================================================= -->
      <section id="sec-navbar" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 mb-2">
              <span>SECTION 01</span>
              <span>｜</span>
              <span>NAVBAR STYLES</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              01. 導覽列設計風格測試與選擇
            </h2>
            <p class="text-sm text-slate-400 mt-1">
              當前選中：<span class="text-cyan-300 font-bold">{{ currentNavbarInfo.name }}</span>（{{ currentNavbarInfo.tagline }}）
            </p>
          </div>

          <div class="text-xs font-mono text-cyan-400 bg-cyan-500/10 px-3 py-1.5 rounded-xl border border-cyan-500/30 self-start sm:self-auto">
            ⚡ 點擊卡片直接切換
          </div>
        </div>

        <!-- 2 大方案大卡片並列 (點擊直接切換並選中) -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div
            v-for="s in navbarStyles"
            :key="s.id"
            @click="store.setNavbarStyle(s.id)"
            class="p-5 rounded-3xl border transition-all cursor-pointer flex flex-col justify-between group relative overflow-hidden"
            :class="[
              store.activeNavbarStyle === s.id
                ? 'bg-gradient-to-br from-cyan-950/60 via-slate-900/90 to-slate-950 border-cyan-500/70 shadow-2xl shadow-cyan-950/60 text-white'
                : 'bg-slate-900/60 hover:bg-slate-850 border-slate-800 text-slate-300'
            ]"
          >
            <div
              v-if="store.activeNavbarStyle === s.id"
              class="absolute left-0 top-0 bottom-0 w-1.5 bg-cyan-400 shadow-[0_0_12px_#22d3ee]"
            ></div>

            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="text-3xl p-2 rounded-2xl bg-slate-800/80 border border-slate-700/60">
                  {{ s.icon }}
                </span>
                <span
                  class="text-xs font-mono font-bold px-2.5 py-1 rounded-full"
                  :class="store.activeNavbarStyle === s.id ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40' : 'bg-slate-800 text-slate-400'"
                >
                  {{ store.activeNavbarStyle === s.id ? 'ACTIVE ✓' : '點擊選擇' }}
                </span>
              </div>

              <h3 class="font-extrabold text-base text-white mb-1.5">
                {{ s.name }}
              </h3>

              <p class="text-xs text-slate-400 leading-relaxed">
                {{ s.tagline }}
              </p>
            </div>

            <div class="pt-4 mt-4 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between">
              <span :class="store.activeNavbarStyle === s.id ? 'text-cyan-400 font-bold' : 'text-slate-500'">
                {{ store.activeNavbarStyle === s.id ? '● 已套用為全站風格' : '點此套用' }}
              </span>
              <span class="text-slate-500">→</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 02：導覽列與頁尾 1px 邊框光芒物理動態與速度調校 (Border Glow Motion Lab) -->
      <!-- ======================================================================= -->
      <section id="sec-glow-motion" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 mb-2">
              <span>SECTION 02</span>
              <span>｜</span>
              <span>BORDER GLOW MOTION LAB</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              02. 導覽列與頁尾 1px 邊框光芒物理動態與速度調校
            </h2>
            <p class="text-sm text-slate-400 mt-1">
              當前預設：<span class="text-cyan-300 font-bold">{{ currentGlowInfo.name }}</span> ｜ 速度倍率：<span class="text-cyan-400 font-mono font-bold">{{ store.glowSpeedMultiplier }}x</span>
            </p>
          </div>

          <div class="text-xs font-mono text-cyan-400 bg-cyan-500/10 px-3 py-1.5 rounded-xl border border-cyan-500/30 self-start sm:self-auto">
            🚀 4 大頂級非線性物理預設
          </div>
        </div>

        <!-- 速度倍率即時調節控制台 (Velocity Multiplier Panel) -->
        <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-5">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-lg">⏱️</span>
                <h3 class="font-extrabold text-base text-white">
                  全站動效速度倍率調節器 (Dynamic Velocity Slider)
                </h3>
              </div>
              <p class="text-xs text-slate-400 mt-1">
                直接改變 CSS 全域變數 <code class="text-cyan-300 font-mono">--glow-speed-mult</code>，毫秒級即時更新導覽列、頁尾與實驗室全部動畫！
              </p>
            </div>

            <!-- 快速倍率按鈕組 -->
            <div class="flex flex-wrap gap-2">
              <button
                v-for="opt in speedOptions"
                :key="opt.value"
                type="button"
                @click="store.setGlowSpeedMultiplier(opt.value)"
                class="px-3 py-1.5 rounded-xl text-xs font-mono font-bold transition-all cursor-pointer"
                :class="[
                  Math.abs(store.glowSpeedMultiplier - opt.value) < 0.01
                    ? 'bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/30 scale-105'
                    : 'bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 border border-slate-700/60'
                ]"
              >
                {{ opt.label }}
              </button>
            </div>
          </div>

          <!-- 精密滑桿控制 -->
          <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center pt-2 border-t border-slate-800/80">
            <div class="sm:col-span-8 flex items-center space-x-4">
              <span class="text-xs font-mono text-slate-400 min-w-[36px]">0.5x</span>
              <input
                type="range"
                min="0.5"
                max="2.0"
                step="0.05"
                :value="store.glowSpeedMultiplier"
                @input="e => store.setGlowSpeedMultiplier(parseFloat((e.target as HTMLInputElement).value))"
                class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-400"
              />
              <span class="text-xs font-mono text-slate-400 min-w-[36px]">2.0x</span>
            </div>

            <div class="sm:col-span-4 flex items-center justify-between sm:justify-end space-x-3">
              <div class="px-3 py-1 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-mono font-black text-sm shadow-inner">
                {{ store.glowSpeedMultiplier.toFixed(2) }}x 速度
              </div>
              <button
                type="button"
                @click="store.setGlowSpeedMultiplier(1.0)"
                class="px-3 py-1 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium border border-slate-700/60 transition-colors cursor-pointer"
              >
                重設 1.0x
              </button>
            </div>
          </div>
        </div>

        <!-- 4 大動效風格卡片網格 -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div
            v-for="g in glowPresets"
            :key="g.id"
            @click="store.setGlowPreset(g.id)"
            class="p-6 rounded-3xl border transition-all cursor-pointer flex flex-col justify-between group relative overflow-hidden"
            :class="[
              store.activeGlowPreset === g.id
                ? 'bg-gradient-to-br from-cyan-950/60 via-slate-900/90 to-slate-950 border-cyan-500/70 shadow-2xl shadow-cyan-950/60 text-white'
                : 'bg-slate-900/60 hover:bg-slate-850 border-slate-800 text-slate-300'
            ]"
          >
            <div
              v-if="store.activeGlowPreset === g.id"
              class="absolute left-0 top-0 bottom-0 w-1.5 bg-cyan-400 shadow-[0_0_12px_#22d3ee]"
            ></div>

            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                  <span class="text-2xl p-2 rounded-2xl bg-slate-800/80 border border-slate-700/60">
                    {{ g.icon }}
                  </span>
                  <div>
                    <span class="text-xs font-mono font-bold px-2 py-0.5 rounded-md bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                      {{ g.badge }}
                    </span>
                  </div>
                </div>
                <span
                  class="text-xs font-mono font-bold px-3 py-1 rounded-full"
                  :class="store.activeGlowPreset === g.id ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40' : 'bg-slate-800 text-slate-400'"
                >
                  {{ store.activeGlowPreset === g.id ? 'ACTIVE ✓' : '點擊切換' }}
                </span>
              </div>

              <div>
                <h3 class="font-black text-lg text-white mb-1">
                  {{ g.name }}
                </h3>
                <p class="text-xs text-cyan-300/80 font-mono leading-relaxed">
                  {{ g.tagline }}
                </p>
              </div>

              <!-- 動效物理參數規格表 -->
              <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 space-y-0.5">
                  <div class="text-xs text-slate-500">週期時間</div>
                  <div class="text-cyan-300 font-bold truncate">{{ g.duration }}</div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 space-y-0.5">
                  <div class="text-xs text-slate-500">佔空留白比</div>
                  <div class="text-emerald-400 font-bold truncate">{{ g.dutyCycle }}</div>
                </div>
                <div class="col-span-2 p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 space-y-0.5">
                  <div class="text-xs text-slate-500">運動曲線 (Easing)</div>
                  <div class="text-purple-300 font-bold font-mono text-xs truncate">{{ g.easing }}</div>
                </div>
              </div>

              <p class="text-xs text-slate-400 leading-relaxed">
                {{ g.description }}
              </p>

              <!-- 卡片內置即時單軌預覽 (Mini Live Preview Track) -->
              <div class="pt-2">
                <div class="text-xs font-mono text-slate-500 mb-1.5 flex justify-between">
                  <span>單軌動效即時預覽：</span>
                  <span class="text-cyan-400">100vw 視窗等比模擬</span>
                </div>
                <div class="relative h-6 bg-slate-950/90 rounded-xl border border-slate-800/80 overflow-hidden flex items-center px-2">
                  <div class="w-full h-[1px] bg-slate-800/80 absolute inset-x-0"></div>
                  <!-- 模擬光暈 -->
                  <div
                    class="w-32 h-2 bg-gradient-to-r from-transparent via-cyan-400/90 via-blue-400/70 to-transparent blur-[2px] rounded-full pointer-events-none"
                    :class="`glow-stream-${g.id}`"
                  ></div>
                  <!-- 模擬 1px 亮線 -->
                  <div
                    class="w-24 h-[1px] bg-gradient-to-r from-transparent via-cyan-100 via-cyan-300 to-transparent shadow-[0_0_6px_#22d3ee] pointer-events-none"
                    :class="`glow-stream-${g.id}`"
                  ></div>
                </div>
              </div>
            </div>

            <div class="pt-4 mt-4 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between">
              <span :class="store.activeGlowPreset === g.id ? 'text-cyan-400 font-bold' : 'text-slate-500'">
                {{ store.activeGlowPreset === g.id ? '● 已套用至全站導覽列與頁尾' : '點此套用此動態物理方案' }}
              </span>
              <span class="text-slate-500">→</span>
            </div>
          </div>
        </div>

        <!-- 天地呼應即時對位模擬器 (Twin-Track Polyphony Simulator) -->
        <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-2xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800/80 pb-4">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center text-xl">
                🌌
              </div>
              <div>
                <h3 class="font-black text-lg text-white">
                  天地呼應與相位對位即時監控台 (Navbar 天 ｜ Footer 地 雙軌同步)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">
                  觀測頂部導覽列光束與頁尾光束在時間軸上的交錯對位律動（Polyphonic Counterpoint）
                </p>
              </div>
            </div>

            <div class="text-xs font-mono px-3 py-1.5 rounded-xl bg-slate-950 border border-cyan-500/30 text-cyan-300">
              當前模式：{{ currentGlowInfo.name }}
            </div>
          </div>

          <!-- 雙軌視覺展示 -->
          <div class="space-y-4">
            <!-- 頂部 Navbar 軌道 -->
            <div class="space-y-1.5">
              <div class="flex items-center justify-between text-xs font-mono">
                <span class="text-cyan-400 font-bold flex items-center space-x-1.5">
                  <span>🔺 天：頂部導覽列 (Navbar Precision 1px Line)</span>
                </span>
                <span class="text-slate-500">相位 0.0s 始發基準</span>
              </div>
              <div class="relative h-10 bg-slate-950 rounded-2xl border border-slate-800 overflow-hidden flex items-center">
                <div class="w-full h-[1px] bg-slate-800/80 absolute inset-x-0"></div>
                <!-- 一體化運動光艙 (天) -->
                <div
                  class="absolute inset-y-0 w-80 pointer-events-none flex flex-col items-center justify-center"
                  :class="`glow-stream-${store.activeGlowPreset}`"
                >
                  <!-- 內部背光 -->
                  <div class="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-500/25 via-blue-500/20 to-transparent blur-md"></div>
                  <!-- 光暈 -->
                  <div class="w-4/5 h-[3px] bg-gradient-to-r from-transparent via-cyan-400/90 via-blue-400/70 to-transparent blur-[2px] rounded-full"></div>
                  <!-- 1px 核心線 -->
                  <div class="w-3/5 h-[1.5px] -translate-y-[1px] bg-gradient-to-r from-transparent via-white via-cyan-300 to-transparent shadow-[0_0_8px_#22d3ee]"></div>
                </div>
              </div>
            </div>

            <!-- 底部 Footer 軌道 -->
            <div class="space-y-1.5">
              <div class="flex items-center justify-between text-xs font-mono">
                <span class="text-blue-400 font-bold flex items-center space-x-1.5">
                  <span>🔻 地：底部頁尾 (Footer Precision 1px Line)</span>
                </span>
                <span class="text-slate-500">相位交錯延遲呼應中</span>
              </div>
              <div class="relative h-10 bg-slate-950 rounded-2xl border border-slate-800 overflow-hidden flex items-center">
                <div class="w-full h-[1px] bg-slate-800/80 absolute inset-x-0"></div>
                <!-- 一體化運動光艙 (地) -->
                <div
                  class="absolute inset-y-0 w-80 pointer-events-none flex flex-col items-center justify-center"
                  :class="`footer-glow-${store.activeGlowPreset}`"
                >
                  <!-- 內部背光 -->
                  <div class="absolute inset-0 bg-gradient-to-r from-transparent via-cyan-500/25 via-blue-500/20 to-transparent blur-md"></div>
                  <!-- 光暈 -->
                  <div class="w-4/5 h-[3px] bg-gradient-to-r from-transparent via-cyan-400/90 via-blue-400/70 to-transparent blur-[2px] rounded-full"></div>
                  <!-- 1px 核心線 -->
                  <div class="w-3/5 h-[1.5px] -translate-y-[1px] bg-gradient-to-r from-transparent via-white via-cyan-300 to-transparent shadow-[0_0_8px_#22d3ee]"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 03：全域背景氛圍測試與展示 (Ambient Background Studio) -->
      <!-- ======================================================================= -->
      <section id="sec-bg" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 mb-2">
              <span>SECTION 03</span>
              <span>｜</span>
              <span>AMBIENT BACKGROUND</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              03. 全域背景氛圍測試與展示
            </h2>
            <p class="text-sm text-slate-400 mt-1">
              當前運作：<span class="text-cyan-300 font-bold">3D 宇宙深空流動星雲 (Three.js WebGL)</span> ｜ 全站 100% 常駐高幀率渲染
            </p>
          </div>

          <div class="text-xs font-mono text-cyan-400 bg-cyan-500/10 px-3 py-1.5 rounded-xl border border-cyan-500/30 self-start sm:self-auto">
            🌌 旗艦定案基準
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <!-- 旗艦定案卡片：3D 宇宙深空流動星雲 -->
          <div class="p-6 rounded-3xl bg-gradient-to-br from-cyan-950/60 via-slate-900/90 to-slate-950 border border-cyan-500/70 shadow-2xl shadow-cyan-950/60 text-white relative overflow-hidden flex flex-col justify-between group">
            <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-cyan-400 shadow-[0_0_12px_#22d3ee]"></div>

            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-3xl p-2 rounded-2xl bg-slate-800/80 border border-slate-700/60">
                  🌌
                </span>
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">
                  ACTIVE ✓ ｜ 全站旗艦定案
                </span>
              </div>

              <div>
                <h3 class="font-extrabold text-lg text-white mb-2">
                  1. 3D 宇宙深空流動星雲與銀河星空 (3D Nebula & Milky Way Stars)
                </h3>
                <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                  5 大 3D 柔焦星雲漫游交疊，搭配 130 顆三階星等銀河繁星（微暗星、中景星、璀璨亮星）在深空中自然眨眼微閃爍，營造如高山觀星般的浪漫深邃銀河！
                </p>
              </div>

              <!-- 規格參數徽章 -->
              <div class="grid grid-cols-2 gap-2.5 pt-2">
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 text-xs font-mono text-cyan-300 flex items-center space-x-2">
                  <span>☁️</span>
                  <span>5 大星雲自轉舒展</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 text-xs font-mono text-cyan-300 flex items-center space-x-2">
                  <span>✨</span>
                  <span>320 顆銀河繁星微閃</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 text-xs font-mono text-cyan-300 flex items-center space-x-2">
                  <span>💎</span>
                  <span>三階星等微十字星芒</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 text-xs font-mono text-cyan-300 flex items-center space-x-2">
                  <span>⚡</span>
                  <span>120fps+ WebGL</span>
                </div>
              </div>
            </div>

            <div class="pt-4 mt-4 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between text-cyan-400 font-bold">
              <span>● 全站常駐運作中</span>
              <span>100% LOADED ✓</span>
            </div>
          </div>

          <!-- 5 大星雲深空物理特性即時調控台 (Deep Space Physics Controls) -->
          <div class="p-6 rounded-3xl bg-slate-900/80 backdrop-blur-xl border border-slate-800/90 shadow-2xl shadow-slate-950/60 text-white flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/40">
                  🎛️ 4 大星雲物理特性即時調控台
                </span>
                <span class="text-xs font-mono text-slate-400">
                  REAL-TIME PHYSICS
                </span>
              </div>

              <div class="space-y-2.5 pt-1">
                <!-- 1. 游標引力透鏡視差 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>🪐</span>
                    <span class="font-bold text-slate-200">游標引力透鏡視差 (Parallax)</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.nebulaFeatures.mouseParallax"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 focus:ring-offset-0 cursor-pointer"
                  />
                </label>

                <!-- 2. 絲狀雲氣纖維紋理 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>🌪️</span>
                    <span class="font-bold text-slate-200">絲狀雲氣纖維紋理 (Filaments)</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.nebulaFeatures.filamentNoise"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 focus:ring-offset-0 cursor-pointer"
                  />
                </label>

                <!-- 3. 引力波能量交織呼吸 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>💓</span>
                    <span class="font-bold text-slate-200">引力波能量交織呼吸 (Breathing)</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.nebulaFeatures.entangledPulse"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 focus:ring-offset-0 cursor-pointer"
                  />
                </label>

                <!-- 4. 滾動深空穿梭推進 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>🚀</span>
                    <span class="font-bold text-slate-200">滾動深空穿梭推進 (Scroll Warp)</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.nebulaFeatures.scrollWarp"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 focus:ring-offset-0 cursor-pointer"
                  />
                </label>
              </div>
            </div>

            <div class="pt-3 mt-3 border-t border-slate-800/80 text-xs font-mono text-slate-400 flex items-center justify-between">
              <span>4 大物理特性即時連動中</span>
              <span class="text-cyan-400 font-bold">ALL SYSTEMS LIVE</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 03.5：Awwwards 級 360° 天球仰望偶發流星控制台 (Celestial Meteor Lab) -->
      <!-- ======================================================================= -->
      <section id="sec-meteors" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-500/10 text-amber-400 border border-amber-500/30 mb-2">
              <span>SECTION 03.5</span>
              <span>｜</span>
              <span>CELESTIAL SPORADIC METEORS</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              03.5 360° 天球仰望偶發流星物理實驗室
            </h2>
            <p class="text-sm text-slate-400 mt-1">
              打破傳統單向傾斜流星！重現仰望真實天穹時，流星從四面八方隨機偶發穿梭、白熱等離子高熱核與微爆火流星光學！
            </p>
          </div>

          <!-- ⚡ 立即召喚流星大按鈕群 (Instant Meteor Launches) -->
          <div class="flex flex-wrap gap-2.5 flex-shrink-0">
            <button
              type="button"
              @click="store.triggerMeteor()"
              class="px-5 py-3 rounded-2xl font-black text-xs sm:text-sm text-slate-950 bg-gradient-to-r from-amber-300 via-amber-400 to-yellow-500 hover:from-amber-200 hover:to-yellow-400 shadow-xl shadow-amber-500/25 hover:shadow-amber-500/40 hover:scale-105 active:scale-95 transition-all flex items-center justify-center space-x-2 cursor-pointer"
            >
              <span>⚡</span>
              <span>發射流星</span>
            </button>
            <button
              type="button"
              @click="store.triggerCodeMeteor()"
              class="px-5 py-3 rounded-2xl font-black text-xs sm:text-sm text-slate-950 bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 hover:from-emerald-300 hover:to-cyan-300 shadow-xl shadow-emerald-500/25 hover:shadow-emerald-500/40 hover:scale-105 active:scale-95 transition-all flex items-center justify-center space-x-2 cursor-pointer"
            >
              <span>👾</span>
              <span>發射代碼流星</span>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <!-- 卡片 1: 頻率節奏模式 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                ⏱️ 頻率節奏模式
              </span>
              <span class="text-xs font-mono text-slate-400">FREQUENCY</span>
            </div>

            <div class="space-y-2">
              <button
                type="button"
                @click="store.setMeteorMode('sporadic')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.mode === 'sporadic' ? 'bg-cyan-500/20 border-cyan-400/60 text-white shadow-lg shadow-cyan-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">🌌 靜謐偶發（8~22s 久久一次）</div>
                  <div class="text-xs text-slate-400 mt-0.5">預設推薦！符合真實夜空仰望，靜謐不干擾閱讀</div>
                </div>
                <span v-if="store.meteorConfig.mode === 'sporadic'" class="text-cyan-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>

              <button
                type="button"
                @click="store.setMeteorMode('shower')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.mode === 'shower' ? 'bg-cyan-500/20 border-cyan-400/60 text-white shadow-lg shadow-cyan-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">🎆 璀璨流星雨（2~5s 頻繁穿梭）</div>
                  <div class="text-xs text-slate-400 mt-0.5">適合動效展演與即時視覺鑑賞</div>
                </div>
                <span v-if="store.meteorConfig.mode === 'shower'" class="text-cyan-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>

              <button
                type="button"
                @click="store.setMeteorMode('fireball')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.mode === 'fireball' ? 'bg-amber-500/20 border-amber-400/60 text-white shadow-lg shadow-amber-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">💥 純微爆火流星（Fireballs Only）</div>
                  <div class="text-xs text-slate-400 mt-0.5">每顆流星均伴隨 110px 耀斑微爆與散落碎屑火花</div>
                </div>
                <span v-if="store.meteorConfig.mode === 'fireball'" class="text-amber-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>
            </div>
          </div>

          <!-- 卡片 2: 360° 天球放射幾何 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/30">
                🧭 發射幾何方向
              </span>
              <span class="text-xs font-mono text-slate-400">GEOMETRY</span>
            </div>

            <div class="space-y-2">
              <button
                type="button"
                @click="store.setMeteorDirection('omnidirectional')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.direction === 'omnidirectional' ? 'bg-purple-500/20 border-purple-400/60 text-white shadow-lg shadow-purple-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">🌐 360° 仰望天穹四面八方</div>
                  <div class="text-xs text-slate-400 mt-0.5">自上、下、左、右各維度隨機劃過夜空</div>
                </div>
                <span v-if="store.meteorConfig.direction === 'omnidirectional'" class="text-purple-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>

              <button
                type="button"
                @click="store.setMeteorDirection('radiant')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.direction === 'radiant' ? 'bg-purple-500/20 border-purple-400/60 text-white shadow-lg shadow-purple-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">🎯 天頂深空向外輻射 (Radiant)</div>
                  <div class="text-xs text-slate-400 mt-0.5">從天頂輻射點朝 360° 圓形散射而出</div>
                </div>
                <span v-if="store.meteorConfig.direction === 'radiant'" class="text-purple-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>

              <button
                type="button"
                @click="store.setMeteorDirection('diagonal')"
                class="w-full p-3 rounded-2xl border text-left transition-all flex items-center justify-between"
                :class="store.meteorConfig.direction === 'diagonal' ? 'bg-purple-500/20 border-purple-400/60 text-white shadow-lg shadow-purple-500/10' : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700'"
              >
                <div>
                  <div class="font-bold text-sm">📐 經典斜向掠過 (Diagonal)</div>
                  <div class="text-xs text-slate-400 mt-0.5">維持傳統右上向左下之流線軌跡</div>
                </div>
                <span v-if="store.meteorConfig.direction === 'diagonal'" class="text-purple-400 font-mono text-xs font-bold">ACTIVE ✓</span>
              </button>
            </div>
          </div>

          <!-- 卡片 3: 光學物理特性規格 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl flex flex-col justify-between space-y-4">
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  🔬 光學物理規格
                </span>
                <span class="text-xs font-mono text-slate-400">PHYSICS SPEC</span>
              </div>

              <div class="space-y-2.5 text-xs font-mono">
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">等離子白熱針尖核心</span>
                  <span class="text-white font-bold">#FFFFFF (1.4~2.2px)</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">非線性電離彗尾長度</span>
                  <span class="text-cyan-300 font-bold">140px ~ 440px</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">火流星耀斑微爆脈衝</span>
                  <span class="text-amber-300 font-bold">110px Radial Flare</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">殘留發光煙霧痕跡</span>
                  <span class="text-purple-300 font-bold">1.2s Slow Diffusion</span>
                </div>
              </div>
            </div>

            <div class="pt-3 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between text-slate-400">
              <span>全天球流星已全域啟用</span>
              <span class="text-cyan-400 font-bold">60FPS CANVAS 2D</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 03.6：AI 深空量子思維漣漪與幽靈代碼彩蛋控制台 (Quantum Waves & Cyber Easter Egg) -->
      <!-- ======================================================================= -->
      <section id="sec-easter-eggs" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-4">
          <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 mb-2">
              <span>SECTION 03.6</span>
              <span>｜</span>
              <span>QUANTUM MIND WAVES & CYBER MATRIX EASTER EGGS</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              03.6 AI 深空量子思維漣漪與幽靈代碼彩蛋
            </h2>
            <p class="text-sm text-slate-400 mt-1">
              為仰望星空注入極致純淨的 AI 科技彩蛋！無連線噪訊干擾、自發性量子思維漣漪光環、以及進站首發與自然掠過的幽靈代碼流星！
            </p>
          </div>

          <!-- 🧠 立即激發神經元量子脈衝按鈕 -->
          <div class="flex flex-wrap gap-2.5 flex-shrink-0">
            <button
              type="button"
              @click="store.triggerSynapticPulse()"
              class="px-5 py-3 rounded-2xl font-black text-xs sm:text-sm text-white bg-gradient-to-r from-cyan-500 via-blue-600 to-purple-600 hover:from-cyan-400 hover:to-purple-500 shadow-xl shadow-cyan-500/25 hover:scale-105 active:scale-95 transition-all flex items-center justify-center space-x-2 cursor-pointer"
            >
              <span>🧠</span>
              <span>激發量子思維漣漪</span>
            </button>
            <button
              type="button"
              @click="store.triggerCodeMeteor()"
              class="px-5 py-3 rounded-2xl font-black text-xs sm:text-sm text-slate-950 bg-gradient-to-r from-emerald-400 to-teal-300 hover:from-emerald-300 hover:to-teal-200 shadow-xl shadow-emerald-500/25 hover:scale-105 active:scale-95 transition-all flex items-center justify-center space-x-2 cursor-pointer"
            >
              <span>⚡</span>
              <span>發射幽靈代碼流星</span>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <!-- 卡片 1: 👾 幽靈代碼流星彩蛋 (Cyber Matrix Code-Meteor) -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-4 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  👾 幽靈代碼流星彩蛋
                </span>
                <span class="text-xs font-mono text-slate-400">CYBER MATRIX</span>
              </div>

              <div>
                <h3 class="font-bold text-base text-white mb-1">黑客科技矩陣流星</h3>
                <p class="text-xs text-slate-400 leading-relaxed">
                  🌟 進站 2.2 秒首發 100% 必定掠過！後續全天球流星 55% 偶發轉化，沿途動態拋灑發光微塵符號粒子！
                </p>
              </div>

              <!-- 機率切換按鈕組 -->
              <div class="space-y-2">
                <label class="text-xs font-mono text-slate-300 font-bold block">
                  偶發生成機率 (Chance)
                </label>
                <div class="grid grid-cols-4 gap-2">
                  <button
                    v-for="c in [
                      { label: '15%', val: 0.15 },
                      { label: '35%', val: 0.35 },
                      { label: '55%', val: 0.55 },
                      { label: '100%', val: 1.00 }
                    ]"
                    :key="c.val"
                    type="button"
                    @click="store.meteorConfig.codeMeteorChance = c.val"
                    class="py-1.5 px-2 rounded-xl text-xs font-mono font-bold transition-all cursor-pointer text-center"
                    :class="[
                      Math.abs(store.meteorConfig.codeMeteorChance - c.val) < 0.05
                        ? 'bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-950 font-black shadow-md shadow-emerald-500/30 scale-105'
                        : 'bg-slate-950/70 text-slate-400 hover:text-slate-200 border border-slate-800'
                    ]"
                  >
                    {{ c.label }}
                  </button>
                </div>
              </div>

              <!-- 發光代碼微塵粒子庫預覽 (職訓核心技能分組) -->
              <div class="p-3 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-2.5">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-mono text-emerald-400 font-bold">
                    🔤 職訓核心技能微塵庫 (Skills Pool)
                  </span>
                  <span class="text-xs font-mono text-slate-400">20 顆技能粒子</span>
                </div>
                
                <div class="space-y-2 text-xs font-mono">
                  <!-- 前端 -->
                  <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                    <span class="text-slate-400 font-bold min-w-[32px]">前端:</span>
                    <span class="px-1.5 py-0.5 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">&lt;Vue/&gt;</span>
                    <span class="px-1.5 py-0.5 rounded bg-amber-500/15 text-amber-300 border border-amber-500/30">JavaScript</span>
                    <span class="px-1.5 py-0.5 rounded bg-orange-500/15 text-orange-300 border border-orange-500/30">HTML5</span>
                    <span class="px-1.5 py-0.5 rounded bg-sky-500/15 text-sky-300 border border-sky-500/30">CSS3</span>
                    <span class="px-1.5 py-0.5 rounded bg-yellow-500/15 text-yellow-300 border border-yellow-500/30">Pinia</span>
                    <span class="px-1.5 py-0.5 rounded bg-purple-500/15 text-purple-300 border border-purple-500/30">Bootstrap</span>
                  </div>

                  <!-- 後端與資料庫 -->
                  <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                    <span class="text-slate-400 font-bold min-w-[32px]">後端:</span>
                    <span class="px-1.5 py-0.5 rounded bg-green-500/15 text-green-300 border border-green-500/30">Node.js</span>
                    <span class="px-1.5 py-0.5 rounded bg-slate-500/15 text-slate-300 border border-slate-500/30">Express</span>
                    <span class="px-1.5 py-0.5 rounded bg-sky-500/15 text-sky-300 border border-sky-500/30">REST API</span>
                    <span class="px-1.5 py-0.5 rounded bg-indigo-500/15 text-indigo-300 border border-indigo-500/30">Axios</span>
                    <span class="px-1.5 py-0.5 rounded bg-rose-500/15 text-rose-300 border border-rose-500/30">NPM</span>
                  </div>

                  <!-- 資料庫 (MongoDB) -->
                  <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                    <span class="text-slate-400 font-bold min-w-[32px]">庫:</span>
                    <span class="px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/40">MongoDB</span>
                    <span class="px-1.5 py-0.5 rounded bg-teal-500/15 text-teal-300 border border-teal-500/30">NoSQL</span>
                    <span class="px-1.5 py-0.5 rounded bg-amber-500/15 text-amber-300 border border-amber-500/30">JSON</span>
                    <span class="px-1.5 py-0.5 rounded bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">CRUD</span>
                  </div>

                  <!-- AI 與 920h -->
                  <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                    <span class="text-slate-400 font-bold min-w-[32px]">AI:</span>
                    <span class="px-1.5 py-0.5 rounded bg-pink-500/15 text-pink-300 border border-pink-500/30">AI</span>
                    <span class="px-1.5 py-0.5 rounded bg-rose-500/15 text-rose-300 border border-rose-500/30">GenAI</span>
                    <span class="px-1.5 py-0.5 rounded bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">Prompt</span>
                    <span class="px-1.5 py-0.5 rounded bg-fuchsia-500/15 text-fuchsia-300 border border-fuchsia-500/30">Agent</span>
                    <span class="text-slate-400 font-bold ml-1">時數:</span>
                    <span class="px-1.5 py-0.5 rounded bg-white/20 text-white font-bold border border-white/40">920h</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="pt-3 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between text-slate-400">
              <span>JetBrains Mono 原生渲染</span>
              <span class="text-emerald-400 font-bold">READY</span>
            </div>
          </div>

          <!-- 卡片 2: 🧠 AI 量子思維漣漪 (Quantum Mind Waves) -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-4 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
                  🧠 AI 量子思維光環
                </span>
                <span class="text-xs font-mono text-slate-400">QUANTUM WAVES</span>
              </div>

              <div>
                <h3 class="font-bold text-base text-white mb-1">深空純淨無連線・思維漣漪</h3>
                <p class="text-xs text-slate-400 leading-relaxed">
                  深空繁星純淨自然無直線連線；每隔 9~14 秒自發性向外擴散出一圈同心量子柔焦光環，大器深邃不干擾閱讀！
                </p>
              </div>

              <!-- 特性開關 -->
              <div class="space-y-2.5">
                <!-- 1. 總開關 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>🌐</span>
                    <span class="font-bold text-slate-200">啟用量子思維光環</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.synapticConfig.enabled"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 cursor-pointer"
                  />
                </label>

                <!-- 2. 自發性深空量子思維放電 -->
                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 hover:border-cyan-500/40 cursor-pointer transition-all">
                  <div class="flex items-center space-x-2.5 text-xs sm:text-sm">
                    <span>🌊</span>
                    <span class="font-bold text-slate-200">自發性宇宙思維量子漣漪 (9~14s)</span>
                  </div>
                  <input
                    type="checkbox"
                    v-model="store.synapticConfig.autonomousPulse"
                    class="w-4 h-4 rounded text-cyan-500 bg-slate-900 border-slate-700 focus:ring-cyan-500 cursor-pointer"
                  />
                </label>
              </div>
            </div>

            <div class="pt-3 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between text-slate-400">
              <span>無連線純淨星空</span>
              <span class="text-cyan-400 font-bold">ACTIVE</span>
            </div>
          </div>

          <!-- 卡片 3: 💫 彩蛋體驗引導與效能指標 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 backdrop-blur-xl shadow-xl space-y-4 flex flex-col justify-between">
            <div class="space-y-3.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/30">
                  💫 彩蛋體驗引導
                </span>
                <span class="text-xs font-mono text-slate-400">HOW IT FEELS</span>
              </div>

              <div>
                <h3 class="font-bold text-base text-white mb-1">純粹深空・絕無干擾</h3>
                <p class="text-xs text-slate-400 leading-relaxed">
                  繁星維持最純天然閃爍與星雲漫游，無任何連線噪訊；偶爾掠過的代碼流星與量子光環讓民眾會心一笑！
                </p>
              </div>

              <div class="space-y-2 text-xs font-mono">
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">量子思維漣漪擴散半徑</span>
                  <span class="text-cyan-300 font-bold">220px ~ 360px</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">進站首發代碼流星</span>
                  <span class="text-emerald-300 font-bold">2.2 秒 100% 必出</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 flex items-center justify-between">
                  <span class="text-slate-400">GPU / CPU 額外開銷</span>
                  <span class="text-emerald-400 font-bold">&lt; 0.2ms (極致絲滑)</span>
                </div>
              </div>
            </div>

            <div class="pt-3 border-t border-slate-800/80 text-xs font-mono flex items-center justify-between text-slate-400">
              <span>全域同步生效於所有分頁</span>
              <span class="text-purple-400 font-bold">ACTIVE</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 區域 04：UI 卡片與 3D 微互動展演區 (UI Components & Micro-interactions) -->
      <!-- ======================================================================= -->
      <section id="sec-ui" class="space-y-6">
        <div class="border-b border-slate-800 pb-4">
          <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 mb-2">
            <span>SECTION 04</span>
            <span>｜</span>
            <span>UI MICRO-INTERACTIONS</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
            04. UI 卡片與 3D 微互動展演區
          </h2>
          <p class="text-sm text-slate-400 mt-1">
            測試各類按鈕光效、毛玻璃質感與卡片在深色星雲背景下的易讀性與反饋手感。
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- 卡片 1: 磁吸科技按鈕光影 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-xl space-y-4 group hover:border-cyan-500/50 transition-all">
            <div class="w-10 h-10 rounded-xl bg-cyan-500/15 border border-cyan-500/30 text-cyan-400 flex items-center justify-center text-xl">
              ⚡
            </div>
            <h4 class="text-base font-extrabold text-white group-hover:text-cyan-300 transition-colors">
              流光霓虹漸層按鈕
            </h4>
            <p class="text-xs text-slate-400 leading-relaxed">
              自帶呼吸漸層與微發光邊框，點擊時伴隨輕微微震回饋。
            </p>
            <div class="pt-2">
              <button
                type="button"
                class="w-full py-3 rounded-xl font-bold text-xs text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-lg shadow-cyan-500/25 hover:scale-105 active:scale-95 transition-all cursor-pointer"
              >
                互動體驗按鈕 →
              </button>
            </div>
          </div>

          <!-- 卡片 2: 毛玻璃全息卡片 -->
          <div class="p-6 rounded-3xl bg-slate-900/60 backdrop-blur-xl border border-slate-800/80 shadow-xl space-y-4 group hover:border-blue-500/50 transition-all">
            <div class="w-10 h-10 rounded-xl bg-blue-500/15 border border-blue-500/30 text-blue-400 flex items-center justify-center text-xl">
              💎
            </div>
            <h4 class="text-base font-extrabold text-white group-hover:text-blue-300 transition-colors">
              深度毛玻璃 (Frosted Glass)
            </h4>
            <p class="text-xs text-slate-400 leading-relaxed">
              高斯模糊消隱底層雜訊，確保在動態星雲背景上文字依然具備 100% 高對比度。
            </p>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800/60 text-xs font-mono text-slate-300">
              backdrop-blur-2xl ｜ bg-slate-900/80
            </div>
          </div>

          <!-- 卡片 3: AI 脈衝呼吸燈 -->
          <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-xl space-y-4 group hover:border-emerald-500/50 transition-all">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 flex items-center justify-center text-xl">
              🤖
            </div>
            <h4 class="text-base font-extrabold text-white group-hover:text-emerald-300 transition-colors">
              AI 脈衝呼吸燈
            </h4>
            <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2 font-mono text-xs">
              <div class="flex items-center space-x-2 text-emerald-400">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                <span>SYSTEM ONLINE</span>
              </div>
              <div class="text-xs text-slate-500">AI AGENT: READY</div>
            </div>
          </div>
        </div>
      </section>

      <!-- ======================================================================= -->
      <!-- 底部：一鍵返回官網檢驗 (Bottom Action Hub) -->
      <!-- ======================================================================= -->
      <section class="p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-slate-900/90 to-slate-950 border border-cyan-500/30 shadow-2xl text-center space-y-4">
        <h3 class="text-xl font-extrabold text-white">
          測試完畢？所有選擇皆已全域同步生效！
        </h3>
        <p class="text-sm text-slate-400">
          當前配置：導覽列【<span class="text-cyan-300 font-bold">{{ currentNavbarInfo.name }}</span>】 ｜ 邊框動效【<span class="text-cyan-300 font-bold">{{ currentGlowInfo.name }}</span>】 ｜ 速度【<span class="text-cyan-300 font-mono font-bold">{{ store.glowSpeedMultiplier }}x</span>】
        </p>
        <div class="pt-2 flex justify-center">
          <router-link
            to="/"
            class="px-8 py-4 rounded-2xl font-bold text-sm text-white bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 shadow-xl shadow-cyan-500/25 hover:scale-105 active:scale-95 transition-all inline-flex items-center space-x-2"
          >
            <span>← 返回招生官網驗收全域效果</span>
          </router-link>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useThemeStore, type NavbarStyleType, type GlowMotionPreset } from '@/stores/useThemeStore'
import { useSeoMeta } from '@/composables/useSeoMeta'

useSeoMeta({
  title: 'Kaifu 視覺與動效實驗室',
  robots: 'noindex, nofollow',
  canonicalPath: '/kaifu-lab'
})

const store = useThemeStore()

const navbarStyles: { id: NavbarStyleType; name: string; tagline: string; icon: string }[] = [
  { id: 'smart_morph', name: '方案 1: 雙態智能變形 × 能量雷射光軌 (旗艦基準)', tagline: '置頂 100% 滿版通透 ➔ 滾動絲滑收縮圓角膠囊 ＋ 頂部天幕消隱', icon: '💎' },
  { id: 'full_autohide', name: '方案 2: 滿版全景 × 底部神祕光刃 (滿版常駐)', tagline: '全程 100% 滿版大氣常駐 ＋ 底部非線性微型流星由左至右穿梭', icon: '🌊' },
]

const currentNavbarInfo = computed(() => {
  const opt = navbarStyles.find(s => s.id === store.activeNavbarStyle)
  return opt || navbarStyles[0]
})

const glowPresets: {
  id: GlowMotionPreset;
  name: string;
  tagline: string;
  icon: string;
  badge: string;
  duration: string;
  easing: string;
  dutyCycle: string;
  description: string;
}[] = [
  {
    id: 'cosmic_pulse',
    name: '方案 A【靈動星際流星 (Cosmic Pulse)】',
    tagline: '非對稱疾速穿梭 ➔ 柔和拖尾 ➔ 4.5s 深沉暗態留白呼吸',
    icon: '🌠',
    badge: '👑 大師強烈推薦・旗艦首選',
    duration: '8.0s (穿梭 3.5s + 留白 4.5s)',
    easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
    dutyCycle: '44% 行進 / 56% 靜默呼吸',
    description: '打破 linear 機械勻速感，賦予光芒蓄勢破空與優雅減速的流星生命感。長達 4.5 秒的靜息留白營造崇高的神秘感與期待感，天地對位交錯 2.4 秒。'
  },
  {
    id: 'gentle_aurora',
    name: '方案 B【柔和悠揚極光 (Gentle Aurora)】',
    tagline: '10s 溫柔平滑往返 Ping-Pong，兩端微停頓柔焦撫過',
    icon: '🌌',
    badge: '🌿 平穩寧靜・沉浸閱讀',
    duration: '10.0s (左右平滑往返)',
    easing: 'cubic-bezier(0.45, 0.05, 0.55, 0.95)',
    dutyCycle: '100% 柔和常在 (無完全熄滅)',
    description: '經典正弦波平滑來回撫動，光芒在端點處溫和放慢駐留 0.8 秒，如北極光在天際漫漫舒展，極度安撫視覺，適合長時間專注文檔閱讀。'
  },
  {
    id: 'quantum_radar',
    name: '方案 C【量子雷達巡航 (Quantum Radar)】',
    tagline: '5s 週期單向高速巡弋，1.2s 短暫暗態蓄能脈衝',
    icon: '⚡',
    badge: '🚀 科技感十足・敏捷銳利',
    duration: '5.0s (巡航 3.8s + 蓄能 1.2s)',
    easing: 'cubic-bezier(0.25, 0.1, 0.25, 1)',
    dutyCycle: '76% 巡弋 / 24% 蓄能',
    description: '節奏明快的高動量掃描線，模擬量子雷達巡航波，光芒穿透力強，自帶高飽和科技光暈，展現極致運算性能與敏捷活力。'
  },
  {
    id: 'hyperdrive_warp',
    name: '方案 D【深空星芒脈衝 (Hyperdrive Warp)】',
    tagline: '1.8s 曲速光束掠過，5.2s 冷卻蓄能深空夜色',
    icon: '💫',
    badge: '🛸 瞬態躍遷・超時空感',
    duration: '7.0s (躍遷 1.8s + 冷卻 5.2s)',
    easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
    dutyCycle: '26% 躍遷 / 74% 深邃黑夜',
    description: '靈感來自科幻曲速引擎（Warp Drive），極短時間內以超高速閃耀劃過視窗並伴隨光學拉伸，隨後進入超長深空靜息，戲劇張力拉滿。'
  }
]

const currentGlowInfo = computed(() => {
  const opt = glowPresets.find(g => g.id === store.activeGlowPreset)
  return opt || glowPresets[0]
})

const speedOptions = [
  { label: '0.5x (慢速微觀)', value: 0.5 },
  { label: '0.75x (悠閒節奏)', value: 0.75 },
  { label: '1.0x (標準黃金)', value: 1.0 },
  { label: '1.25x (輕快躍動)', value: 1.25 },
  { label: '1.5x (敏捷雷射)', value: 1.5 },
  { label: '2.0x (疾速穿梭)', value: 2.0 }
]
</script>

