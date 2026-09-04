# 工作流：Django Migration 安全執行流程

觸發條件：任何對 models.py 的欄位新增、修改或刪除操作。

## 執行步驟

### Step 1：影響範圍確認
使用 grep_search 確認此次 Model 變更是否影響：
- schemas.py 的對應 Schema 欄位
- admin.py 的 list_display 設定
- seed_data.py 的種子資料植入邏輯

### Step 2：新增欄位安全確認
若新增欄位有 NOT NULL 約束，確認已提供 default 值。
若新增圖片欄位，確認同時新增對應的 _alt 文字欄位。

### Step 3：產生 Migration 檔案

  python manage.py makemigrations

仔細閱讀 Django 產生的 Migration 變更摘要，確認符合預期。

### Step 4：套用 Migration

  python manage.py migrate

確認套用成功，無錯誤訊息。

### Step 5：Django 系統確認

  python manage.py check

確認系統無任何設定或 Model 錯誤。

### Step 6：後台功能確認
啟動 Django 伺服器，登入 http://127.0.0.1:8000/admin/ 確認新欄位正確出現於後台表單中。

### Step 7：同步更新 schemas.py
若 Model 有欄位異動，同步更新 `server/apps/api/schemas.py` 中對應的 Schema 欄位定義。