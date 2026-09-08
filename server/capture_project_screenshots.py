"""
學員專題成果 - 自動無頭瀏覽器截圖與雙向同步腳本
使用 Selenium WebDriver (Headless Chrome) 自動拜訪每位學員專題的線上 Demo 網址，
等待 SPA 動態渲染完成後截圖，並使用 Pillow 壓縮為高畫質輕量 WebP 格式，
同步儲存至後端 media/projects 與前端 public/projects 目錄，並更新資料庫。
"""
import os
import sys
import time
from pathlib import Path
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 初始化 Django 環境
sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

from apps.cms.models import StudentProject

# 輸出路徑配置
SERVER_MEDIA_DIR = BASE_DIR / "media" / "projects"
CLIENT_PUBLIC_DIR = BASE_DIR.parent / "client" / "public" / "projects"

SERVER_MEDIA_DIR.mkdir(parents=True, exist_ok=True)
CLIENT_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

def init_driver():
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

def capture_project(driver, url: str, output_webp: Path, client_webp: Path, wait_sec: float = 3.5) -> bool:
    """透過 Selenium 打開網頁、等待 SPA 渲染並轉存為 WebP"""
    temp_png = output_webp.with_suffix('.png')
    
    try:
        try:
            driver.get(url)
        except Exception as e:
            print(f"  ⚠️ 頁面載入可能超時或有異常，但仍嘗試等待渲染: {e}")
            
        time.sleep(wait_sec)
        
        # 截取螢幕
        driver.save_screenshot(str(temp_png))
        
        if not temp_png.exists() or temp_png.stat().st_size == 0:
            print(f"  ⚠️ 截圖檔案不存在或為空: {url}")
            return False
            
        # 使用 Pillow 壓縮轉為 WebP
        with Image.open(temp_png) as img:
            if img.mode in ('RGBA', 'LA'):
                img.save(output_webp, 'WEBP', quality=85, method=6)
                img.save(client_webp, 'WEBP', quality=85, method=6)
            else:
                rgb_img = img.convert('RGB')
                rgb_img.save(output_webp, 'WEBP', quality=85, method=6)
                rgb_img.save(client_webp, 'WEBP', quality=85, method=6)
                
        if temp_png.exists():
            temp_png.unlink()
            
        size_kb = output_webp.stat().st_size / 1024
        print(f"  ✅ 成功截圖並轉換 WebP ({size_kb:.1f} KB): {output_webp.name}")
        return True
    except Exception as e:
        print(f"  ❌ 截圖處理發生異常 ({url}): {e}")
        if temp_png.exists():
            temp_png.unlink()
        return False

def sync_to_cloudinary(p_id: int, local_webp: Path):
    """若系統有設定 Cloudinary，同步上傳至 CDN 避免 404"""
    try:
        from django.conf import settings
        if getattr(settings, 'IS_CLOUDINARY_CONFIGURED', False):
            import cloudinary.uploader
            res = cloudinary.uploader.upload(
                str(local_webp),
                public_id=f"media/projects/project_{p_id}",
                overwrite=True,
                resource_type='image'
            )
            print(f"  ☁️ 已同步至 Cloudinary CDN: {res.get('secure_url')}")
    except Exception as e:
        print(f"  ⚠️ Cloudinary 上傳略過或失敗: {e}")

def main():
    projects = StudentProject.objects.all().order_by('id')
    total = projects.count()
    print(f"\n📋 開始批次處理 {total} 筆學員專題作品截圖 (Selenium Headless Chrome)...\n")
    
    driver = init_driver()
    success_count = 0
    
    try:
        for idx, p in enumerate(projects, 1):
            print(f"[{idx}/{total}] 正在截圖: ID {p.id} - {p.student_name} - {p.project_name}")
            print(f"       網址: {p.demo_url}")
            
            if not p.demo_url or not p.demo_url.startswith('http'):
                print(f"  ⏭️ 跳過：無效網址")
                continue
                
            server_file = SERVER_MEDIA_DIR / f"project_{p.id}.webp"
            client_file = CLIENT_PUBLIC_DIR / f"project_{p.id}.webp"
            
            # 執行截圖
            if capture_project(driver, p.demo_url, server_file, client_file, wait_sec=3.5):
                p.cover_image = f"projects/project_{p.id}.webp"
                p.image_alt = f"{p.project_name} - 學員 {p.student_name} 專題作品首頁成果"
                p.save(update_fields=['cover_image', 'image_alt'])
                sync_to_cloudinary(p.id, server_file)
                success_count += 1
            else:
                print(f"  ❌ 專案 {p.project_name} 截圖失敗")
                
            time.sleep(0.5)
    finally:
        driver.quit()
        
    print(f"\n🎉 批次處理完成！共成功完成 {success_count}/{total} 個專案截圖與資料庫更新！\n")

if __name__ == '__main__':
    main()
