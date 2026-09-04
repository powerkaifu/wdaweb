---
name: seed-data
description: 安全新增或更新種子資料的 SOP。當使用者說「更新預設資料」、「重置初始資料」或「植入新資料」時使用。
---

# 技能：種子資料管理

## 安全更新原則

使用 get_or_create 或 update_or_create 而非直接 create，避免重複執行時產生重複資料。

## 執行 SOP

### Step 1：確認目標資料範圍
確認使用者要新增或更新哪個 Model 的種子資料。

### Step 2：在 seed_data.py 中調整資料
使用 Model.objects.update_or_create() 模式：

  Model.objects.update_or_create(
      defaults={欄位: 值},
      唯一識別欄位=識別值,
  )

### Step 3：執行種子腳本

  python seed_data.py

### Step 4：驗證
前往 http://127.0.0.1:8000/admin/ 確認新資料已正確出現於後台管理清單中。