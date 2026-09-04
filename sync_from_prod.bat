@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵線上資料與圖片同步工具

echo ==============================================================================
echo   正在從線上 Render 伺服器同步最新 CMS 資料與圖片至本地端...
echo ==============================================================================
echo.

cd /d "%~dp0server"

set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% sync_from_prod.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] 同步過程發生錯誤，請確認網路連線或線上伺服器狀態。
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ==============================================================================
echo   [OK] 線上最新資料與高畫質圖片已全數同步至本地端！
echo   您現在可以在本地執行 run_dev.bat 查看最新內容。
echo ==============================================================================
echo.
pause
