@echo off
chcp 65001 >nul
title 泰山職訓「前端網頁技術與AI應用」前後端一鍵啟動器

echo ==============================================================================
echo   正在啟動 泰山職訓「前端網頁技術與AI應用」前後端開發伺服器...
echo ==============================================================================
echo.

:: 1. 啟動 Django 後端伺服器 (在新視窗中執行)
echo [1/2] 正在啟動 Django 後端 API 與 Admin 管理後台 (Port 8000)...
start "泰山職訓 - Django 後端 API (Port 8000)" cmd /k "cd /d %~dp0server && venv\Scripts\activate && python manage.py runserver 8000"

:: 等待 2 秒確保後端啟動
timeout /t 2 /nobreak >nul

:: 2. 啟動 Vue 3 前台開發伺服器 (在新視窗中執行)
echo [2/2] 正在啟動 Vue 3 前台展示網站 (Port 5173)...
start "泰山職訓 - Vue 3 前台網站 (Port 5173)" cmd /k "cd /d %~dp0client && npm run dev"

echo.
echo ==============================================================================
echo   前後端服務已全數於獨立視窗中啟動！
echo ==============================================================================
echo   前台網站首頁   : http://localhost:5173
echo   管理員後台     : http://127.0.0.1:8000/admin/
echo   API Swagger文件: http://127.0.0.1:8000/api/v1/docs
echo ==============================================================================
echo.

:: 3. 自動在預設瀏覽器打開前台與後台管理頁面
timeout /t 3 /nobreak >nul
start http://localhost:5173
start http://127.0.0.1:8000/admin/

exit
