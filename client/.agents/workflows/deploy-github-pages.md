# 工作流：GitHub Pages 部署上線

觸發條件：使用者說「部署前台」、「上線網站」或「發布到 GitHub Pages」。

## 執行步驟

### Step 1：部署前品質確認
- 執行 `npm run build` 確認 TypeScript 零錯誤，打包成功。
- 確認 `client/.env.production` 中的 VITE_API_BASE_URL 已指向 Render 正式後端網址（非 localhost）。
- 執行 a11y-audit 技能進行無障礙快速稽核。

### Step 2：設定確認
確認以下設定正確：
- client/vite.config.ts 的 base 設定為 './'
- .github/workflows/deploy.yml 的工作流設定正確無誤

### Step 3：執行 Git Commit 並推送

  git add .
  git commit -m "feat: 更新前台部署內容"

提醒使用者手動執行：

  git push origin main

### Step 4：監看 GitHub Actions 狀態
告知使用者前往以下路徑確認 CI/CD 執行狀態：
- GitHub Repository → Actions → Deploy Vue 3 Frontend to GitHub Pages

### Step 5：確認上線
部署成功後，確認網站可在以下網址正常訪問：
- https://使用者帳號.github.io/專案名稱/