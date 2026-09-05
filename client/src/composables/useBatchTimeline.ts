import { computed, toValue, type MaybeRefOrGetter } from 'vue'
import type { AdmissionBatch } from '@/types'
import { defaultBatches } from '@/stores/useCmsStore'
import {
  isBatchEnrolling,
  isBatchUpcoming,
  isBatchTraining,
  isBatchEnded,
  isBatchScreeningOrPreparing,
  getCountdownText,
} from '@/utils/batchStatus'

export interface LifecycleStep {
  key: string
  label: string
}

export interface TrainingProgress {
  elapsedDays: number
  totalDays: number
  percent: number
  remainingDays: number
}

export interface StatusPill {
  label: string
  class: string
}

export interface DetailNotice {
  icon: string
  text: string
}

/**
 * 招生期別時序與生命週期演算 Composable
 * 遵循 SRP 與 SoC 原則，將期別推導、雙期別智慧輪替、5 階段步進節點、進度條百分比完全抽離封裝
 * 同時配置防禦性 defaultBatches 兜底防線，確保任何異常情境下 100% 絕對有卡片呈現
 */
export function useBatchTimeline(batchesInput: MaybeRefOrGetter<AdmissionBatch[]>) {
  const lifecycleSteps: LifecycleStep[] = [
    { key: 'register', label: '1.報名' },
    { key: 'screening', label: '2.甄試' },
    { key: 'preparing', label: '3.待訓' },
    { key: 'training', label: '4.培訓' },
    { key: 'graduation', label: '5.結訓' }
  ]

  /**
   * 取得期別的時間軸絕對權重時間戳 (用於精確時序排序，避免日期欄位缺失導致亂序)
   */
  function getBatchTimeValue(batch: AdmissionBatch): number {
    if (batch.training_start_date) {
      const t = new Date(batch.training_start_date.replace(/-/g, '/')).getTime()
      if (!isNaN(t)) return t
    }
    if (batch.enroll_start_date) {
      const t = new Date(batch.enroll_start_date.replace(/-/g, '/')).getTime()
      if (!isNaN(t)) return t
    }
    return (batch.sort_order || 0) * 1000000000000
  }

  /**
   * 取得期別生命週期的活躍優先權重 (Liveness Priority)：
   * - 4: 火熱報名中 (open / closing_soon) ➔ 核心主角，絕對優先上首頁！
   * - 3: 待開訓或甄試中 (screening / preparing) ➔ 緊湊進行中，優先保留！
   * - 2: 正式受訓中 (training) ➔ 現役衝刺班，優先保留！
   * - 1: 即將開放籌備中 (upcoming) ➔ 次要保留
   * - 0: 已圓滿結訓 (ended) ➔ 最先被輪替歸檔！
   */
  function getBatchLivenessPriority(batch: AdmissionBatch): number {
    if (isBatchEnrolling(batch)) return 4
    if (isBatchScreeningOrPreparing(batch)) return 3
    if (isBatchTraining(batch)) return 2
    if (isBatchUpcoming(batch)) return 1
    return 0
  }

  /**
   * 智慧自適應期別輪替與位置錨定 (Smart Adaptive Batch Slotting)：
   * 1. 總數 > 2 時，依活躍優先級篩選，優先淘汰已結訓舊班
   * 2. 嚴格依時間序列「左舊進行中、右新即將到來/報名中」自然流向排列
   * 3. 雙重防禦保底：若無資料自動使用 defaultBatches，確保期別卡片 100% 絕對存在
   */
  const sortedBatches = computed(() => {
    const rawList = toValue(batchesInput)
    const list = Array.isArray(rawList) && rawList.length > 0 ? rawList : defaultBatches
    const visibleBatches = [...list].filter(b => b.status_override !== 'hidden')

    if (visibleBatches.length <= 2) {
      return visibleBatches.sort((a, b) => getBatchTimeValue(a) - getBatchTimeValue(b))
    }

    const prioritized = [...visibleBatches].sort((a, b) => {
      const pDiff = getBatchLivenessPriority(b) - getBatchLivenessPriority(a)
      if (pDiff !== 0) return pDiff
      return getBatchTimeValue(b) - getBatchTimeValue(a)
    })

    const selectedTwo = prioritized.slice(0, 2)
    return selectedTwo.sort((a, b) => getBatchTimeValue(a) - getBatchTimeValue(b))
  })

  function getScreeningEndTime(screeningDateStr?: string | null): number {
    if (!screeningDateStr) return 0
    try {
      const base = new Date(screeningDateStr.replace(/-/g, '/')).getTime()
      // 甄試結束精準時間點：當天 16:35:00
      return base + (16 * 60 + 35) * 60 * 1000
    } catch {
      return 0
    }
  }

  function isScreeningEnded(batch: AdmissionBatch): boolean {
    if (!batch.screening_date) return false
    const endTime = getScreeningEndTime(batch.screening_date)
    return endTime > 0 && Date.now() >= endTime
  }

  function getStepStatus(batch: AdmissionBatch, stepNumber: number): 'completed' | 'active' | 'pending' {
    const now = Date.now()
    const enrollEnd = batch.enroll_end_date ? new Date(batch.enroll_end_date.replace(/-/g, '/')).getTime() + 24 * 60 * 60 * 1000 - 1000 : 0
    const screeningEndTime = getScreeningEndTime(batch.screening_date)
    const trainStart = batch.training_start_date ? new Date(batch.training_start_date.replace(/-/g, '/')).getTime() : 0
    const trainEnd = batch.training_end_date ? new Date(batch.training_end_date.replace(/-/g, '/')).getTime() + 24 * 60 * 60 * 1000 - 1000 : 0

    if (stepNumber === 1) {
      if (now > enrollEnd && enrollEnd > 0) return 'completed'
      if (isBatchEnrolling(batch)) return 'active'
      return 'pending'
    }
    if (stepNumber === 2) {
      if (screeningEndTime > 0 && now >= screeningEndTime) return 'completed'
      if (now > enrollEnd && (screeningEndTime === 0 || now < screeningEndTime)) return 'active'
      return 'pending'
    }
    if (stepNumber === 3) {
      if (now >= trainStart && trainStart > 0) return 'completed'
      if (screeningEndTime > 0 && now >= screeningEndTime && now < trainStart) return 'active'
      return 'pending'
    }
    if (stepNumber === 4) {
      if (now > trainEnd && trainEnd > 0) return 'completed'
      if (now >= trainStart && now <= trainEnd) return 'active'
      return 'pending'
    }
    if (stepNumber === 5) {
      if (now >= trainEnd && trainEnd > 0) return 'completed'
      return 'pending'
    }
    return 'pending'
  }

  function getFastStatusPill(batch: AdmissionBatch): StatusPill {
    if (isBatchEnded(batch)) {
      return {
        label: `🏁 本期已結訓 · 報名截止`,
        class: 'bg-slate-900/90 text-slate-400 border border-slate-800 shadow-none'
      }
    }
    if (isBatchTraining(batch)) {
      const prog = getTrainingProgress(batch)
      const days = prog.remainingDays
      return {
        label: days <= 14 ? `🏁 倒數結訓 · 距結訓僅剩 ${days} 天` : `🟢 920h 實體培訓進行中`,
        class: 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/40 shadow-sm shadow-emerald-500/10'
      }
    }
    if (isBatchScreeningOrPreparing(batch)) {
      return {
        label: `✨ 甄試結束 · 待開訓 (${batch.training_start_date} 開課)`,
        class: 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/40 shadow-sm shadow-cyan-500/10'
      }
    }
    if (isBatchEnrolling(batch)) {
      return {
        label: `🔥 火熱報名中 · ${getCountdownText(batch.enroll_end_date)}`,
        class: 'bg-amber-500/20 text-amber-300 border border-amber-500/40 shadow-sm shadow-amber-500/10'
      }
    }
    if (isBatchUpcoming(batch)) {
      return {
        label: `⏳ 新期別籌備中`,
        class: 'bg-purple-500/15 text-purple-300 border border-purple-500/30'
      }
    }
    return {
      label: `🏁 本期已結訓（報名截止）`,
      class: 'bg-slate-800 text-slate-400 border border-slate-700'
    }
  }

  function getLifecycleLineWidth(batch: AdmissionBatch): string {
    if (getStepStatus(batch, 5) === 'completed') return '100%'
    if (getStepStatus(batch, 4) === 'active') return '75%'
    if (getStepStatus(batch, 3) === 'active') return '50%'
    if (getStepStatus(batch, 2) === 'active') return '25%'
    if (getStepStatus(batch, 1) === 'active') return '0%'
    return '0%'
  }

  function getStepNodeClass(batch: AdmissionBatch, stepNumber: number): string {
    if (isBatchEnded(batch)) {
      return 'bg-slate-800 text-slate-400 border border-slate-700/80'
    }
    const status = getStepStatus(batch, stepNumber)
    if (status === 'completed') {
      return 'bg-emerald-500 text-slate-950 shadow-[0_0_10px_rgba(16,185,129,0.4)]'
    }
    if (status === 'active') {
      return 'bg-cyan-400 text-slate-950 font-black ring-4 ring-cyan-400/40 shadow-[0_0_16px_rgba(6,182,212,0.85)]'
    }
    return 'bg-slate-800 text-slate-500 border border-slate-700/80'
  }

  function getStepTextClass(batch: AdmissionBatch, stepNumber: number): string {
    if (isBatchEnded(batch)) return 'text-slate-500'
    const status = getStepStatus(batch, stepNumber)
    if (status === 'completed') return 'text-emerald-400 font-semibold'
    if (status === 'active') return 'text-cyan-300 font-bold'
    return 'text-slate-500'
  }

  function getTrainingProgress(batch: AdmissionBatch): TrainingProgress {
    if (!batch.training_start_date || !batch.training_end_date) {
      return { elapsedDays: 0, totalDays: 169, percent: 0, remainingDays: 0 }
    }
    try {
      const start = new Date(batch.training_start_date.replace(/-/g, '/')).getTime()
      const end = new Date(batch.training_end_date.replace(/-/g, '/')).getTime() + 24 * 60 * 60 * 1000 - 1000
      const now = Date.now()
      const totalDays = Math.max(1, Math.round((end - start) / (1000 * 60 * 60 * 24)))
      const elapsedDays = Math.max(1, Math.min(totalDays, Math.round((now - start) / (1000 * 60 * 60 * 24))))
      const percent = Math.min(100, Math.round((elapsedDays / totalDays) * 100))
      const remainingDays = Math.max(0, totalDays - elapsedDays)
      return { elapsedDays, totalDays, percent, remainingDays }
    } catch {
      return { elapsedDays: 0, totalDays: 169, percent: 0, remainingDays: 0 }
    }
  }

  function getLifecycleDetailNotice(batch: AdmissionBatch): DetailNotice {
    if (isBatchTraining(batch)) {
      const prog = getTrainingProgress(batch)
      if (prog.remainingDays <= 14) {
        return {
          icon: '⏳',
          text: `受訓倒數衝刺：已受訓 ${prog.elapsedDays}/${prog.totalDays} 天，距 ${batch.training_end_date} 正式結訓僅剩 ${prog.remainingDays} 天！`
        }
      }
      return {
        icon: '🎓',
        text: `920h 核心培訓進行中：已完成 ${prog.elapsedDays} / ${prog.totalDays} 天`
      }
    }
    if (isBatchScreeningOrPreparing(batch)) {
      return {
        icon: '✨',
        text: `甄試已圓滿結束 · 正備取名單造冊審核中，預計 ${batch.training_start_date} 正式開訓！`
      }
    }
    if (isBatchEnrolling(batch)) {
      return {
        icon: '🔥',
        text: `官方熱烈報名中 · 把握 100% 全額補助參訓機會！`
      }
    }
    if (isBatchUpcoming(batch)) {
      return {
        icon: '⏳',
        text: `新一期別籌備中 · 預定開訓日期即將公布`
      }
    }
    return {
      icon: '🏁',
      text: `本期訓練已正式結訓 · 報名已截止受理`
    }
  }

  return {
    lifecycleSteps,
    sortedBatches,
    getStepStatus,
    isScreeningEnded,
    getFastStatusPill,
    getLifecycleLineWidth,
    getStepNodeClass,
    getStepTextClass,
    getTrainingProgress,
    getLifecycleDetailNotice
  }
}
