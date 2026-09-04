---
name: physics-spring-microinteractions
description: 物理彈簧動效 (Spring Physics)、磁吸按鈕 (Magnetic UI)、觸覺回饋與手感微互動規範。當開發按鈕點擊動態、卡片磁吸跟隨、彈窗手感或手勢拖曳時啟動此技能。
---

# 技能：物理彈簧手感與 UI 微互動規範

## 1. 物理彈簧原理 (Spring Mechanics)
拋棄機械式固定時間的 `ease-in-out`，改以物理三大參數定義動態：
- **Stiffness (剛度)**：數值越高，回彈越迅速有力（如 300 ~ 500）。
- **Damping (阻尼)**：數值越低，回彈次數越多；適中阻尼（如 20 ~ 30）可產生極致手感。
- **Mass (質量)**：物體的慣性質感。

## 2. 經典微互動模式

### 2.1 磁吸按鈕 (Magnetic Button Effect)
當滑鼠移近按鈕時，按鈕與文字以平滑阻尼向滑鼠游標輕微位移，離開時彈簧回正。
```ts
function onMouseMove(e: MouseEvent, target: HTMLElement) {
  const rect = target.getBoundingClientRect()
  const x = (e.clientX - (rect.left + rect.width / 2)) * 0.25
  const y = (e.clientY - (rect.top + rect.height / 2)) * 0.25
  target.style.transform = `translate3d(${x}px, ${y}px, 0)`
}

function onMouseLeave(target: HTMLElement) {
  target.style.transform = 'translate3d(0, 0, 0)'
}
```

### 2.2 點擊微反饋 (Active Press Feedback)
所有主要操作按鈕加入按下時的物理微縮放：
`active:scale-95 transition-transform duration-100 ease-out`。
