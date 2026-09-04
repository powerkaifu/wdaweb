---
name: deploy-render
description: Render 雲端部署前的完整自我診斷與操作 SOP。當使用者說「部署後端」、「上傳到 Render」或遇到 Render 部署失敗時啟動。
---

# 技能：Render 雲端部署診斷

## 部署前自我診斷清單

### 1. requirements.txt 是否最新
執行以下指令重新生成依賴清單：

  pip freeze > requirements.txt

確認 gunicorn、whitenoise、dj-database-url 皆在清單中。

### 2. settings.py 生產設定確認
確認以下設定由環境變數讀取，而非硬編碼：
- SECRET_KEY = os.getenv('SECRET_KEY')
- DEBUG = os.getenv('DEBUG', 'True') == 'True'
- ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

### 3. build.sh 腳本確認
確認 server/build.sh 包含以下步驟：
- pip install -r requirements.txt
- python manage.py collectstatic --no-input
- python manage.py migrate
- python seed_data.py

### 4. 靜態檔案設定確認
確認 settings.py 中：
- STATIC_ROOT = BASE_DIR / 'staticfiles'
- STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
- 'whitenoise.middleware.WhiteNoiseMiddleware' 在 MIDDLEWARE 中且位於 SecurityMiddleware 之後

### 5. CORS 跨域設定確認
確認 CSRF_TRUSTED_ORIGINS 包含：
- https://*.onrender.com
- https://*.github.io

## Render Dashboard 環境變數設定對照表

| 變數名稱 | 值 |
| :--- | :--- |
| PYTHON_VERSION | 3.12.0 |
| DEBUG | False |
| SECRET_KEY | （Render 自動生成）|
| ALLOWED_HOSTS | * |
| DATABASE_URL | （選填，Render PostgreSQL）|