@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵從線上同步回本地端

echo ==============================================================================
echo   正在從線上 Render 伺服器同步最新 CMS 資料與圖片至本地端...
echo   (包含：資料庫 SQLite、Cloudinary 實體圖片下載、本地靜態資產、備份檔)
echo ==============================================================================
echo.

cd /d %~dp0server

set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% sync_from_prod.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==============================================================================
    echo   [OK] 線上資料與圖片已全數同步至本地端！
    echo   您現在可以在本地執行 run_dev.bat 預覽最新同步內容。
    echo ==============================================================================
) else (
    echo.
    echo [ERROR] 同步過程發生錯誤，請確認網路連線或線上 Render 伺服器狀態。
)

echo.
pause
