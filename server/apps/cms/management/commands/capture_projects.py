# -*- coding: utf-8 -*-
"""
Django 管理命令：自動無頭爬取學員專題線上 Demo 首頁並上傳縮圖至 CDN
使用方式：
    python manage.py capture_projects         # 只處理缺少縮圖的新增專案
    python manage.py capture_projects --all   # 強制重新截取全部專案
"""
from django.core.management.base import BaseCommand
from apps.cms.services.screenshot_service import capture_missing_projects


class Command(BaseCommand):
    help = "使用無頭 Chrome 自動訪問學員專題 Demo 網址、截圖並同步至 Cloudinary CDN 與本地靜態目錄"

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='強制重新截取所有專案，即使已有封面圖',
        )

    def handle(self, *args, **options):
        force_all = options.get('all', False)
        mode_text = "全部專案" if force_all else "缺少封面縮圖的專案"
        self.stdout.write(self.style.NOTICE(f"[INFO] 開始自動截圖學員專案成果 ({mode_text})..."))

        success_count, total = capture_missing_projects(force_all=force_all)

        if total == 0:
            self.stdout.write(self.style.SUCCESS("[INFO] 目前沒有需要處理的專案（所有專案皆已有封面圖）。若需重新截取請加上 --all 參數。"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"[SUCCESS] 處理完成！共成功截取並同步 {success_count}/{total} 個專案！"
            ))
