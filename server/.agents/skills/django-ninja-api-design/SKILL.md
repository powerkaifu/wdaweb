---
name: django-ninja-api-design
description: Django Ninja 現代型別化 RESTful API 設計與 Swagger 文件規範。當在後端新增 API 端點、設計 Schema、調整路由或對齊前後端介面時啟動。
---

# 技能：Django Ninja 高效型別化 API 架構規範

## 1. 三層分層原則
1. **`models.py` (資料層)**：欄位定義、軟刪除基底、Meta 排序與驗證，不混寫業務路由。
2. **`schemas.py` (型別層)**：使用 Pydantic / Ninja `Schema`，明確定義輸入 `XxxIn` 與輸出 `XxxOut`。
3. **`routers.py` (路由層)**：宣告 `@api.get()` / `@api.post()`，負責 ORM 查詢、序列化與異常處理。

## 2. API 路由命名與安全規範
- **公開前台端點**：統一掛載於 `/api/v1/public/` 前綴下，不需登入即可存取。
- **媒體檔案絕對網址**：圖片 URL 欄位在 Schema/Router 中透過 `request.build_absolute_uri()` 轉換為完整 URL。
- **轉換追蹤端點**：POST 追蹤操作回傳統一格式 `ApiResponse(success=True, message=...)`。
