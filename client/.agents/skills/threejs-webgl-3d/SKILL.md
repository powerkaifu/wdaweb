---
name: threejs-webgl-3d
description: Three.js、WebGL 3D 場景、GLTF 模型載入、PBR 材質與 3D 效能優化標準。當需要開發 3D 互動場景、3D 模型展示、著色器光暈或 3D 數據視覺化時啟動此技能。
---

# 技能：Three.js 與 WebGL 3D 前端視覺權威規範

## 1. 核心渲染管線 (Three.js Lifecycle)
一個健全的 Three.js 組件必須包含：
1. **Scene**（場景）+ **PerspectiveCamera**（透視攝影機）+ **WebGLRenderer**（渲染器）
2. **Resize 響應監聽**：動態更新 `camera.aspect` 與 `renderer.setSize`，並依據 `Math.min(window.devicePixelRatio, 2)` 限制像素比以保護效能。
3. **RAF 渲染迴圈**：記錄 `requestAnimationFrame` ID。
4. **資源完整銷毀 (Disposal)**：幾何體、材質、貼圖與 WebGL Context 回收。

## 2. 嚴格防洩漏銷毀範本 (Disposal Checklist)
```ts
onUnmounted(() => {
  if (rafId) cancelAnimationFrame(rafId)
  window.removeEventListener('resize', onResize)

  // 走訪場景並銷毀所有幾何體與材質
  scene.traverse((object: any) => {
    if (object.isMesh) {
      if (object.geometry) object.geometry.dispose()
      if (object.material) {
        if (Array.isArray(object.material)) {
          object.material.forEach((mat: any) => mat.dispose())
        } else {
          object.material.dispose()
        }
      }
    }
  })

  renderer.dispose()
  renderer.forceContextLoss()
})
```

## 3. 效能最佳實踐
- **限制像素比**：`renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`，避免在 4K 螢幕上造成 GPU 負載過大。
- **減少 Draw Calls**：大量相似 3D 物件使用 `InstancedMesh`。
- **模型壓縮**：3D 模型優先使用 Draco / KTX2 壓縮的 `.glb` 格式。
