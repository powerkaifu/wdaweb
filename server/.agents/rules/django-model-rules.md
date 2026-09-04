---
trigger: always_on
---

# Django Model 設計規範

## 欄位命名規範

- 欄位名稱使用 snake_case（例：batch_name、sort_order、is_active）。
- 布林欄位以 is_ 或 has_ 開頭（例：is_active、is_featured）。
- 日期時間欄位以 _at 結尾（例：created_at、deleted_at、enroll_start_date）。

## 軟刪除規範

- 所有 CMS Model 必須繼承 SoftDeleteModel。
- 軟刪除欄位：deleted_at = DateTimeField(null=True, blank=True, default=None)。
- 查詢時預設過濾 deleted_at__isnull=True（軟刪除資料不出現在 API 回傳）。
- Admin 後台提供「移至垃圾桶」與「還原」兩個批次動作。

## Migration 安全守則

- 新增任何有 NOT NULL 約束的欄位時，必須提供 default 值（例：default=0 或 default=''）。
- 重新命名欄位時，使用 RenameField 操作而非刪除後新增，以保留既有資料。
- 執行 Migration 前必須先執行 python manage.py check 確認無設定錯誤。
- 正式環境 Migration 前，必須先備份資料庫。

## 圖片欄位規範

- 圖片欄位使用 ImageField(upload_to='子目錄名稱/', null=True, blank=True)。
- 對應的 Alt 文字欄位使用 CharField(max_length=200, default='', blank=True)。
- settings.py 中必須正確設定 MEDIA_URL 與 MEDIA_ROOT。