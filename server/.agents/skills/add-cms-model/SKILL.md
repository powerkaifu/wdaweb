---
name: add-cms-model
description: 新增一個 CMS 資料模型的端對端 SOP（Model → Admin → Migration → Schema → Router → Seed Data）。當使用者說「新增後台功能」、「新增資料表」或「我要能管理 X」時啟動。
---

# 技能：新增 CMS Model 端對端流程

## 執行 SOP

### Step 1：分析需求
確認新 Model 需要哪些欄位、是否需要圖片上傳、是否需要 sort_order 排序。

### Step 2：在 models.py 新增 Model 類別
在 `server/apps/cms/models.py` 中：
- 繼承 SoftDeleteModel
- 加入 sort_order 與 is_active 欄位
- 撰寫 Meta.ordering 與 __str__ 方法
- 圖片欄位對應加入 _alt 欄位（無障礙 Alt Text）

### Step 3：在 admin.py 新增 Admin 配置
在 `server/apps/cms/admin.py` 中：
- 繼承 UnfoldModelAdmin
- 設定 list_display、list_editable（sort_order、is_active）
- 若有圖片欄位，加入縮圖預覽方法
- 加入「移至垃圾桶」與「還原」批次動作

### Step 4：執行 Migration

  python manage.py makemigrations
  python manage.py migrate

確認 Migration 成功執行無錯誤。

### Step 5：在 schemas.py 新增 Schema
在 `server/apps/api/schemas.py` 中新增對應的 XxxOut Schema，圖片欄位使用 Optional[str] 並提供 resolve_xxx 方法。

### Step 6：在 routers.py 新增 API 端點
在 `server/apps/api/routers.py` 中新增對應的 GET 端點，回傳 List[XxxOut]，使用 filter(deleted_at__isnull=True) 過濾軟刪除資料。

### Step 7：更新 seed_data.py
在 `server/seed_data.py` 中加入對應的初始種子資料，確保開發環境有基本資料可用。

### Step 8：驗證
- 確認後台 Admin 介面可正確顯示與操作新 Model。
- 確認 http://127.0.0.1:8000/api/v1/docs 中新 API 端點可正確回傳資料。