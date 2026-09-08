# -*- coding: utf-8 -*-
"""
學員專題成果 - 自動無頭瀏覽器截圖與 CDN 同步服務模組
支援管理命令、Django Admin Action 與背景非同步觸發
"""
import os
import sys
import time
import logging
import threading
from pathlib import Path
from PIL import Image
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)

BASE_DIR = Path(settings.BASE_DIR)
SERVER_MEDIA_DIR = BASE_DIR / "media" / "projects"
CLIENT_PUBLIC_DIR = BASE_DIR.parent / "client" / "public" / "projects"

SERVER_MEDIA_DIR.mkdir(parents=True, exist_ok=True)
CLIENT_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)


def get_headless_driver():
    """建立並配置 Selenium Headless Chrome Driver"""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,800')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(25)
    return driver


def sync_file_to_cloudinary(p_id: int, local_webp: Path) -> str:
    """若系統有設定 Cloudinary，同步上傳至 CDN 避免 404"""
    if getattr(settings, 'IS_CLOUDINARY_CONFIGURED', False):
        try:
            import cloudinary.uploader
            res = cloudinary.uploader.upload(
                str(local_webp),
                public_id=f"media/projects/project_{p_id}",
                overwrite=True,
                resource_type='image'
            )
            secure_url = res.get('secure_url', '')
            logger.info(f"[ScreenshotService] ID {p_id} 成功同步至 Cloudinary: {secure_url}")
            return secure_url
        except Exception as e:
            logger.warning(f"[ScreenshotService] ID {p_id} 上傳 Cloudinary 失敗: {e}")
    return ""


def capture_single_project(project_id: int, wait_sec: float = 3.5, driver=None) -> bool:
    """針對單一專案執行無頭截圖、WebP 轉換、本機與前端同步及 Cloudinary 上架"""
    from apps.cms.models import StudentProject

    try:
        project = StudentProject.objects.get(id=project_id)
    except StudentProject.DoesNotExist:
        logger.error(f"[ScreenshotService] 找不到專案 ID: {project_id}")
        return False

    url = project.demo_url
    if not url or not url.startswith('http'):
        logger.warning(f"[ScreenshotService] 專案 ID {project_id} 沒有有效 Demo URL: {url}")
        return False

    should_close_driver = False
    if driver is None:
        driver = get_headless_driver()
        should_close_driver = True

    server_file = SERVER_MEDIA_DIR / f"project_{project.id}.webp"
    client_file = CLIENT_PUBLIC_DIR / f"project_{project.id}.webp"
    temp_png = server_file.with_suffix('.png')

    try:
        logger.info(f"[ScreenshotService] 正在拜訪專案 {project.id} ({project.project_name}): {url}")
        try:
            driver.get(url)
        except Exception as e:
            logger.warning(f"[ScreenshotService] 頁面可能超時，仍嘗試等待 SPA 渲染: {e}")

        time.sleep(wait_sec)
        driver.save_screenshot(str(temp_png))

        if not temp_png.exists() or temp_png.stat().st_size == 0:
            logger.error(f"[ScreenshotService] 截圖檔案生成失敗或為空: {url}")
            return False

        # 使用 Pillow 轉成優質 WebP
        with Image.open(temp_png) as img:
            if img.mode in ('RGBA', 'LA'):
                img.save(server_file, 'WEBP', quality=85, method=6)
                img.save(client_file, 'WEBP', quality=85, method=6)
            else:
                rgb_img = img.convert('RGB')
                rgb_img.save(server_file, 'WEBP', quality=85, method=6)
                rgb_img.save(client_file, 'WEBP', quality=85, method=6)

        if temp_png.exists():
            temp_png.unlink()

        # 更新資料庫
        project.cover_image = f"projects/project_{project.id}.webp"
        if not project.image_alt:
            project.image_alt = f"{project.project_name} - 學員 {project.student_name} 專題作品首頁成果"
        project.save(update_fields=['cover_image', 'image_alt'])

        # 同步上傳至 Cloudinary
        sync_file_to_cloudinary(project.id, server_file)
        logger.info(f"[ScreenshotService] ✅ 專案 ID {project.id} ({project.project_name}) 截圖與同步完成！")
        return True
    except Exception as e:
        logger.error(f"[ScreenshotService] ❌ 專案 ID {project.id} 截圖失敗: {e}")
        if temp_png.exists():
            temp_png.unlink()
        return False
    finally:
        if should_close_driver:
            driver.quit()


def capture_missing_projects(force_all: bool = False) -> tuple[int, int]:
    """批次處理缺圖或所有專案"""
    from apps.cms.models import StudentProject

    qs = StudentProject.objects.filter(is_active=True).order_by('id')
    if not force_all:
        # 只挑選尚未設定封面圖的專案
        qs = qs.filter(cover_image='')

    total = qs.count()
    if total == 0:
        return 0, 0

    driver = get_headless_driver()
    success_count = 0
    try:
        for p in qs:
            if capture_single_project(p.id, wait_sec=3.5, driver=driver):
                success_count += 1
            time.sleep(0.5)
    finally:
        driver.quit()

    return success_count, total


def trigger_async_capture(project_id: int):
    """在獨立背景執行緒中非同步執行單一專案截圖（避免阻擋 Admin 介面或 Web Request）"""
    thread = threading.Thread(
        target=capture_single_project,
        args=(project_id, 3.5, None),
        daemon=True
    )
    thread.start()
    return thread
