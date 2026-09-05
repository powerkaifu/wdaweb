<template>
  <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden select-none">
    <!-- 1. 底層 WebGL 3D 宇宙星雲與恆星微粒 -->
    <canvas ref="canvasRef" class="w-full h-full block absolute inset-0"></canvas>
    <!-- 2. 頂層 Awwwards 級 360° 天球仰望偶發流星光學層 -->
    <canvas ref="meteorCanvasRef" class="w-full h-full block absolute inset-0 pointer-events-none"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'
import { useThemeStore } from '@/stores/useThemeStore'

const canvasRef = ref<HTMLCanvasElement | null>(null)
const meteorCanvasRef = ref<HTMLCanvasElement | null>(null)
const store = useThemeStore()

// Three.js 核心實例
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let renderer: THREE.WebGLRenderer | null = null
let clock: THREE.Clock | null = null
let animId: number | null = null

// 當前啟用的 3D 物件群組與更新函式
let currentModeGroup: THREE.Group | null = null
let currentUpdateFn: ((delta: number, elapsedTime: number) => void) | null = null

// 貼圖快取
let nebulaTexture: THREE.CanvasTexture | null = null
let starTexture: THREE.CanvasTexture | null = null
let starShaderMaterial: THREE.ShaderMaterial | null = null

// 互動感測狀態
let targetMouseX = 0
let targetMouseY = 0
let currentMouseX = 0
let currentMouseY = 0

// 📱 裝置性能感知、智慧動態降級與省電休眠狀態 (Mobile Zero-Jank & Power Shield)
let isMobileDevice = false
let prefersReducedMotion = false
let isPageHidden = false

function updateDeviceCapabilities() {
  if (typeof window === 'undefined') return
  isMobileDevice = window.innerWidth < 768 || /Android|iPhone|iPad|iPod/i.test(navigator.userAgent)
  prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
}

// 動態計算最適 DPR：桌機維持 2.0，手機端限制 1.0 ~ 1.25（大幅減省 75% 像素寫入開銷，消除 GPU 頻寬瓶頸）
function getOptimalDpr(): number {
  const rawDpr = window.devicePixelRatio || 1
  return isMobileDevice ? Math.min(rawDpr, 1.25) : Math.min(rawDpr, 2.0)
}

// ===========================================================================
// 🌠 Awwwards 級 360° 天球仰望偶發流星物理系統 (Celestial Sporadic Meteor Engine)
// ===========================================================================
interface MeteorSpark {
  x: number
  y: number
  vx: number
  vy: number
  alpha: number
  decay: number
  size: number
  color: string
}

interface MeteorAfterglowSegment {
  x: number
  y: number
  width: number
  alpha: number
  decay: number
  color: string
}

interface CelestialMeteor {
  x: number
  y: number
  startX: number
  startY: number
  prevX: number
  prevY: number
  angle: number
  speed: number
  length: number
  currentLength: number
  colorScheme: {
    core: string
    glow: string
    outer: string
    accent: string
  }
  isFireball: boolean
  isCodeMeteor: boolean
  hasExploded: boolean
  flareAlpha: number
  flareRadius: number
  age: number
  duration: number
  dead: boolean
}

// ===========================================================================
// 👾 幽靈代碼流星彩蛋 (Cyber Matrix Code-Meteor)
// ===========================================================================
interface CodeDust {
  x: number
  y: number
  vx: number
  vy: number
  text: string
  alpha: number
  decay: number
  color: string
  size: number
}

interface CodeSymbolItem {
  text: string
  color: string
  category: 'frontend' | 'backend' | 'database' | 'ai' | 'milestone'
}

const CODE_SYMBOLS: CodeSymbolItem[] = [
  // 💻 前端網頁技術 (Frontend)
  { text: '<Vue/>', color: '#4ade80', category: 'frontend' },
  { text: 'JavaScript', color: '#facc15', category: 'frontend' },
  { text: 'HTML5', color: '#fb923c', category: 'frontend' },
  { text: 'CSS3', color: '#38bdf8', category: 'frontend' },
  { text: 'Pinia', color: '#fde047', category: 'frontend' },
  { text: 'Bootstrap', color: '#c084fc', category: 'frontend' },

  // ⚙️ 後端開發與執行環境 (Backend)
  { text: 'Node.js', color: '#22c55e', category: 'backend' },
  { text: 'Express', color: '#94a3b8', category: 'backend' },
  { text: 'REST API', color: '#38bdf8', category: 'backend' },
  { text: 'Axios', color: '#818cf8', category: 'backend' },
  { text: 'NPM', color: '#f87171', category: 'backend' },

  // 🗄️ 資料庫 (Database - 專屬 MongoDB NoSQL)
  { text: 'MongoDB', color: '#10b981', category: 'database' },
  { text: 'NoSQL', color: '#34d399', category: 'database' },
  { text: 'JSON', color: '#fbbf24', category: 'database' },
  { text: 'CRUD', color: '#2dd4bf', category: 'database' },

  // 🧠 AI 與智慧應用 (AI)
  { text: 'AI', color: '#f472b6', category: 'ai' },
  { text: 'GenAI', color: '#fb7185', category: 'ai' },
  { text: 'Prompt', color: '#22d3ee', category: 'ai' },
  { text: 'Agent', color: '#e879f9', category: 'ai' },

  // 🏅 職訓精神里程碑
  { text: '920h', color: '#ffffff', category: 'milestone' }
]

let activeCodeDusts: CodeDust[] = []
let lastMeteorCodeTriggerCount = 0

// ===========================================================================
// 🧠 宇宙深空量子思維漣漪 (Quantum Mind Waves) - 純光環擴散，無任何直線連線
// ===========================================================================
interface NeuralFlashWave {
  x: number
  y: number
  radius: number
  maxRadius: number
  alpha: number
  decay: number
  speed: number
  color: string
  hasSecondaryRing: boolean
}

let activeFlashWaves: NeuralFlashWave[] = []
let nextAutonomousFlashCountdown = 3.6 // 🌟 進站 3.6 秒首發量子思維漣漪 (緊接 2.2s 代碼流星後)
let lastManualPulseCount = 0

let meteorCtx: CanvasRenderingContext2D | null = null
let activeMeteors: CelestialMeteor[] = []
let activeSparks: MeteorSpark[] = []
let activeAfterglows: MeteorAfterglowSegment[] = []
let nextMeteorCountdown = 2.2 // 🌟 進站 2.2 秒首發歡迎禮
let hasSpawnedWelcomeMeteor = false
let lastMeteorTriggerCount = 0

const METEOR_PALETTES = [
  {
    name: 'cyan_plasma',
    core: '#ffffff',
    glow: 'rgba(34, 211, 238, 0.95)',
    outer: 'rgba(59, 130, 246, 0.40)',
    accent: '#22d3ee'
  },
  {
    name: 'violet_aurora',
    core: '#ffffff',
    glow: 'rgba(192, 132, 252, 0.95)',
    outer: 'rgba(147, 51, 234, 0.35)',
    accent: '#c084fc'
  },
  {
    name: 'bolide_gold',
    core: '#ffffff',
    glow: 'rgba(253, 224, 71, 0.95)',
    outer: 'rgba(249, 115, 22, 0.40)',
    accent: '#fde047'
  },
  {
    name: 'diamond_white',
    core: '#ffffff',
    glow: 'rgba(224, 242, 254, 0.90)',
    outer: 'rgba(56, 189, 248, 0.30)',
    accent: '#e0f2fe'
  },
  {
    name: 'cyber_matrix',
    core: '#ffffff',
    glow: 'rgba(52, 211, 153, 0.95)',
    outer: 'rgba(6, 182, 212, 0.40)',
    accent: '#34d399'
  }
]

function spawnMeteor(forceFireball = false, forceCode = false) {
  if (!meteorCanvasRef.value) return
  const w = meteorCanvasRef.value.width || window.innerWidth
  const h = meteorCanvasRef.value.height || window.innerHeight

  const dirMode = store.meteorConfig.direction
  let startX = 0
  let startY = 0
  let angle = 0

  if (dirMode === 'radiant') {
    startX = w * 0.5 + (Math.random() - 0.5) * (w * 0.2)
    startY = h * 0.4 + (Math.random() - 0.5) * (h * 0.2)
    angle = Math.random() * Math.PI * 2
  } else if (dirMode === 'diagonal') {
    startX = Math.random() * w * 0.8 + w * 0.2
    startY = -40
    angle = Math.PI * 0.75 + (Math.random() - 0.5) * 0.35
  } else {
    const side = Math.random()
    if (side < 0.35) {
      startX = Math.random() * w
      startY = -30
      angle = Math.PI * 0.25 + Math.random() * Math.PI * 0.50
    } else if (side < 0.60) {
      startX = Math.random() * w
      startY = h + 30
      angle = Math.PI * 1.25 + Math.random() * Math.PI * 0.50
    } else if (side < 0.80) {
      startX = -30
      startY = Math.random() * h
      angle = (Math.random() - 0.5) * (Math.PI * 0.60)
    } else if (side < 0.95) {
      startX = w + 30
      startY = Math.random() * h
      angle = Math.PI + (Math.random() - 0.5) * (Math.PI * 0.60)
    } else {
      startX = w * 0.3 + Math.random() * w * 0.4
      startY = h * 0.3 + Math.random() * h * 0.4
      angle = Math.random() * Math.PI * 2
    }
  }

  const isFireball = !forceCode && (forceFireball || store.meteorConfig.mode === 'fireball' || Math.random() < store.meteorConfig.fireballChance)
  const isCodeMeteor = forceCode || (!isFireball && Math.random() < store.meteorConfig.codeMeteorChance)

  let palette = METEOR_PALETTES[Math.floor(Math.random() * 4)]
  if (isFireball) {
    palette = METEOR_PALETTES[2] // bolide_gold
  } else if (isCodeMeteor) {
    palette = METEOR_PALETTES[4] // cyber_matrix
  }

  const speed = isFireball
    ? 850 + Math.random() * 450
    : isCodeMeteor
      ? 1500 + Math.random() * 600
      : 1400 + Math.random() * 900

  const length = isFireball
    ? 240 + Math.random() * 200
    : isCodeMeteor
      ? 210 + Math.random() * 160
      : 140 + Math.random() * 160

  const travelDistance = Math.sqrt(w * w + h * h) * (0.45 + Math.random() * 0.40)
  const duration = travelDistance / speed

  const meteor: CelestialMeteor = {
    x: startX,
    y: startY,
    startX,
    startY,
    prevX: startX,
    prevY: startY,
    angle,
    speed,
    length,
    currentLength: 0,
    colorScheme: palette,
    isFireball,
    isCodeMeteor,
    hasExploded: false,
    flareAlpha: 0,
    flareRadius: 0,
    age: 0,
    duration: Math.max(0.45, Math.min(1.4, duration)),
    dead: false
  }

  activeMeteors.push(meteor)
}

/**
 * 💡 生成 3D 柔焦星雲 Sprite 專用徑向羽化貼圖 (支援絲狀纖維噪點紋理)
 */
function getOrCreateNebulaTexture(): THREE.CanvasTexture {
  if (nebulaTexture) return nebulaTexture

  const size = 512
  const canvas = document.createElement('canvas')
  canvas.width = size
  canvas.height = size
  const ctx = canvas.getContext('2d')!

  const center = size / 2

  // 1. 底層徑向光學柔焦羽化
  const grad = ctx.createRadialGradient(center, center, 0, center, center, center)
  grad.addColorStop(0, 'rgba(255, 255, 255, 0.85)')
  grad.addColorStop(0.20, 'rgba(255, 255, 255, 0.55)')
  grad.addColorStop(0.48, 'rgba(255, 255, 255, 0.18)')
  grad.addColorStop(0.78, 'rgba(255, 255, 255, 0.03)')
  grad.addColorStop(1, 'rgba(0, 0, 0, 0.0)')

  ctx.fillStyle = grad
  ctx.beginPath()
  ctx.arc(center, center, center, 0, Math.PI * 2)
  ctx.fill()

  // 2. 注入多層微細絲狀雲氣擾動紋理 (Filament Noise)
  const imgData = ctx.getImageData(0, 0, size, size)
  const data = imgData.data

  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      const idx = (y * size + x) * 4
      const alpha = data[idx + 3]
      if (alpha > 5) {
        const nx = x / size * 8.0
        const ny = y / size * 8.0
        const noise = Math.sin(nx * 3.5 + Math.cos(ny * 2.5)) * Math.cos(ny * 4.0 - Math.sin(nx * 2.0))
        const modulation = 1.0 + noise * 0.18
        data[idx + 3] = Math.min(255, Math.max(0, alpha * modulation))
      }
    }
  }
  ctx.putImageData(imgData, 0, 0)

  nebulaTexture = new THREE.CanvasTexture(canvas)
  nebulaTexture.needsUpdate = true
  return nebulaTexture
}

/**
 * ✨ 生成真實天體光學恆星光暈貼圖 (64x64 精緻纖細鑽石十字光刺、微型飽和白核與柔和色溫光暈)
 */
function getOrCreateStarTexture(): THREE.CanvasTexture {
  if (starTexture) return starTexture

  const size = 64
  const canvas = document.createElement('canvas')
  canvas.width = size
  canvas.height = size
  const ctx = canvas.getContext('2d')!

  const center = size / 2

  // 1. 底層精巧色溫柔焦光暈 (Subtle Cyan-Blue Halo)
  const outerGrad = ctx.createRadialGradient(center, center, 0, center, center, 14)
  outerGrad.addColorStop(0, 'rgba(255, 255, 255, 0.95)')
  outerGrad.addColorStop(0.25, 'rgba(165, 243, 252, 0.65)') // 鑽石青藍色溫
  outerGrad.addColorStop(0.60, 'rgba(56, 189, 248, 0.20)')
  outerGrad.addColorStop(1, 'rgba(0, 0, 0, 0)')

  ctx.fillStyle = outerGrad
  ctx.beginPath()
  ctx.arc(center, center, 14, 0, Math.PI * 2)
  ctx.fill()

  // 2. 45 度次級微星芒 (Diagonal Micro Rays)
  ctx.save()
  ctx.translate(center, center)
  ctx.rotate(Math.PI / 4)
  ctx.strokeStyle = 'rgba(224, 242, 254, 0.45)'
  ctx.lineWidth = 0.6
  ctx.beginPath()
  ctx.moveTo(-10, 0)
  ctx.lineTo(10, 0)
  ctx.moveTo(0, -10)
  ctx.lineTo(0, 10)
  ctx.stroke()
  ctx.restore()

  // 3. 水平與垂直主軸針尖級尖銳十字星芒 (Needle-Sharp Diffraction Spikes)
  const drawSpike = (angle: number) => {
    ctx.save()
    ctx.translate(center, center)
    ctx.rotate(angle)

    ctx.beginPath()
    ctx.moveTo(0, -0.8)
    ctx.lineTo(24, 0)
    ctx.lineTo(0, 0.8)
    ctx.lineTo(-24, 0)
    ctx.closePath()

    const spikeGrad = ctx.createRadialGradient(0, 0, 0, 0, 0, 24)
    spikeGrad.addColorStop(0, 'rgba(255, 255, 255, 1.0)')
    spikeGrad.addColorStop(0.35, 'rgba(224, 242, 254, 0.80)')
    spikeGrad.addColorStop(0.70, 'rgba(56, 189, 248, 0.25)')
    spikeGrad.addColorStop(1, 'rgba(6, 182, 212, 0)')
    ctx.fillStyle = spikeGrad
    ctx.fill()
    ctx.restore()
  }

  // 繪製纖細銳利的主十字星芒
  drawSpike(0)
  drawSpike(Math.PI / 2)

  // 4. 超高亮度針尖高能白核 (Pinpoint 100% White Core)
  const coreGrad = ctx.createRadialGradient(center, center, 0, center, center, 3)
  coreGrad.addColorStop(0, 'rgba(255, 255, 255, 1.0)')
  coreGrad.addColorStop(0.70, 'rgba(255, 255, 255, 0.95)')
  coreGrad.addColorStop(1, 'rgba(224, 242, 254, 0)')

  ctx.fillStyle = coreGrad
  ctx.beginPath()
  ctx.arc(center, center, 3, 0, Math.PI * 2)
  ctx.fill()

  starTexture = new THREE.CanvasTexture(canvas)
  starTexture.needsUpdate = true
  return starTexture
}

function disposeObject(obj: THREE.Object3D) {
  obj.traverse((child) => {
    if (child instanceof THREE.Mesh || child instanceof THREE.Points || child instanceof THREE.Sprite) {
      if (child.geometry) {
        child.geometry.dispose()
      }
      if (child.material) {
        if (Array.isArray(child.material)) {
          child.material.forEach((m) => m.dispose())
        } else {
          child.material.dispose()
        }
      }
    }
  })
}

function clearCurrentScene() {
  if (currentModeGroup && scene) {
    scene.remove(currentModeGroup)
    disposeObject(currentModeGroup)
    currentModeGroup = null
  }
  starShaderMaterial = null
  currentUpdateFn = null
}

// ---------------------------------------------------------------------------
// 🌌 全域旗艦：【3D 宇宙深空流動星雲與銀河星空 (3D Nebula & Milky Way Stars)】
// ---------------------------------------------------------------------------
function initNebulaFlowScene() {
  if (!scene) return
  clearCurrentScene()

  const group = new THREE.Group()
  const nTex = getOrCreateNebulaTexture()
  const sTex = getOrCreateStarTexture()

  // 1. 建立 5 大 3D 柔焦星雲 Sprite 氣團 (加速流動 + 旋轉 + 呼吸擴散 + 引力波互補)
  const nebulaConfigs = [
    {
      color: new THREE.Color('#06b6d4'), // 電光青雲氣 (主視覺)
      baseX: -14,
      baseY: 7,
      baseZ: -18,
      scale: 58,
      driftRadiusX: 16.0,
      driftRadiusY: 10.0,
      driftRadiusZ: 6.5,
      speed: 0.28,
      phase: 0.0,
      baseOpacity: 0.20,
      pulseSpeed: 0.45,
      parallaxWeight: 1.1
    },
    {
      color: new THREE.Color('#3b82f6'), // 科技蔚藍雲氣
      baseX: 16,
      baseY: -7,
      baseZ: -26,
      scale: 66,
      driftRadiusX: 18.5,
      driftRadiusY: 11.5,
      driftRadiusZ: 8.0,
      speed: 0.24,
      phase: 1.25, // 引力波能量交織相差
      baseOpacity: 0.22,
      pulseSpeed: 0.38,
      parallaxWeight: 0.7
    },
    {
      color: new THREE.Color('#8b5cf6'), // 夢幻紫晶雲氣
      baseX: 8,
      baseY: 10,
      baseZ: -14,
      scale: 52,
      driftRadiusX: 14.5,
      driftRadiusY: 9.0,
      driftRadiusZ: 6.0,
      speed: 0.32,
      phase: 2.50, // 引力波能量交織相差
      baseOpacity: 0.18,
      pulseSpeed: 0.50,
      parallaxWeight: 1.3
    },
    {
      color: new THREE.Color('#0284c7'), // 深邃海洋深藍
      baseX: -12,
      baseY: -10,
      baseZ: -32,
      scale: 70,
      driftRadiusX: 20.0,
      driftRadiusY: 12.0,
      driftRadiusZ: 9.0,
      speed: 0.22,
      phase: 3.75, // 引力波能量交織相差
      baseOpacity: 0.19,
      pulseSpeed: 0.35,
      parallaxWeight: 0.5
    },
    {
      color: new THREE.Color('#a855f7'), // 紫霞高能氣團 (近景流動)
      baseX: 0,
      baseY: 2,
      baseZ: -9,
      scale: 46,
      driftRadiusX: 13.0,
      driftRadiusY: 8.0,
      driftRadiusZ: 5.0,
      speed: 0.35,
      phase: 5.0, // 引力波能量交織相差
      baseOpacity: 0.16,
      pulseSpeed: 0.55,
      parallaxWeight: 1.6
    }
  ]

  interface NebulaSpriteRuntime {
    sprite: THREE.Sprite
    material: THREE.SpriteMaterial
    config: typeof nebulaConfigs[0]
  }
  const spritesRuntime: NebulaSpriteRuntime[] = []

  nebulaConfigs.forEach((cfg) => {
    const mat = new THREE.SpriteMaterial({
      map: nTex,
      color: cfg.color,
      transparent: true,
      opacity: cfg.baseOpacity,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    })
    const sprite = new THREE.Sprite(mat)
    sprite.scale.set(cfg.scale, cfg.scale, 1)
    sprite.position.set(cfg.baseX, cfg.baseY, cfg.baseZ)
    group.add(sprite)

    spritesRuntime.push({ sprite, material: mat, config: cfg })
  })

  // 2. 建立自然銀河繁星 (Three-Tier Stellar Magnitudes + GPU 原生非同步物理閃爍)
  // 桌機維持 960 顆三階繁星；手機端自適應精簡為 360 顆（保證璀璨星空美感，頂點運算減少 62%）
  const starCount = isMobileDevice ? 360 : 960
  const starGeometry = new THREE.BufferGeometry()
  const starPositions = new Float32Array(starCount * 3)
  const starColors = new Float32Array(starCount * 3)
  const starScales = new Float32Array(starCount)
  const starBaseBrightness = new Float32Array(starCount)
  const starPhases = new Float32Array(starCount)
  const starSpeeds = new Float32Array(starCount)
  const starTwinkleStrengths = new Float32Array(starCount)
  const starParallaxes = new Float32Array(starCount)

  // 三階天體光學色溫調色板
  const colorBrightWhite = new THREE.Color('#ffffff') // 純淨高能亮核白
  const colorCyan = new THREE.Color('#a5f3fc')        // 科技鑽石青藍
  const colorPurple = new THREE.Color('#f3e8ff')      // 溫潤紫晶微星

  for (let i = 0; i < starCount; i++) {
    const i3 = i * 3
    let x = 0
    let y = 0
    let z = 0

    let scale = 1.0
    let baseBrightness = 0.7
    let speed = 1.0
    let twinkleStrength = 0.5
    let parallax = 0.35
    let c = colorBrightWhite

    if (i < 64) {
      // 🌟 【Tier 1：64 顆璀璨一等星 (Bright Stellar Beacons)】
      // 分佈於中近景醒目視野，一眼可見光芒四射的鑽石十字光刺
      const isArmBeacon = i < 40
      if (isArmBeacon) {
        // 沿著主星河高光帶排布
        const t = (Math.random() - 0.5) * 80
        const armCurve = t * 0.40 + Math.sin(t * 0.08) * 6.0
        x = t + (Math.random() - 0.5) * 8.0
        y = armCurve + (Math.random() - 0.5) * 6.0
        z = -14 - Math.random() * 14 // 較近的景深 (-14 ~ -28)
      } else {
        // 醒目散落於兩側深空天幕
        x = (Math.random() - 0.5) * 88
        y = (Math.random() - 0.5) * 58
        z = -15 - Math.random() * 15
      }

      scale = 1.05 + Math.random() * 0.35 // 1.05 ~ 1.40 精巧鑽石一等星尺寸
      baseBrightness = 1.05 + Math.random() * 0.25 // 1.05 ~ 1.30 飽和高光
      speed = 1.3 + Math.random() * 1.7 // 靈動呼吸頻率
      twinkleStrength = 0.70 + Math.random() * 0.35 // 0.70 ~ 1.05 大幅度閃爍，波峰觸發 HDR 溢光
      parallax = 0.45 + Math.random() * 0.35 // 近景顯著視差

      c = Math.random() < 0.75 ? colorBrightWhite : colorCyan
    } else if (i < 364) {
      // 🌌 【Tier 2：300 顆中景二等星 (Mid-Magnitude Stars)】
      // 沿銀河旋臂弧線密集分佈，各自獨立眨眼閃爍
      const t = (Math.random() - 0.5) * 90
      const armCurve = t * 0.42 + Math.sin(t * 0.09) * 6.5
      const spread = (Math.random() - 0.5) * (Math.random() * 20 + 6)

      x = t
      y = armCurve + spread
      z = -22 - Math.random() * 20

      scale = 0.50 + Math.random() * 0.25 // 0.50 ~ 0.75 中景靈動二等星
      baseBrightness = 0.80 + Math.random() * 0.25 // 0.80 ~ 1.05
      speed = 0.8 + Math.random() * 1.4
      twinkleStrength = 0.50 + Math.random() * 0.30
      parallax = 0.25 + Math.random() * 0.25

      const rndColor = Math.random()
      if (rndColor < 0.60) c = colorBrightWhite
      else if (rndColor < 0.85) c = colorCyan
      else c = colorPurple
    } else {
      // ✨ 【Tier 3：596 顆銀河深空星塵 (Deep Space Stellar Dust)】
      // 廣域漫佈於深邃背景，微幅平穩閃爍，襯托深邃層次
      x = (Math.random() - 0.5) * 110
      y = (Math.random() - 0.5) * 80
      z = -26 - Math.random() * 34

      scale = 0.22 + Math.random() * 0.16 // 0.22 ~ 0.38 針尖微星星塵
      baseBrightness = 0.55 + Math.random() * 0.25 // 0.55 ~ 0.80 明晰微光
      speed = 0.4 + Math.random() * 0.7
      twinkleStrength = 0.25 + Math.random() * 0.20
      parallax = 0.12 + Math.random() * 0.18

      c = Math.random() < 0.80 ? colorBrightWhite : colorCyan
    }

    starPositions[i3] = x
    starPositions[i3 + 1] = y
    starPositions[i3 + 2] = z

    starColors[i3] = c.r
    starColors[i3 + 1] = c.g
    starColors[i3 + 2] = c.b

    starScales[i] = scale
    starBaseBrightness[i] = baseBrightness
    starPhases[i] = Math.random() * Math.PI * 2 // 獨立隨機初始相位
    starSpeeds[i] = speed
    starTwinkleStrengths[i] = twinkleStrength
    starParallaxes[i] = parallax
  }

  starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3))
  starGeometry.setAttribute('aColor', new THREE.BufferAttribute(starColors, 3))
  starGeometry.setAttribute('aScale', new THREE.BufferAttribute(starScales, 1))
  starGeometry.setAttribute('aBaseBrightness', new THREE.BufferAttribute(starBaseBrightness, 1))
  starGeometry.setAttribute('aPhase', new THREE.BufferAttribute(starPhases, 1))
  starGeometry.setAttribute('aSpeed', new THREE.BufferAttribute(starSpeeds, 1))
  starGeometry.setAttribute('aTwinkleStrength', new THREE.BufferAttribute(starTwinkleStrengths, 1))
  starGeometry.setAttribute('aParallax', new THREE.BufferAttribute(starParallaxes, 1))

  // 🚀 GPU 原生著色器材質 (ShaderMaterial)：非同步物理閃爍 + 光學動態膨脹 + HDR 亮核溢光
  starShaderMaterial = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uMouse: { value: new THREE.Vector2(0, 0) },
      uPixelRatio: { value: Math.min(window.devicePixelRatio, 2) },
      uTexture: { value: sTex },
      uMouseParallax: { value: store.nebulaFeatures.mouseParallax ? 1.0 : 0.0 }
    },
    vertexShader: `
      uniform float uTime;
      uniform vec2 uMouse;
      uniform float uPixelRatio;
      uniform float uMouseParallax;

      attribute vec3 aColor;
      attribute float aScale;
      attribute float aBaseBrightness;
      attribute float aPhase;
      attribute float aSpeed;
      attribute float aTwinkleStrength;
      attribute float aParallax;

      varying vec3 vColor;
      varying float vBrightness;

      void main() {
        vColor = aColor;

        // 1. GPU 原生視差偏移 (零 CPU 耗損)
        vec3 pos = position;
        pos.x += uMouse.x * aParallax * 1.5 * uMouseParallax;
        pos.y += -uMouse.y * aParallax * 1.0 * uMouseParallax;

        // 2. 非同步雙頻物理大氣閃爍波 (複合非週期諧波，模擬真實夜空眨眼)
        float wave1 = sin(uTime * aSpeed + aPhase);
        float wave2 = cos(uTime * aSpeed * 0.618 + aPhase * 1.414);
        float twinkle = wave1 * 0.70 + wave2 * 0.30;

        // 3. 亮度動態計算 (一等星波峰可達 1.45，激發高光 HDR 溢白光核)
        float brightness = clamp(aBaseBrightness + twinkle * aTwinkleStrength, 0.15, 1.45);
        vBrightness = brightness;

        // 4. 動態光學膨脹：亮度增強時，光暈直徑隨之物理擴散
        float dynamicScale = aScale * (0.80 + brightness * 0.35);

        // 5. 投影座標與視距衰減 (保證微米精緻度，一等星約 14px~20px，二等星約 6px~9px，星塵約 2px~4px)
        vec4 mvPosition = modelViewMatrix * vec4(pos, 1.0);
        float dist = max(-mvPosition.z, 1.0);
        gl_PointSize = clamp(dynamicScale * (160.0 / dist) * uPixelRatio, 1.2 * uPixelRatio, 22.0 * uPixelRatio);

        gl_Position = projectionMatrix * mvPosition;
      }
    `,
    fragmentShader: `
      uniform sampler2D uTexture;

      varying vec3 vColor;
      varying float vBrightness;

      void main() {
        vec4 tex = texture2D(uTexture, gl_PointCoord);

        // 1. 基礎天體光學色彩
        vec3 rgb = vColor * tex.rgb * vBrightness;

        // 2. HDR 亮核溢光 (Bloom)：極亮瞬間核心泛白飽和
        if (vBrightness > 1.0) {
          float excess = vBrightness - 1.0;
          rgb += vec3(excess * 0.85);
        }

        // 3. 不透明度平滑過渡
        float alpha = tex.a * clamp(vBrightness * 0.85 + 0.15, 0.20, 1.0);

        gl_FragColor = vec4(rgb, alpha);
      }
    `,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  })

  const starPoints = new THREE.Points(starGeometry, starShaderMaterial)
  group.add(starPoints)

  scene.add(group)
  currentModeGroup = group

  // 3. 逐幀渲染 (4 大核心物理特性協同運算 + GPU 原生星光驅動)
  currentUpdateFn = (delta: number, elapsedTime: number) => {
    // 游標視差平滑阻尼 Lerp
    currentMouseX += (targetMouseX - currentMouseX) * 0.04
    currentMouseY += (targetMouseY - currentMouseY) * 0.04

    // A. 5 大星雲的平滑三維漫游、自轉與引力波交織呼吸
    spritesRuntime.forEach(({ sprite, material, config }) => {
      const t = elapsedTime * config.speed + config.phase

      const driftX = config.baseX + Math.cos(t) * config.driftRadiusX
      const driftY = config.baseY + Math.sin(t * 0.85) * config.driftRadiusY
      const driftZ = config.baseZ + Math.sin(t * 0.6) * config.driftRadiusZ

      // 視差偏移 (若開啟游標引力透鏡)
      const pX = store.nebulaFeatures.mouseParallax ? currentMouseX * config.parallaxWeight * 2.8 : 0
      const pY = store.nebulaFeatures.mouseParallax ? -currentMouseY * config.parallaxWeight * 2.0 : 0

      sprite.position.x = driftX + pX
      sprite.position.y = driftY + pY
      sprite.position.z = driftZ

      // 星雲緩慢自轉 (加強內部氣流旋轉感)
      material.rotation = Math.sin(t * 0.3) * 0.2 + elapsedTime * (config.speed * 0.08)

      // 星雲引力波交織呼吸 (形態有機膨脹收縮)
      const pulsePhase = store.nebulaFeatures.entangledPulse ? config.phase : 0
      const dynamicScale = config.scale * (1 + Math.sin(elapsedTime * config.pulseSpeed + pulsePhase) * 0.12)
      sprite.scale.set(dynamicScale, dynamicScale, 1)

      // 亮度微光呼吸
      material.opacity = config.baseOpacity + Math.sin(elapsedTime * config.pulseSpeed + pulsePhase) * 0.025
    })

    // B. GPU 原生驅動 420 顆繁星非同步閃爍與視差 (零 CPU 迴圈開銷)
    if (starShaderMaterial) {
      starShaderMaterial.uniforms.uTime.value = elapsedTime
      starShaderMaterial.uniforms.uMouse.value.set(currentMouseX, currentMouseY)
      starShaderMaterial.uniforms.uMouseParallax.value = store.nebulaFeatures.mouseParallax ? 1.0 : 0.0
    }
  }
}

// ---------------------------------------------------------------------------
// 🧠 宇宙深空量子思維漣漪演算法 (Quantum Mind Waves Physics) - 大小不固定、多階範圍動態擴散
// ---------------------------------------------------------------------------
function triggerAutonomousFlash(w: number, h: number) {
  // 🌟 動態規模範圍（大小不固定，自適應螢幕）：
  // Tier 1: 小型靈動微光波 (約 35% 機率) -> 半徑 300 ~ 460px，靈巧聚焦
  // Tier 2: 中大型深空脈衝波 (約 45% 機率) -> 半徑 520 ~ 780px，廣域擴散
  // Tier 3: 浩瀚超巨引力波 (約 20% 機率) -> 半徑 850 ~ 1150px，震撼橫跨大半星空！
  const randTier = Math.random()
  let targetMaxRadius: number
  let speed: number
  let decay: number
  let hasSecondaryRing = false

  const minDim = Math.min(w, h)

  if (randTier < 0.35) {
    // 1. 小型靈動微光波
    targetMaxRadius = Math.max(300, minDim * (0.32 + Math.random() * 0.15))
    speed = 190 + Math.random() * 60
    decay = 0.45 + Math.random() * 0.10 // 存活約 1.8~2.0 秒
    hasSecondaryRing = false
  } else if (randTier < 0.80) {
    // 2. 中大型深空脈衝波
    targetMaxRadius = Math.max(520, minDim * (0.55 + Math.random() * 0.22))
    speed = 260 + Math.random() * 80
    decay = 0.32 + Math.random() * 0.08 // 存活約 2.5~2.8 秒
    hasSecondaryRing = Math.random() < 0.65 // 65% 機率帶次級諧振雙環
  } else {
    // 3. 浩瀚超巨型引力波 (橫跨全域深空)
    targetMaxRadius = Math.max(850, minDim * (0.85 + Math.random() * 0.35))
    speed = 340 + Math.random() * 90
    decay = 0.26 + Math.random() * 0.06 // 存活約 3.0~3.5 秒
    hasSecondaryRing = true // 巨波必帶雙環，視覺極具層次深度
  }

  // 隨機微光色彩 (85% 電光青、15% 深空天藍)
  const color = Math.random() < 0.85 ? '#22d3ee' : '#38bdf8'

  activeFlashWaves.push({
    x: w * 0.15 + Math.random() * w * 0.70,
    y: h * 0.15 + Math.random() * h * 0.70,
    radius: 10,
    maxRadius: targetMaxRadius,
    alpha: 0.90,
    decay,
    speed,
    color,
    hasSecondaryRing
  })
}

/**
 * ⚡ 高效能粒子無痛移除輔助函式 (O(1) Swap-and-Pop)
 * 避免 Array.prototype.splice 引發的記憶體搬移與 GC 停頓
 */
function fastRemove<T>(arr: T[], index: number): void {
  const last = arr.pop()!
  if (index < arr.length) {
    arr[index] = last
  }
}

function renderQuantumMindWaves(ctx: CanvasRenderingContext2D, dt: number, w: number, h: number) {
  // 1. 檢查自發性宇宙深空量子思想放電 (約 8~14 秒一次，靈動自然)
  if (store.synapticConfig.autonomousPulse) {
    nextAutonomousFlashCountdown -= dt
    if (nextAutonomousFlashCountdown <= 0) {
      triggerAutonomousFlash(w, h)
      nextAutonomousFlashCountdown = 8.0 + Math.random() * 5.5
    }
  }

  // 2. 檢查手動觸發神經脈衝
  if (store.synapticConfig.manualPulseCount !== lastManualPulseCount) {
    lastManualPulseCount = store.synapticConfig.manualPulseCount
    triggerAutonomousFlash(w, h)
  }

  // 3. 更新並繪製量子思維漣漪光環 (純同心柔焦光環，非線性阻尼擴散 + 漸近羽化消隱)
  for (let i = activeFlashWaves.length - 1; i >= 0; i--) {
    const wave = activeFlashWaves[i]
    const progress = Math.min(1.0, wave.radius / wave.maxRadius)
    
    // 非線性動量衰減：波前起始高速擴散，隨向外擴展平滑減速，還原真實深空引力波能量散逸
    const currentSpeed = wave.speed * Math.max(0.20, 1.0 - progress * 0.75)
    wave.radius += currentSpeed * dt
    wave.alpha -= dt * wave.decay

    // 漸近式邊緣羽化 (Asymptotic Edge Feathering)：保證半徑逼近 maxRadius 時 alpha 完美歸零，徹底杜絕突兀消失截斷
    const edgeFade = 1.0 - Math.pow(progress, 1.4)
    const currentAlpha = Math.max(0, wave.alpha * edgeFade)

    if (wave.alpha <= 0 || progress >= 1.0 || currentAlpha <= 0.003) {
      fastRemove(activeFlashWaves, i)
      continue
    }

    ctx.save()
    // A. 主光環
    ctx.beginPath()
    ctx.arc(wave.x, wave.y, wave.radius, 0, Math.PI * 2)
    ctx.strokeStyle = wave.color === '#22d3ee'
      ? `rgba(34, 211, 238, ${(currentAlpha * 0.28).toFixed(3)})`
      : `rgba(56, 189, 248, ${(currentAlpha * 0.28).toFixed(3)})`
    ctx.lineWidth = Math.max(0.8, 1.8 - progress * 0.9)
    if (!isMobileDevice) {
      ctx.shadowColor = wave.color
      ctx.shadowBlur = 10 + progress * 12
    }
    ctx.stroke()

    // B. 次級諧振雙環 (波幅緊湊伴隨，間距自適應微調；手機端跳過以節省 GPU 算力)
    if (!isMobileDevice && wave.hasSecondaryRing && wave.radius > 35) {
      const secondaryRadius = Math.max(10, wave.radius - Math.min(22, Math.max(5, wave.radius * 0.065)))
      ctx.beginPath()
      ctx.arc(wave.x, wave.y, secondaryRadius, 0, Math.PI * 2)
      ctx.strokeStyle = `rgba(56, 189, 248, ${(currentAlpha * 0.13).toFixed(3)})`
      ctx.lineWidth = 0.8
      ctx.shadowBlur = 6
      ctx.stroke()
    }
    ctx.restore()
  }
}

// ---------------------------------------------------------------------------
// 🌠 Awwwards 級流星渲染與物理更新 (Sub-Frame Optical Canvas Simulation)
// ---------------------------------------------------------------------------
function updateAndRenderMeteors(dt: number) {
  if (!meteorCtx || !meteorCanvasRef.value) return
  const ctx = meteorCtx
  const dpr = Math.min(window.devicePixelRatio || 1, 2)
  const logicalW = window.innerWidth
  const logicalH = window.innerHeight

  // 物理螢幕 DPI 座標矩陣重置與邏輯視窗尺寸清屏
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  ctx.clearRect(0, 0, logicalW, logicalH)

  // 0. 繪製深空量子思維漣漪光環 (純光環擴散，無任何直線連線干擾)
  if (store.synapticConfig.enabled) {
    renderQuantumMindWaves(ctx, dt, logicalW, logicalH)
  }

  // 1. 檢查常規手動立即觸發
  if (store.meteorConfig.manualTriggerCount !== lastMeteorTriggerCount) {
    lastMeteorTriggerCount = store.meteorConfig.manualTriggerCount
    spawnMeteor()
  }

  // 1.1 檢查幽靈代碼流星手動立即觸發
  if (store.meteorConfig.manualTriggerCodeCount !== lastMeteorCodeTriggerCount) {
    lastMeteorCodeTriggerCount = store.meteorConfig.manualTriggerCodeCount
    spawnMeteor(false, true)
  }

  // 2. 自動隨機排程 (進站首發歡迎禮 + 自然偶發)
  if (store.meteorConfig.enabled) {
    nextMeteorCountdown -= dt
    if (nextMeteorCountdown <= 0) {
      if (!hasSpawnedWelcomeMeteor) {
        hasSpawnedWelcomeMeteor = true
        spawnMeteor(false, true) // 🌟 進站 2.2 秒首發 100% 必定為幽靈代碼流星歡迎禮！
      } else {
        spawnMeteor()
      }

      if (store.meteorConfig.mode === 'shower') {
        // 璀璨流星雨：2 ~ 4 秒一顆
        nextMeteorCountdown = 2.0 + Math.random() * 2.5
      } else {
        // 靜謐自然偶發：6 ~ 14 秒一顆 (搭配 55% 代碼流星機率，平均約 18 秒必定遇見一顆代碼流星)
        nextMeteorCountdown = 6.0 + Math.random() * 8.0
      }
    }
  }

  // 3. 更新並繪製「殘留煙霧痕跡 (Phosphorescent Afterglow)」
  ctx.save()
  ctx.globalCompositeOperation = 'lighter'

  for (let i = activeAfterglows.length - 1; i >= 0; i--) {
    const ag = activeAfterglows[i]
    ag.alpha -= ag.decay * dt
    if (ag.alpha <= 0) {
      fastRemove(activeAfterglows, i)
      continue
    }
    ctx.beginPath()
    ctx.arc(ag.x, ag.y, ag.width, 0, Math.PI * 2)
    ctx.fillStyle = ag.color.replace('ALPHA', String(ag.alpha * 0.12))
    ctx.fill()
  }

  // 4. 更新並繪製「火流星微爆碎屑粒子 (Bolide Sparks)」
  for (let i = activeSparks.length - 1; i >= 0; i--) {
    const s = activeSparks[i]
    s.x += s.vx * dt
    s.y += s.vy * dt
    s.vy += 60 * dt
    s.vx *= 0.96
    s.vy *= 0.96
    s.alpha -= s.decay * dt

    if (s.alpha <= 0) {
      fastRemove(activeSparks, i)
      continue
    }

    ctx.beginPath()
    ctx.arc(s.x, s.y, s.size * s.alpha, 0, Math.PI * 2)
    ctx.fillStyle = s.color.replace('ALPHA', String(s.alpha))
    if (!isMobileDevice) {
      ctx.shadowColor = s.color.replace('ALPHA', '0.8')
      ctx.shadowBlur = 6
    }
    ctx.fill()
  }

  // 4.1 更新並繪製「幽靈代碼流星粒子微塵 (Cyber Code Dust)」
  for (let i = activeCodeDusts.length - 1; i >= 0; i--) {
    const cd = activeCodeDusts[i]
    cd.x += cd.vx * dt
    cd.y += cd.vy * dt
    cd.alpha -= cd.decay * dt

    if (cd.alpha <= 0) {
      fastRemove(activeCodeDusts, i)
      continue
    }

    ctx.save()
    ctx.font = `bold ${Math.round(cd.size)}px "JetBrains Mono", "Fira Code", monospace`
    ctx.fillStyle = cd.color
    ctx.globalAlpha = Math.max(0, Math.min(1, cd.alpha * 0.95))
    if (!isMobileDevice) {
      ctx.shadowColor = cd.color
      ctx.shadowBlur = 8
    }
    ctx.fillText(cd.text, cd.x, cd.y)
    ctx.restore()
  }

  // 5. 更新並繪製「主體流星 (Meteors)」
  for (let i = activeMeteors.length - 1; i >= 0; i--) {
    const m = activeMeteors[i]
    m.age += dt
    const progress = m.age / m.duration

    if (progress >= 1.0) {
      m.dead = true
      fastRemove(activeMeteors, i)
      continue
    }

    const moveStep = m.speed * dt
    m.prevX = m.x
    m.prevY = m.y
    m.x += Math.cos(m.angle) * moveStep
    m.y += Math.sin(m.angle) * moveStep

    if (progress < 0.25) {
      m.currentLength = (progress / 0.25) * m.length
    } else if (progress > 0.75) {
      m.currentLength = ((1.0 - progress) / 0.25) * m.length
    } else {
      m.currentLength = m.length
    }

    const tailX = m.x - Math.cos(m.angle) * m.currentLength
    const tailY = m.y - Math.sin(m.angle) * m.currentLength

    let opacity = 1.0
    if (progress < 0.15) opacity = progress / 0.15
    else if (progress > 0.80) opacity = (1.0 - progress) / 0.20

    // 幽靈代碼流星沿途拋灑發光代碼微塵 (職訓四大技能庫：前端、後端、資料庫、AI)
    if (m.isCodeMeteor && Math.random() < 0.40) {
      const item = CODE_SYMBOLS[Math.floor(Math.random() * CODE_SYMBOLS.length)]
      activeCodeDusts.push({
        x: m.x + (Math.random() - 0.5) * 20,
        y: m.y + (Math.random() - 0.5) * 20,
        vx: (Math.random() - 0.5) * 36 - Math.cos(m.angle) * 35,
        vy: (Math.random() - 0.5) * 36 - Math.sin(m.angle) * 35,
        text: item.text,
        alpha: 1.0,
        decay: 0.70 + Math.random() * 0.50,
        color: item.color,
        size: 11 + Math.random() * 4
      })
    }

    if (Math.random() < 0.40) {
      activeAfterglows.push({
        x: m.x,
        y: m.y,
        width: m.isFireball ? 4.5 : (m.isCodeMeteor ? 3.0 : 2.5),
        alpha: opacity,
        decay: m.isFireball ? 0.65 : 1.1,
        color: m.colorScheme.glow.replace(/[\d\.]+\)$/, 'ALPHA)')
      })
    }

    // 火流星微爆
    if (m.isFireball && !m.hasExploded && progress >= 0.58) {
      m.hasExploded = true
      m.flareAlpha = 1.0
      m.flareRadius = 110

      const sparkCount = 6 + Math.floor(Math.random() * 4)
      for (let s = 0; s < sparkCount; s++) {
        const sparkAngle = m.angle + (Math.random() - 0.5) * Math.PI * 1.2
        const sparkSpeed = 80 + Math.random() * 220
        activeSparks.push({
          x: m.x,
          y: m.y,
          vx: Math.cos(sparkAngle) * sparkSpeed,
          vy: Math.sin(sparkAngle) * sparkSpeed,
          alpha: 1.0,
          decay: 1.8 + Math.random() * 1.5,
          size: 1.2 + Math.random() * 1.8,
          color: m.colorScheme.glow.replace(/[\d\.]+\)$/, 'ALPHA)')
        })
      }
    }

    // Pass 1: 環境微光暈
    const ambientRadius = m.isFireball ? 65 : (m.isCodeMeteor ? 45 : 35)
    const ambGrad = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, ambientRadius)
    ambGrad.addColorStop(0, m.colorScheme.glow.replace(/[\d\.]+\)$/, `${0.45 * opacity})`))
    ambGrad.addColorStop(0.5, m.colorScheme.outer.replace(/[\d\.]+\)$/, `${0.20 * opacity})`))
    ambGrad.addColorStop(1, 'rgba(0, 0, 0, 0)')

    ctx.fillStyle = ambGrad
    ctx.beginPath()
    ctx.arc(m.x, m.y, ambientRadius, 0, Math.PI * 2)
    ctx.fill()

    // Pass 2: 耀斑微爆
    if (m.flareAlpha > 0.01) {
      m.flareAlpha -= dt * 4.5
      const fGrad = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, m.flareRadius)
      fGrad.addColorStop(0, `rgba(255, 255, 255, ${0.95 * m.flareAlpha})`)
      fGrad.addColorStop(0.25, m.colorScheme.glow.replace(/[\d\.]+\)$/, `${0.75 * m.flareAlpha})`))
      fGrad.addColorStop(0.65, m.colorScheme.outer.replace(/[\d\.]+\)$/, `${0.30 * m.flareAlpha})`))
      fGrad.addColorStop(1, 'rgba(0, 0, 0, 0)')

      ctx.fillStyle = fGrad
      ctx.beginPath()
      ctx.arc(m.x, m.y, m.flareRadius, 0, Math.PI * 2)
      ctx.fill()
    }

    // Pass 3: 等離子漸層彗尾
    const trailGrad = ctx.createLinearGradient(tailX, tailY, m.x, m.y)
    trailGrad.addColorStop(0, 'rgba(0, 0, 0, 0)')
    trailGrad.addColorStop(0.35, m.colorScheme.outer.replace(/[\d\.]+\)$/, `${0.30 * opacity})`))
    trailGrad.addColorStop(0.75, m.colorScheme.glow.replace(/[\d\.]+\)$/, `${0.80 * opacity})`))
    trailGrad.addColorStop(1, `rgba(255, 255, 255, ${0.98 * opacity})`)

    ctx.beginPath()
    ctx.moveTo(tailX, tailY)
    ctx.lineTo(m.x, m.y)
    ctx.strokeStyle = trailGrad
    ctx.lineWidth = m.isFireball ? 3.0 : (m.isCodeMeteor ? 2.2 : 1.8)
    ctx.lineCap = 'round'
    if (!isMobileDevice) {
      ctx.shadowColor = m.colorScheme.accent
      ctx.shadowBlur = m.isFireball ? 16 : (m.isCodeMeteor ? 12 : 9)
    }
    ctx.stroke()

    // Pass 4: 白熱針尖核心
    const coreGrad = ctx.createLinearGradient(
      m.x - Math.cos(m.angle) * (m.isFireball ? 25 : 16),
      m.y - Math.sin(m.angle) * (m.isFireball ? 25 : 16),
      m.x,
      m.y
    )
    coreGrad.addColorStop(0, 'rgba(255, 255, 255, 0)')
    coreGrad.addColorStop(0.6, 'rgba(255, 255, 255, 0.6)')
    coreGrad.addColorStop(1, `rgba(255, 255, 255, ${1.0 * opacity})`)

    ctx.beginPath()
    ctx.moveTo(m.x - Math.cos(m.angle) * (m.isFireball ? 25 : 16), m.y - Math.sin(m.angle) * (m.isFireball ? 25 : 16))
    ctx.lineTo(m.x, m.y)
    ctx.strokeStyle = coreGrad
    ctx.lineWidth = m.isFireball ? 1.6 : 1.0
    ctx.stroke()

    ctx.beginPath()
    ctx.arc(m.x, m.y, m.isFireball ? 2.2 : 1.4, 0, Math.PI * 2)
    ctx.fillStyle = '#ffffff'
    if (!isMobileDevice) {
      ctx.shadowColor = '#ffffff'
      ctx.shadowBlur = 12
    }
    ctx.fill()
  }

  ctx.restore()
}

// ---------------------------------------------------------------------------
// 互動監聽：滑鼠移動（用於 Three.js 柔和深空視差）
// ---------------------------------------------------------------------------
function handleMouseMove(e: MouseEvent) {
  targetMouseX = (e.clientX / window.innerWidth - 0.5) * 2
  targetMouseY = (e.clientY / window.innerHeight - 0.5) * 2
}

// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------
// 視窗縮放、分頁休眠保護與主渲染循環 (Mobile Zero-Jank & Power Shield)
// ---------------------------------------------------------------------------
function handleResize() {
  updateDeviceCapabilities()
  const w = window.innerWidth
  const h = window.innerHeight
  const dpr = getOptimalDpr()

  if (renderer && camera && canvasRef.value) {
    camera.aspect = w / h
    camera.updateProjectionMatrix()
    renderer.setSize(w, h)
    renderer.setPixelRatio(dpr)
  }

  if (starShaderMaterial) {
    starShaderMaterial.uniforms.uPixelRatio.value = dpr
  }

  if (meteorCanvasRef.value) {
    meteorCanvasRef.value.width = Math.round(w * dpr)
    meteorCanvasRef.value.height = Math.round(h * dpr)
  }
}

// 🔋 分頁切換與螢幕鎖定自動休眠鎖（防發燙、防耗電、防切回瞬移爆衝）
function handleVisibilityChange() {
  if (typeof document === 'undefined') return
  if (document.hidden) {
    isPageHidden = true
    if (animId) {
      cancelAnimationFrame(animId)
      animId = null
    }
  } else {
    isPageHidden = false
    // 喚醒時重置時鐘，防止背景暫停後 delta 瞬態爆增造成天體流星瞬移
    if (clock) {
      clock.getDelta()
    }
    if (!animId) {
      renderLoop()
    }
  }
}

function renderLoop() {
  if (isPageHidden) return
  animId = requestAnimationFrame(renderLoop)

  if (!renderer || !scene || !camera || !clock) return

  const delta = clock.getDelta()
  const elapsedTime = clock.getElapsedTime()

  // 尊重無障礙「減少動態效果」偏好：停止粒子與流星的高頻動畫，僅保持靜止深空
  if (prefersReducedMotion) {
    renderer.render(scene, camera)
    return
  }

  // 1. 更新並渲染 3D 宇宙星雲與微星
  if (currentUpdateFn) {
    currentUpdateFn(delta, elapsedTime)
  }
  renderer.render(scene, camera)

  // 2. 更新並渲染頂層 Awwwards 級流星與量子思維光環系統
  updateAndRenderMeteors(delta)
}

onMounted(() => {
  if (!canvasRef.value || !meteorCanvasRef.value) return

  updateDeviceCapabilities()
  const width = window.innerWidth
  const height = window.innerHeight
  const dpr = getOptimalDpr()

  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(55, width / height, 0.1, 120)
  camera.position.set(0, 0, 15)
  camera.lookAt(0, 0, 0)

  renderer = new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  })
  renderer.setSize(width, height)
  renderer.setPixelRatio(dpr)

  // Canvas 2D Retina / HiDPI 完美物理像素清晰度適配（手機端鎖定最適 DPR 1.25，省 75% 像素負擔）
  meteorCanvasRef.value.width = Math.round(width * dpr)
  meteorCanvasRef.value.height = Math.round(height * dpr)
  meteorCtx = meteorCanvasRef.value.getContext('2d')

  // 預熱 JetBrains Mono 向量字型快取防呆
  if (typeof document !== 'undefined' && 'fonts' in document) {
    document.fonts.load('bold 14px "JetBrains Mono"').catch(() => {})
  }

  clock = new THREE.Clock()

  initNebulaFlowScene()

  window.addEventListener('resize', handleResize)
  window.addEventListener('mousemove', handleMouseMove, { passive: true })
  document.addEventListener('visibilitychange', handleVisibilityChange)

  renderLoop()
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('mousemove', handleMouseMove)
  document.removeEventListener('visibilitychange', handleVisibilityChange)

  if (animId) {
    cancelAnimationFrame(animId)
    animId = null
  }

  clearCurrentScene()

  if (nebulaTexture) {
    nebulaTexture.dispose()
    nebulaTexture = null
  }
  if (starTexture) {
    starTexture.dispose()
    starTexture = null
  }

  if (renderer) {
    renderer.dispose()
    renderer = null
  }

  activeMeteors = []
  activeSparks = []
  activeAfterglows = []
  activeCodeDusts = []
  activeFlashWaves = []
  meteorCtx = null

  scene = null
  camera = null
  clock = null
})
</script>
