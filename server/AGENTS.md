# 後端 API 與管理系統（Django）AI 代理人核心準則

> activation: always_on
> scope: server/ 目錄下所有檔案

---

## 1. 後端架構概覽（三層嚴格分離）

  server/
  ├── apps/
  │   ├── cms/
  │   │   ├── models.py    # 層級 1：資料模型（ORM、軟刪除、欄位定義）
  │   │   └── admin.py     # Django Unfold Admin 設定（視覺化管理介面）
  │   └── api/
  │       ├── schemas.py   # 層級 2：輸入/輸出型別定義（Pydantic-style Ninja Schema）
  │       └── routers.py   # 層級 3：HTTP 路由控制（禁止在此直接寫複雜 ORM 查詢）
  ├── core/
  │   ├── settings.py      # 核心設定（CORS、資料庫、靜態檔案）
  │   └── urls.py          # 根 URL 配置
  └── seed_data.py         # 種子資料植入腳本

---

## 2. 三層架構職責定義（禁止混用）

- models.py（資料層）：只負責欄位定義、資料驗證、軟刪除邏輯與 Meta 設定，禁止撰寫業務邏輯。
- schemas.py（型別層）：只負責定義 API 的輸入輸出資料結構，不直接操作資料庫。
- routers.py（路由層）：只負責接收請求、呼叫 Model 查詢、序列化資料並回傳，禁止在此處撰寫複雜業務規則。

---

## 3. Model 設計強制規範

- 所有 CMS Model 必須繼承 SoftDeleteModel 基底類別（具備 deleted_at、created_at、updated_at）。
- 所有可排序的 Model 必須包含 sort_order = IntegerField(default=0) 欄位。
- 所有可啟用停用的 Model 必須包含 is_active = BooleanField(default=True) 欄位。
- 新增欄位時若有 NOT NULL 約束，必須提供 default 值，避免 Migration 互動式提示卡住。

---

## 4. API 公開性原則

- /api/v1/public/ 路由：完全公開，不需要身份驗證，前台 Vue 3 呼叫的所有端點均在此路由前綴下。
- /admin/ 路由：由 Django Session 處理管理員身份驗證，Unfold Admin UI 負責。
- 絕對禁止在 /api/v1/public/ 路由中暴露任何管理員相關的敏感操作。

---

## 5. 單一管理員原則

- 系統只允許存在一個超級管理員帳號（預設帳號 admin，由環境變數或後台安全設定密碼）。
- 禁止在 seed_data.py 中建立多個管理員帳號。
- 禁止在後台提供「新增管理員」的功能入口。

---

## 6. 常用指令

  # 啟動開發伺服器
  python manage.py runserver 8000

  # 建立並套用 Migration
  python manage.py makemigrations
  python manage.py migrate

  # 確認 Django 設定無錯誤
  python manage.py check

  # 植入種子資料
  python seed_data.py
