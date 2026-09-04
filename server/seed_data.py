import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from apps.cms.models import (
    Carousel, AdmissionBatch, CurriculumModule, TechCard,
    Facility, StudentProject, FAQ, SiteSetting
)
from datetime import date

print("=== 開始植入種子資料 ===")

# 1. 建立單一超級管理員
if not User.objects.filter(username="admin").exists():
    admin_user = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    admin_email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@wdaweb.gov.tw")
    admin_pass = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Taishan@2026#Admin")
    User.objects.create_superuser(admin_user, admin_email, admin_pass)
    print(f"[OK] 管理員帳號建立成功：{admin_user}")
else:
    print("[INFO] 管理員帳號已存在")

# 2. 全域站台設定
site, _ = SiteSetting.objects.get_or_create(id=1)
site.site_title = "泰山職訓－前端網頁技術與AI應用"
site.seo_description = "勞動部勞動力發展署北基宜花金馬分署－泰山職業訓練場「前端網頁技術與AI應用」專班。920 小時紮實養成、待業者享 100% 全額免費培訓與每月職訓生活津貼補助，一人配置獨立雙螢幕電腦，輔導專題實作與就業媒合。官方諮詢專線：(02) 2901-8274。"
site.seo_keywords = "泰山職訓, 前端網頁技術與AI應用, 泰山職業訓練場, 勞動部職訓, 前端工程師培訓, 網頁設計課程, 免費職訓課程, 職訓生活津貼, 待業者全額免費, Vue3課程, TypeScript職訓, AI網頁開發, 轉職前端工程師, 青年職訓補助, 台灣就業通, 北分署職訓"
site.announcement_bar_enabled = True
site.announcement_text = "🔥 第 1 期熱烈招生中！待業民眾享全額免費受訓與生活津貼補助！"
site.announcement_link = "#batches"
site.contact_phone = "(02) 2901-8274"
site.contact_address = "新北市泰山區貴子里致遠新村 55 之 1 號"
site.footer_copyright = "本網站為前端班師資自主推廣與學員成果展示網頁"
site.save()
print("[OK] 站台全域設定已更新標題為：泰山職訓－前端網頁技術與AI應用")

# 3. 首頁輪播圖 (精準 3 筆黃金輪播圖保證)
carousels_data = [
    (1, "從零開始的前端工程師養成", "政府自辦 920 小時紮實培訓 ｜ 待業者完全免費 ｜ 輔導就業與生活津貼", "泰山職訓前端網頁技術與AI應用班主視覺", "立即線上報名", "#batches", 1),
    (2, "現代前端框架與 AI 協同開發", "一人兩機雙螢幕教學設備 ｜ 打造 AI 應用的優秀作品集 ｜ 跨領域轉職最佳起點", "泰山職訓雙螢幕教室實境", "立即線上報名", "#batches", 2),
    (3, "打造專屬的個人全端作品集", "獨立完成全端架構 ｜ 實踐 AI 工具輔助開發 ｜ 累積求職競爭力的實戰作品集", "泰山職訓跨領域轉職前端網頁成果", "立即線上報名", "#batches", 3),
]
Carousel.objects.exclude(id__in=[1, 2, 3]).delete()
for cid, title, sub, alt, cta, link, order in carousels_data:
    Carousel.objects.update_or_create(
        id=cid,
        defaults={
            "title": title,
            "subtitle": sub,
            "image_alt": alt,
            "cta_text": cta,
            "cta_link": link,
            "cta_target": "_self",
            "sort_order": order,
            "is_active": True,
            "deleted_at": None
        }
    )
print("[OK] 首頁 3 筆黃金輪播圖精準同步完成")

# 4. 招生期別 (第 1 期 & 第 2 期 - 精準官方數據保證)
AdmissionBatch.objects.update_or_create(
    course_code="159268",
    defaults={
        "batch_name": "前端網頁技術與AI應用（第 1 期）",
        "total_hours": 920,
        "enroll_start_date": date(2025, 12, 4),
        "enroll_end_date": date(2026, 2, 25),
        "screening_date": date(2026, 3, 11),
        "training_start_date": date(2026, 3, 25),
        "training_end_date": date(2026, 9, 10),
        "planned_trainees": 24,
        "applicants_count": 36,
        "apply_url": "https://its.taiwanjobs.gov.tw/Course/Detail?ID=159268",
        "status_override": "auto",
        "sort_order": 1
    }
)
AdmissionBatch.objects.update_or_create(
    course_code="159269",
    defaults={
        "batch_name": "前端網頁技術與AI應用（第 2 期）",
        "total_hours": 920,
        "enroll_start_date": date(2026, 5, 7),
        "enroll_end_date": date(2026, 8, 21),
        "screening_date": date(2026, 9, 3),
        "training_start_date": date(2026, 9, 23),
        "training_end_date": date(2027, 3, 24),
        "planned_trainees": 24,
        "applicants_count": 38,
        "apply_url": "https://its.taiwanjobs.gov.tw/Course/Detail?ID=159269",
        "status_override": "auto",
        "sort_order": 2
    }
)
print("[OK] 招生期別精準官方數據（第 1 期 36 人、第 2 期 38 人）同步完成")

# 5. 7 大課程模組 (M1 ~ M7)
modules = [
    ("M1", "一般與共同課程", 53, "基礎與設計", "就業市場分析、勞動法規與權益、性別主流化與職場倫理、職涯資源與求職準備。"),
    ("M2", "網頁排版編輯", 160, "基礎與設計", "HTML5 語意化結構、CSS3 現代排版佈局、Bootstrap 響應式框架、RWD 跨裝置自適應設計、VS Code 開發環境配置。"),
    ("M3", "視覺影像設計", 120, "基礎與設計", "Adobe Photoshop 數位影像編修、網頁版面視覺規劃與調色修圖、Adobe Illustrator 貝茲曲線繪圖、向量圖標與 Web Icon 製作。"),
    ("M4", "數位媒體應用", 107, "基礎與設計", "視覺傳達設計基礎、UI/UX 介面設計與使用者體驗流程、原型設計工具應用、企業參訪與業界職場體驗。"),
    ("M5", "網頁動態技術", 240, "前端核心與框架", "JavaScript 核心語法與 ES6+、DOM 原生操作與前端動態互動、RESTful API 非同步資料串接、Git 版本控制與 GitHub 協同開發、Vue.js 漸進式框架與 Pinia 狀態管理。"),
    ("M6", "資料庫程式設計", 80, "後端與資料庫", "NoSQL 資料庫概念與操作、MongoDB 資料管理與塑模、Node.js 執行環境、NPM 套件管理與基礎後端 API 整合測試。"),
    ("M7", "網頁設計實務", 160, "專案實務與作品", "前端專案專題製作、前後端 API 整合實務、GitHub Pages 雲端部署發布、成果簡報發表與作品集指導。")
]
for idx, (num, name, hrs, cat, desc) in enumerate(modules, 1):
    CurriculumModule.objects.update_or_create(
        module_number=num,
        defaults={
            "module_name": name,
            "hours": hrs,
            "category_tab": cat,
            "description": desc,
            "sort_order": idx,
            "deleted_at": None
        }
    )
print("[OK] 7 大課程模組精準同步完成")

# 6. 技術單元卡片
if not TechCard.objects.exists():
    techs = [
        ("基礎與排版", "HTML5 & CSS3", "現代網頁語意標籤與進階排版"),
        ("基礎與排版", "Bootstrap & Tailwind", "現代前端 UI 框架、快速建立高質感響應式 (RWD) 介面"),
        ("視覺與設計", "Adobe Photoshop & AI", "影像處理修圖、Icon 圖示設計與 UI/UX 視覺傳達流程"),
        ("核心動態技術", "JavaScript (ES6+)", "原生 DOM 操作、非同步 Promise / Async-Await 與現代語法"),
        ("核心動態技術", "Vue.js 3 & Pinia", "組件化架構、Composition API、Vue Router 路由與狀態管理"),
        ("核心動態技術", "RESTful API & Axios", "前後端分離資料串接、JSON 處理與非同步請求處理"),
        ("環境與資料管理", "Node.js & MongoDB", "Node.js 執行環境、NoSQL 資料庫設計與基礎 API 開發"),
        ("協同開發", "Git & GitHub", "版本控制、分支管理、團隊協同開發與 GitHub Pages 部署")
    ]
    for idx, (cat, name, desc) in enumerate(techs, 1):
        TechCard.objects.create(
            category_tab=cat,
            tech_name=name,
            image_alt=f"{name} 技術圖標",
            description=desc,
            sort_order=idx
        )
    print("[OK] 核心技術卡片建立完成")

# 7. 教學設施
if not Facility.objects.exists():
    Facility.objects.create(
        facility_name="雙螢幕教學設備",
        description="一人配置雙螢幕電腦，邊看講師即時示範邊同步動手編程，學習不漏拍！",
        image_alt="泰山職訓雙螢幕電腦教室",
        sort_order=1
    )
    Facility.objects.create(
        facility_name="寬敞明亮專屬實作空間",
        description="專屬獨立座位與高速光纖網路，提供 920 小時專注沉浸式程式開發環境。",
        image_alt="寬敞明亮的教室實作環境",
        sort_order=2
    )
    print("[OK] 教學環境設施建立完成")

# 8. 14 組前後端分離＋資料庫學員專案作品
if not StudentProject.objects.exists():
    projects = [
        ("蔡昀容", "夢百貨", "https://blackcat0708.github.io/DreamDepartmentStore-front/#/", True),
        ("董元琪", "Matching TRPG", "https://chichitung.github.io/MatchingTRPG-front/#/", True),
        ("仲崇安", "Voice Land", "https://josh19961201.github.io/VoiceLand_front/#/", True),
        ("楊詠茜", "桌下吧", "https://cloris222.github.io/quasar-project/#/", True),
        ("黃姿瑄", "團購趣", "https://a733181.github.io/2022-buytogether/#/", False),
        ("許凱炫", "一個地方", "https://qweasd333ee.github.io/a-place-bar-front/", False),
        ("徐嘉伶", "AZ.ZERO", "https://lisia229.github.io/AZFront/#/", False),
        ("郭思緯", "Show Time", "https://kkone0275.github.io/top-free-time-front/#/", False),
        ("王政文", "Ocean", "https://nailshort.github.io/Ocean-front/#/", False),
        ("胡俊宇", "揪遊 (JoYo)", "https://lilmax922.github.io/JoYo-Front/#/", False),
        ("張雅涵", "Sunday", "https://vvn719.github.io/SUNDAY-vue-project/#/", False),
        ("黃佳琦", "綠善生活農場", "https://gagiherdesign.github.io/susi-front/#/", False),
        ("蔡文瑜", "BCoffee", "https://pato830729.github.io/BCcoffee-front/#/", False),
        ("蘇俞甄", "MAUNA COFFEE", "https://a5a5aa.github.io/TSFP-front/#/", False),
    ]
    for idx, (name, title, demo, feat) in enumerate(projects, 1):
        StudentProject.objects.create(
            student_name=name,
            batch_tag="前端專班結訓成果",
            project_name=title,
            image_alt=f"{name} 專案作品 - {title}",
            demo_url=demo,
            is_featured=feat,
            sort_order=idx
        )
    print("[OK] 14 組前後端分離＋資料庫學員專題作品建立完成")

# 9. FAQ 常見問答
if not FAQ.objects.exists():
    faqs = [
        ("參訓資格", "完全沒有寫過程式或設計基礎，適合報名嗎？", "非常適合！本課程專為零基礎及跨領域轉職者設計，從最基礎的 HTML/CSS 排版與影像工具教起，循序漸進至 JavaScript 與 Vue.js 動態框架，只要具備學習熱忱皆可報名。"),
        ("生活津貼", "受訓期間可以申請職業訓練生活津貼嗎？", "符合特定對象資格（如非自願離職者、中高齡待業者、獨力負擔家計者、身心障礙者、原住民等），經公立就業服務機構推介參訓，受訓期間每月可申請基本工資 60% 之職業訓練生活津貼！"),
        ("參訓費用", "這門課程真的完全免費嗎？需要負擔其他材料費嗎？", "政府自辦職前訓練班，待業者經甄試錄取後，學費由政府全額補助（100% 免費）。"),
        ("上課時間", "每天上課的時間與受訓時數為何？", "本班為日間全日制培訓，週一至週五 08:30 ~ 16:30（每天 8 小時），總受訓時數為 920 小時（包含 160 小時專題製作與輔導發表）。"),
        ("就業輔導", "結訓前會提供履歷健檢與作品集指導嗎？", "會的！課程結訓前夕將由專業師資個別提供一對一履歷健檢、作品集面試優化指導，並舉辦專題成果發表會，協助學員以具備競爭力的完整作品集底氣十足接軌就業市場。")
    ]
    for idx, (cat, q, a) in enumerate(faqs, 1):
        FAQ.objects.create(
            category=cat,
            question=q,
            answer=a,
            sort_order=idx
        )
    print("[OK] 常見問答 (FAQ) 資料建立完成")

print("=== 所有種子資料植入成功 ===")
