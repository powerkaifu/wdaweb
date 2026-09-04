import os
from pathlib import Path
from django.urls import reverse_lazy
from django.templatetags.static import static
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-wdaweb-taishan-frontend-ai-key-2026')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'apps.cms',
    'apps.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database: 優先使用 Render DATABASE_URL (PostgreSQL)，若無則使用 SQLite
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS & CSRF 配置 (支援 GitHub Pages 與 Render)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://*.github.io',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

UNFOLD = {
    'SITE_TITLE': '泰山職訓－前端網頁技術與AI應用',
    'SITE_HEADER': '前端班 CMS 內容管理後台',
    'SITE_URL': '/',
    'SITE_ICON': lambda request: static('images/logo.png'),
    'SITE_LOGO': lambda request: static('images/logo.png'),
    'SITE_FAVICONS': [
        {
            'rel': 'icon',
            'sizes': '32x32',
            'type': 'image/png',
            'href': lambda request: static('images/logo.png'),
        },
    ],
    'SHOW_HISTORY': False,
    'SHOW_VIEW_ON_SITE': True,
    'COLORS': {
        'primary': {
            '50': '236 254 255',
            '100': '207 250 254',
            '200': '165 243 252',
            '300': '103 232 249',
            '400': '34 211 238',
            '500': '6 182 212',
            '600': '8 145 178',
            '700': '14 116 144',
            '800': '21 94 117',
            '900': '22 78 99',
            '950': '8 51 68',
        },
    },
    'SIDEBAR': {
        'show_search': False,
        'show_all_applications': False,
        'navigation': [
            {
                'title': '課程特色 (首頁管理)',
                'separator': False,
                'collapsible': False,
                'items': [
                    {
                        'title': '首頁輪播圖管理',
                        'icon': 'view_carousel',
                        'link': lambda request: reverse_lazy('admin:cms_carousel_changelist'),
                    },
                    {
                        'title': '7大課程模組管理 (920h)',
                        'icon': 'school',
                        'link': lambda request: reverse_lazy('admin:cms_curriculummodule_changelist'),
                    },
                    {
                        'title': '核心技術卡片管理',
                        'icon': 'code',
                        'link': lambda request: reverse_lazy('admin:cms_techcard_changelist'),
                    },
                    {
                        'title': '教學設備設施管理',
                        'icon': 'devices',
                        'link': lambda request: reverse_lazy('admin:cms_facility_changelist'),
                    },
                ],
            },
            {
                'title': '學員專題成果',
                'separator': True,
                'collapsible': False,
                'items': [
                    {
                        'title': '學員作品集管理',
                        'icon': 'folder_special',
                        'link': lambda request: reverse_lazy('admin:cms_studentproject_changelist'),
                    },
                ],
            },
            {
                'title': '招生期別與報名',
                'separator': True,
                'collapsible': False,
                'items': [
                    {
                        'title': '招生期別與官方連結',
                        'icon': 'event_available',
                        'link': lambda request: reverse_lazy('admin:cms_admissionbatch_changelist'),
                    },
                ],
            },
            {
                'title': 'Discord 線上諮詢',
                'separator': True,
                'collapsible': False,
                'items': [
                    {
                        'title': 'Discord 社群與全域宣傳設定',
                        'icon': 'forum',
                        'link': lambda request: reverse_lazy('admin:cms_sitesetting_changelist'),
                    },
                ],
            },
            {
                'title': '常見問題 FAQ',
                'separator': True,
                'collapsible': False,
                'items': [
                    {
                        'title': '常見問答 (FAQ) 管理',
                        'icon': 'quiz',
                        'link': lambda request: reverse_lazy('admin:cms_faq_changelist'),
                    },
                ],
            },
            {
                'title': '系統管理與權限',
                'separator': True,
                'collapsible': True,
                'items': [
                    {
                        'title': '管理員帳號',
                        'icon': 'admin_panel_settings',
                        'link': lambda request: reverse_lazy('admin:auth_user_changelist'),
                    },
                ],
            },
        ],
    },
}
