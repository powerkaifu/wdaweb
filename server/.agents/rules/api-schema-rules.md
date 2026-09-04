---
trigger: always_on
---

# Django Ninja API Schema 與 Router 規範

## Schema 命名規範

- 輸出 Schema 後綴使用 Out（例：AdmissionBatchOut、FAQOut）。
- 輸入 Schema 後綴使用 In（例：BatchClickIn）。
- Schema 欄位名稱必須與 Model 欄位名稱一致。

## Router 規範

- 所有公開 API 必須放置於 /api/v1/public/ 路由前綴下。
- GET 端點命名：`get_模型複數名稱`（例：get_batches、get_faqs）。
- POST 追蹤端點命名：`track_動作名稱`（例：track_batch_click、track_project_view）。
- Router 函式中只允許進行直接的 ORM 查詢與序列化，複雜業務邏輯應抽離至 Model method 或 Service 函式。

## 回傳格式規範

- 列表資料回傳 List[XxxOut]。
- 追蹤操作（點擊、瀏覽計數）回傳統一格式：{"success": true, "count": 新數量}。
- 所有端點必須有對應的 response 型別標記。

## 圖片 URL 處理

- Schema 中的圖片欄位使用 Optional[str] 型別，在 resolve_image 方法中使用 request.build_absolute_uri() 建立完整 URL。
- 禁止直接回傳相對路徑，前台需要完整 https:// 開頭的絕對 URL。