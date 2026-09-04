# 工作流：標準 Git Commit 流程

觸發條件：使用者說「幫我 commit」或「提交」或「記錄變更」。

## 執行步驟

### Step 1：影響範圍自我檢查
執行 `git status` 確認本次變更的所有檔案清單。
分析變更是否涉及核心模組（models.py / types/index.ts / routers.py），
若有，強制使用 grep_search 確認所有依賴端皆已同步更新。

### Step 2：程式碼品質確認
- 前台：確認 `npm run build` 可成功通過 TypeScript 編譯（零錯誤）。
- 後端：確認 Django 啟動無錯誤（python manage.py check）。
- 移除所有臨時 console.log 與 print 除錯語句。

### Step 3：執行 Commit
```
git add .
git commit -m "繁體中文 Commit 訊息"
```

### Step 4：提醒使用者手動 Push
**絕對禁止自動執行 git push。**
Commit 完成後，告知使用者可手動執行：
```
git push origin main
```