# 工作流：新增後端 API 端點完整流程

觸發條件：使用者說「新增 API」、「新增後台功能」或「我要前台能顯示 X 資料」。

## 決策：是否需要新增 Model？

- 若需要新的資料表 → 觸發 add-cms-model 技能執行完整端對端流程。
- 若只需要新的查詢端點（資料已存在） → 從 Step 3 開始執行。

## 執行步驟

### Step 1（若需要）：新增 Model
參考 add-cms-model 技能完成 Model、Admin、Migration。

### Step 2（若需要）：植入種子資料
參考 seed-data 技能植入初始資料。

### Step 3：新增 Schema
在 `server/apps/api/schemas.py` 新增對應的輸出 Schema。

### Step 4：新增 Router 端點
在 `server/apps/api/routers.py` 新增對應的 GET 端點。

### Step 5：驗證後端 API
確認 http://127.0.0.1:8000/api/v1/docs 中新端點可正確回傳資料。

### Step 6：通知前端接入
提示使用者接著執行前台的 api-integration 技能完成前台串接。

## 完成定義（Definition of Done）

- [ ] Model 已建立（若需要）
- [ ] Migration 已成功執行
- [ ] Schema 已定義輸出型別
- [ ] Router 端點已新增
- [ ] Swagger 文件中可成功測試新端點
- [ ] 前台已串接並正確顯示資料