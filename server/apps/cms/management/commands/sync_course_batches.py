import json
from django.core.management.base import BaseCommand
from apps.cms.services.batch_sync import sync_admission_batches

class Command(BaseCommand):
    help = "從台灣就業通追蹤系統同步前端網頁技術與AI應用課程報名最新資訊"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("[INFO] 開始同步「前端網頁技術與AI應用」期別報名資訊..."))
        result = sync_admission_batches()
        if result["success"]:
            self.stdout.write(self.style.SUCCESS(
                f"[SUCCESS] 同步成功！新增 {result['created']} 筆，更新 {result['updated']} 筆。"
            ))
            for b in result["synced_batches"]:
                self.stdout.write(
                    f"   - [{b['action'].upper()}] {b['batch_name']} (代碼: {b['course_code']}) | 報名人數: {b['applicants']}/{b['planned']} | 狀態: {b['status']}"
                )
        else:
            self.stdout.write(self.style.ERROR(
                f"[ERROR] 同步失敗: {', '.join(result['errors'])}"
            ))
