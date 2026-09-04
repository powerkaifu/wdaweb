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
import { useCmsStore } from '@/stores/useCmsStore'

const canvasRef = ref<HTMLCanvasElement | null>(null)
const meteorCanvasRef = ref<HTMLCanvasElement | null>(null)
const store = useCmsStore()

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
  hasExploded: boolean
  flareAlpha: number
  flareRadius: number
  age: number
  duration: number
  dead: boolean
}

let meteorCtx: CanvasRenderingContext2D | null = null
let activeMeteors: CelestialMeteor[] = []
let activeSparks: MeteorSpark[] = []
let activeAfterglows: MeteorAfterglowSegment[] = []
let nextMeteorCountdown = 5.0
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
  }
]

function spawnMeteor(forceFireball = false) {
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

  const isFireball = forceFireball || store.meteorConfig.mode === 'fireball' || Math.random() < store.meteorConfig.fireballChance
  const palette = isFireball
    ? METEOR_PALETTES[2]
    : METEOR_PALETTES[Math.floor(Math.random() * METEOR_PALETTES.length)]

  const speed = isFireball
    ? 850 + Math.random() * 450
    : 1400 + Math.random() * 900

  const length = isFireball
    ? 240 + Math.random() * 200
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

  // 2. 建立 960 顆三階星等自然銀河繁星 (Three-Tier Stellar Magnitudes + GPU 原生非同步物理閃爍)
  // Tier 1: 64 顆璀璨一等星（~6.7%）- 小巧晶瑩鑽石十字光刺、飽和呼吸與 HDR 溢光
  // Tier 2: 300 顆中景二等星（~31.2%）- 沿旋臂密集聚散，獨立靈動眨眼
  // Tier 3: 596 顆深空微星星塵（~62.1%）- 廣袤深空微米晶光，鋪陳深邃天幕
  const starCount = 960
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
// 🌠 Awwwards 級流星渲染與物理更新 (Sub-Frame Optical Canvas Simulation)
// ---------------------------------------------------------------------------
function updateAndRenderMeteors(dt: number) {
  if (!meteorCtx || !meteorCanvasRef.value) return
  const ctx = meteorCtx
  const w = meteorCanvasRef.value.width
  const h = meteorCanvasRef.value.height

  ctx.clearRect(0, 0, w, h)

  // 1. 檢查手動立即觸發
  if (store.meteorConfig.manualTriggerCount !== lastMeteorTriggerCount) {
    lastMeteorTriggerCount = store.meteorConfig.manualTriggerCount
    spawnMeteor()
  }

  // 2. 自動隨機排程 (久久一次)
  if (store.meteorConfig.enabled) {
    nextMeteorCountdown -= dt
    if (nextMeteorCountdown <= 0) {
      spawnMeteor()
      if (store.meteorConfig.mode === 'shower') {
        // 璀璨流星雨：2 ~ 4 秒一顆
        nextMeteorCountdown = 2.0 + Math.random() * 2.5
      } else {
        // 靜謐偶發（真實仰望天球）：8 ~ 22 秒久久一次
        nextMeteorCountdown = 8.0 + Math.random() * 14.0
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
      activeAfterglows.splice(i, 1)
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
      activeSparks.splice(i, 1)
      continue
    }

    ctx.beginPath()
    ctx.arc(s.x, s.y, s.size * s.alpha, 0, Math.PI * 2)
    ctx.fillStyle = s.color.replace('ALPHA', String(s.alpha))
    ctx.shadowColor = s.color.replace('ALPHA', '0.8')
    ctx.shadowBlur = 6
    ctx.fill()
  }

  // 5. 更新並繪製「主體流星 (Meteors)」
  for (let i = activeMeteors.length - 1; i >= 0; i--) {
    const m = activeMeteors[i]
    m.age += dt
    const progress = m.age / m.duration

    if (progress >= 1.0) {
      m.dead = true
      activeMeteors.splice(i, 1)
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

    if (Math.random() < 0.40) {
      activeAfterglows.push({
        x: m.x,
        y: m.y,
        width: m.isFireball ? 4.5 : 2.5,
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
    const ambientRadius = m.isFireball ? 65 : 35
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
    ctx.lineWidth = m.isFireball ? 3.0 : 1.8
    ctx.lineCap = 'round'
    ctx.shadowColor = m.colorScheme.accent
    ctx.shadowBlur = m.isFireball ? 16 : 9
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
    ctx.shadowColor = '#ffffff'
    ctx.shadowBlur = 12
    ctx.fill()
  }

  ctx.restore()
}

// ---------------------------------------------------------------------------
// 互動監聽：滑鼠移動與滾動速度
// ---------------------------------------------------------------------------
function handleMouseMove(e: MouseEvent) {
  targetMouseX = (e.clientX / window.innerWidth - 0.5) * 2
  targetMouseY = (e.clientY / window.innerHeight - 0.5) * 2
}

// ---------------------------------------------------------------------------
// 視窗縮放與主渲染循環
// ---------------------------------------------------------------------------
function handleResize() {
  const w = window.innerWidth
  const h = window.innerHeight

  if (renderer && camera && canvasRef.value) {
    camera.aspect = w / h
    camera.updateProjectionMatrix()
    renderer.setSize(w, h)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  }

  if (starShaderMaterial) {
    starShaderMaterial.uniforms.uPixelRatio.value = Math.min(window.devicePixelRatio, 2)
  }

  if (meteorCanvasRef.value) {
    meteorCanvasRef.value.width = w
    meteorCanvasRef.value.height = h
  }
}

function renderLoop() {
  animId = requestAnimationFrame(renderLoop)

  if (!renderer || !scene || !camera || !clock) return

  const delta = clock.getDelta()
  const elapsedTime = clock.getElapsedTime()

  // 1. 更新並渲染 3D 宇宙星雲與微星
  if (currentUpdateFn) {
    currentUpdateFn(delta, elapsedTime)
  }
  renderer.render(scene, camera)

  // 2. 更新並渲染頂層 Awwwards 級流星系統
  updateAndRenderMeteors(delta)
}

onMounted(() => {
  if (!canvasRef.value || !meteorCanvasRef.value) return

  const width = window.innerWidth
  const height = window.innerHeight

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
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  meteorCanvasRef.value.width = width
  meteorCanvasRef.value.height = height
  meteorCtx = meteorCanvasRef.value.getContext('2d')

  clock = new THREE.Clock()

  initNebulaFlowScene()

  window.addEventListener('resize', handleResize)
  window.addEventListener('mousemove', handleMouseMove, { passive: true })

  renderLoop()
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('mousemove', handleMouseMove)

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
  meteorCtx = null

  scene = null
  camera = null
  clock = null
})
</script>
