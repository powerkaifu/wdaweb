---
name: database-migration-safety
description: Django 資料庫安全 Migration、軟刪除機制與種子資料管理 SOP。當修改 models.py 欄位、建立遷移或更新預設資料時啟動。
---

# 技能：Django 資料庫 Migration 安全與種子資料管理

## 1. Migration 防呆守則
- **NOT NULL 約束**：新增任何非 null 欄位時，必須在 Model 中宣告 `default=...`，避免 Migration 產生互動提示卡死 CI/CD。
- **重命名欄位**：使用 Django 的 `RenameField` 操作，嚴禁刪除欄位後重建，避免遺失歷史資料。
- **執行前檢查**：套用 Migration 前，強制執行 `python manage.py check` 確認系統無任何模型衝突。

## 2. 軟刪除與種子資料原則
- **SoftDeleteModel**：所有 CMS Model 均繼承軟刪除，刪除時標記 `deleted_at = timezone.now()`，API 查詢一律加入 `deleted_at__isnull=True`。
- **冪等性種子腳本 (`seed_data.py`)**：資料植入一律使用 `Model.objects.update_or_create()`，確保重複執行不產生重複髒資料。
