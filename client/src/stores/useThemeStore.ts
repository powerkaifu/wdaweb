import { defineStore } from 'pinia'
import { ref } from 'vue'

export type NavbarStyleType = 'smart_morph' | 'full_autohide'
export type GlowMotionPreset = 'cosmic_pulse' | 'gentle_aurora' | 'quantum_radar' | 'hyperdrive_warp'

export interface NebulaFeatures {
  mouseParallax: boolean
  filamentNoise: boolean
  entangledPulse: boolean
  scrollWarp: boolean
}

export interface MeteorConfig {
  enabled: boolean
  mode: 'sporadic' | 'shower' | 'fireball'
  direction: 'omnidirectional' | 'radiant' | 'diagonal'
  fireballChance: number
  codeMeteorChance: number
  manualTriggerCount: number
  manualTriggerCodeCount: number
}

export interface SynapticConfig {
  enabled: boolean
  interactiveCursor: boolean
  autonomousPulse: boolean
  manualPulseCount: number
}

const NAVBAR_STYLE_KEY = 'wda_navbar_style'
const GLOW_PRESET_KEY = 'wda_glow_preset'
const GLOW_SPEED_KEY = 'wda_glow_speed'

/**
 * 全站主題與 3D 視覺特效狀態 Store
 * 遵循 SoC 與 SRP 原則，將視覺動態參數、星空粒子與導覽列風格與 CMS 資料層徹底分離
 */
export const useThemeStore = defineStore('theme', () => {
  // 1. 全站導覽列風格狀態 (2 種風格隨時切換並持久化)
  const savedNavbarStyle = (localStorage.getItem(NAVBAR_STYLE_KEY) as NavbarStyleType) || 'smart_morph'
  const activeNavbarStyle = ref<NavbarStyleType>(savedNavbarStyle)

  function setNavbarStyle(style: NavbarStyleType) {
    activeNavbarStyle.value = style
    try {
      localStorage.setItem(NAVBAR_STYLE_KEY, style)
    } catch (e) {}
  }

  // 2. 全站邊框光芒動效風格 (4 大頂級動態物理預設 + 速度乘數)
  const savedGlowPreset = (localStorage.getItem(GLOW_PRESET_KEY) as GlowMotionPreset) || 'cosmic_pulse'
  const activeGlowPreset = ref<GlowMotionPreset>(savedGlowPreset)

  const savedGlowSpeed = parseFloat(localStorage.getItem(GLOW_SPEED_KEY) || '1.0')
  const glowSpeedMultiplier = ref<number>(isNaN(savedGlowSpeed) ? 1.0 : savedGlowSpeed)

  function applyGlowSpeedCssVar(multiplier: number) {
    if (typeof document !== 'undefined') {
      document.documentElement.style.setProperty('--glow-speed-mult', String(multiplier))
    }
  }

  // 立即套用持久化之速度係數到 CSS 變數
  applyGlowSpeedCssVar(glowSpeedMultiplier.value)

  function setGlowPreset(preset: GlowMotionPreset) {
    activeGlowPreset.value = preset
    try {
      localStorage.setItem(GLOW_PRESET_KEY, preset)
    } catch (e) {}
  }

  function setGlowSpeedMultiplier(multiplier: number) {
    glowSpeedMultiplier.value = multiplier
    applyGlowSpeedCssVar(multiplier)
    try {
      localStorage.setItem(GLOW_SPEED_KEY, String(multiplier))
    } catch (e) {}
  }

  // 3. 3D 宇宙深空星雲與微塵 4 大核心物理特性開關
  const nebulaFeatures = ref<NebulaFeatures>({
    mouseParallax: true,    // 1. 游標引力透鏡視差
    filamentNoise: true,    // 2. 絲狀雲氣纖維紋理
    entangledPulse: true,   // 3. 引力波能量交織呼吸
    scrollWarp: false,      // 4. 滾動深空穿梭推進 (已停用，保持閱讀平穩舒適)
  })

  // 4. Awwwards 級 360° 天球仰望偶發流星物理系統 (支援火流星與幽靈代碼流星彩蛋)
  const meteorConfig = ref<MeteorConfig>({
    enabled: true,
    mode: 'sporadic',       // 'sporadic' (8~22s 偶發) | 'shower' (2~5s 流星雨) | 'fireball' (純火流星)
    direction: 'omnidirectional', // 'omnidirectional' (360° 四面八方) | 'radiant' (天頂向外放射) | 'diagonal' (經典斜掠)
    fireballChance: 0.20,   // 20% 機率微爆火流星
    codeMeteorChance: 0.35, // 35% 機率觸發「幽靈代碼流星」彩蛋
    manualTriggerCount: 0,  // 手動立即發射一般流星計數器
    manualTriggerCodeCount: 0 // 手動立即發射代碼流星計數器
  })

  // 5. 🧠 AI 神經突觸星空網絡 (Synaptic Constellation Network)
  const synapticConfig = ref<SynapticConfig>({
    enabled: true,           // 總開關
    interactiveCursor: true, // 游標引力神經突觸連線
    autonomousPulse: true,   // 宇宙深空自發性思維脈衝
    manualPulseCount: 0      // 手動激發神經脈衝計數器
  })

  function triggerMeteor() {
    meteorConfig.value.manualTriggerCount++
  }

  function triggerCodeMeteor() {
    meteorConfig.value.manualTriggerCodeCount++
  }

  function triggerSynapticPulse() {
    synapticConfig.value.manualPulseCount++
  }

  function setMeteorMode(mode: 'sporadic' | 'shower' | 'fireball') {
    meteorConfig.value.mode = mode
  }

  function setMeteorDirection(dir: 'omnidirectional' | 'radiant' | 'diagonal') {
    meteorConfig.value.direction = dir
  }

  return {
    activeNavbarStyle,
    setNavbarStyle,
    activeGlowPreset,
    glowSpeedMultiplier,
    setGlowPreset,
    setGlowSpeedMultiplier,
    nebulaFeatures,
    meteorConfig,
    synapticConfig,
    triggerMeteor,
    triggerCodeMeteor,
    triggerSynapticPulse,
    setMeteorMode,
    setMeteorDirection,
  }
})
