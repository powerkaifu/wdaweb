---
name: backend-security-audit
description: Django 後端資安防護、CORS/CSRF 白名單、環境變數隔離與 Render 雲端部署安全診斷。
---

# 技能：Django 後端安全與生產部署規範

## 1. 敏感資訊嚴格隔離
- `SECRET_KEY`、`DEBUG`、`DATABASE_URL` 強制由環境變數讀取，禁止在代碼庫中硬編碼。
- 本地開發預設 `DEBUG = True`，生產環境（Render）強制 `DEBUG = False`。

## 2. CORS 與 CSRF 白名單防禦
- `CORS_ALLOWED_ORIGINS` 與 `CSRF_TRUSTED_ORIGINS` 僅允許官方前台（`https://*.github.io`）與後端域名（`https://*.onrender.com`）。

## 3. 單一超級管理員原則
- 系統僅允許單一管理員帳號（預設 admin，由環境變數設定密碼），禁止開放外部註冊入口。
