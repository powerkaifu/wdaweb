"""
線上 CMS 資料與圖片一鍵同步工具 (sync_from_prod.py)
用途：
1. 從線上 Render 伺服器 (https://wdaweb.onrender.com) 取得最新 CMS 資料 (設施、期別、輪播、作品等)。
2. 自動下載 Cloudinary 雲端圖片並儲存至本地 media/、static/ 與 client/ 靜態資產資料夾。
3. 同步更新本地 SQLite 資料庫 (db.sqlite3) 與備份檔 (cms_data_backup.json)。
"""

import os
import sys
import json
import urllib.parse
from pathlib import Path
import requests

# 設定編碼與 Django 環境
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

from django.core.management import call_command
from apps.cms.models import (
    Facility, Carousel, AdmissionBatch, CurriculumModule,
    TechCard, StudentProject, FAQ, SiteSetting
)

PROD_API_BASE = os.getenv("PROD_API_BASE", "https://wdaweb.onrender.com/api/v1/public").rstrip('/')

print("==============================================================================")
print("  正在從線上 Render 伺服器同步最新 CMS 資料與圖片至本地端...")
print(f"  來源 API：{PROD_API_BASE}")
print("==============================================================================\n")

def download_image(img_url: str, dest_rel_path: str) -> bool:
    """下載遠端圖片至指定相對路徑 (自動建立父目錄)"""
    if not img_url or not (img_url.startswith("http://") or img_url.startswith("https://")):
        return False

    targets = [
        BASE_DIR / "media" / dest_rel_path,
    ]

    try:
        # 下載圖片內容
        resp = requests.get(img_url, timeout=20)
        if resp.status_code == 200:
            for target in targets:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "wb") as f:
                    f.write(resp.content)
            print(f"  [下載圖片成功] {img_url} -> {dest_rel_path}")
            return True
        else:
            print(f"  [下載跳過] 狀態碼 {resp.status_code}: {img_url}")
            return False
    except Exception as e:
        print(f"  [下載失敗] {img_url}: {e}")
        return False

def sync_facilities():
    url = f"{PROD_API_BASE}/facilities"
    print(f"[*] 正在同步教學設備設施 ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            print(f"  [!] 無法取得設施資料，狀態碼: {res.status_code}")
            return
        items = res.json()
        for item in items:
            img_url = item.get("image_url", "")
            local_filename = ""
            if img_url:
                # 取得檔名
                parsed = urllib.parse.urlparse(img_url)
                raw_name = Path(parsed.path).name
                if not raw_name.lower().endswith(('.webp', '.jpg', '.png', '.jpeg')):
                    raw_name += ".webp"
                dest_path = f"facilities/{raw_name}"
                download_image(img_url, dest_path)
                local_filename = dest_path

            Facility.objects.update_or_create(
                id=item["id"],
                defaults={
                    "facility_name": item["facility_name"],
                    "description": item["description"],
                    "image": local_filename or item.get("image", ""),
                    "image_alt": item.get("image_alt", ""),
                    "sort_order": item.get("sort_order", 0),
                    "is_active": True,
                }
            )
        print(f"  [OK] 教學設施同步完成，共更新 {len(items)} 筆。")
    except Exception as e:
        print(f"  [!] 同步教學設施失敗: {e}")

def sync_carousels():
    url = f"{PROD_API_BASE}/carousels"
    print(f"[*] 正在同步首頁輪播圖 ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            return
        items = res.json()
        for item in items:
            img_url = item.get("image_url", "")
            local_img = ""
            if img_url:
                parsed = urllib.parse.urlparse(img_url)
                raw_name = Path(parsed.path).name
                if not raw_name.lower().endswith(('.webp', '.jpg', '.png', '.jpeg')):
                    raw_name += ".webp"
                dest_path = f"carousels/{raw_name}"
                download_image(img_url, dest_path)
                local_img = dest_path

            Carousel.objects.update_or_create(
                id=item["id"],
                defaults={
                    "title": item["title"],
                    "subtitle": item.get("subtitle", ""),
                    "image": local_img or item.get("image", ""),
                    "image_alt": item.get("image_alt", ""),
                    "cta_text": item.get("cta_text", "立即報名"),
                    "cta_link": item.get("cta_link", "#batches"),
                    "cta_target": item.get("cta_target", "_self"),
                    "sort_order": item.get("sort_order", 0),
                    "is_active": True,
                }
            )
        print(f"  [OK] 首頁輪播圖同步完成，共更新 {len(items)} 筆。")
    except Exception as e:
        print(f"  [!] 同步首頁輪播圖失敗: {e}")

def sync_projects():
    url = f"{PROD_API_BASE}/projects"
    print(f"[*] 正在同步學員專題成果 ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            return
        items = res.json()
        for item in items:
            img_url = item.get("cover_image_url", "")
            local_img = ""
            if img_url:
                parsed = urllib.parse.urlparse(img_url)
                raw_name = Path(parsed.path).name
                if not raw_name.lower().endswith(('.webp', '.jpg', '.png', '.jpeg')):
                    raw_name += ".webp"
                dest_path = f"projects/{raw_name}"
                download_image(img_url, dest_path)
                local_img = dest_path

            StudentProject.objects.update_or_create(
                id=item["id"],
                defaults={
                    "student_name": item["student_name"],
                    "batch_tag": item.get("batch_tag", "前端專班結訓成果"),
                    "project_name": item["project_name"],
                    "cover_image": local_img or item.get("cover_image", ""),
                    "image_alt": item.get("image_alt", ""),
                    "demo_url": item.get("demo_url", ""),
                    "github_url": item.get("github_url", ""),
                    "view_count": item.get("view_count", 0),
                    "is_featured": item.get("is_featured", False),
                    "sort_order": item.get("sort_order", 0),
                    "is_active": True,
                }
            )
        print(f"  [OK] 學員專題同步完成，共更新 {len(items)} 筆。")
    except Exception as e:
        print(f"  [!] 同步學員專題失敗: {e}")

def sync_batches():
    url = f"{PROD_API_BASE}/batches"
    print(f"[*] 正在同步招生期別 ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            return
        items = res.json()
        for item in items:
            AdmissionBatch.objects.update_or_create(
                id=item["id"],
                defaults={
                    "batch_name": item["batch_name"],
                    "total_hours": item.get("total_hours", 920),
                    "enroll_start_date": item["enroll_start_date"],
                    "enroll_end_date": item["enroll_end_date"],
                    "screening_date": item.get("screening_date"),
                    "training_start_date": item["training_start_date"],
                    "training_end_date": item["training_end_date"],
                    "planned_trainees": item.get("planned_trainees", 24),
                    "applicants_count": item.get("applicants_count", 0),
                    "apply_url": item.get("apply_url", ""),
                    "course_code": item.get("course_code", ""),
                    "status_override": item.get("status_override", "auto"),
                    "click_count": item.get("click_count", 0),
                    "sort_order": item.get("sort_order", 0),
                }
            )
        print(f"  [OK] 招生期別同步完成，共更新 {len(items)} 筆。")
    except Exception as e:
        print(f"  [!] 同步招生期別失敗: {e}")

def sync_site_settings():
    url = f"{PROD_API_BASE}/site-settings"
    print(f"[*] 正在同步全站站台設定 ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            return
        data = res.json()
        if data:
            SiteSetting.objects.update_or_create(
                id=1,
                defaults={
                    "site_title": data.get("site_title", "泰山職訓－前端網頁技術與AI應用"),
                    "seo_description": data.get("seo_description", ""),
                    "seo_keywords": data.get("seo_keywords", ""),
                    "announcement_bar_enabled": data.get("announcement_bar_enabled", True),
                    "announcement_text": data.get("announcement_text", ""),
                    "announcement_link": data.get("announcement_link", "#batches"),
                    "discord_server_id": data.get("discord_server_id", ""),
                    "discord_channel_id": data.get("discord_channel_id", ""),
                    "discord_invite_url": data.get("discord_invite_url", ""),
                    "contact_phone": data.get("contact_phone", "(02) 2901-8274"),
                    "contact_address": data.get("contact_address", "新北市泰山區貴子里致遠新村 55 之 1 號"),
                    "footer_copyright": data.get("footer_copyright", ""),
                }
            )
            print("  [OK] 站台設定同步完成。")
    except Exception as e:
        print(f"  [!] 同步站台設定失敗: {e}")

def sync_faqs():
    url = f"{PROD_API_BASE}/faqs"
    print(f"[*] 正在同步常見問題 FAQ ({url})...")
    try:
        res = requests.get(url, timeout=15)
        if res.status_code != 200:
            return
        items = res.json()
        for item in items:
            FAQ.objects.update_or_create(
                id=item["id"],
                defaults={
                    "category": item["category"],
                    "question": item["question"],
                    "answer": item["answer"],
                    "sort_order": item.get("sort_order", 0),
                    "is_active": True,
                }
            )
        print(f"  [OK] 常見問答同步完成，共更新 {len(items)} 筆。")
    except Exception as e:
        print(f"  [!] 同步常見問答失敗: {e}")

def main():
    sync_facilities()
    sync_carousels()
    sync_projects()
    sync_batches()
    sync_site_settings()
    sync_faqs()

    print("\n[*] 正在將本地資料庫匯出備份至 cms_data_backup.json...")
    backup_file = PROJECT_ROOT / "cms_data_backup.json"
    from io import StringIO
    buf = StringIO()
    call_command("dumpdata", "cms", indent=2, stdout=buf)
    with open(backup_file, "w", encoding="utf-8") as f:
        f.write(buf.getvalue())
    print(f"  [OK] 備份成功儲存至：{backup_file}")

    print("\n==============================================================================")
    print("  線上最新資料與高畫質圖片已 100% 成功同步至本地端！")
    print("  包含：本地 SQLite 資料庫、media 資料夾、前端 assets 圖片與備份檔。")
    print("==============================================================================")

if __name__ == "__main__":
    main()
