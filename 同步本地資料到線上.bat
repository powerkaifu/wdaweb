@echo off
chcp 65001 >nul
title 泰山職訓 CMS 本地資料同步至線上工具

echo ==============================================================================
echo   正在將本地端 CMS 最新資料打包為備份包 (cms_data_backup.json)...
echo ==============================================================================
echo.

cd /d "%~dp0server"

set PYTHONUTF8=1
set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% -Xutf8 manage.py sync_to_deploy

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] 同步作業發生錯誤，請確認本地環境與資料庫狀態。
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ==============================================================================
echo   [OK] 本地資料已成功打包！(檔案：cms_data_backup.json)
echo.
echo   接下來，只要在終端機輸入這三行推送到 GitHub，線上就會自動同步：
echo     git add .
echo     git commit -m "chore: 同步本地最新資料與設定至線上"
echo     git push
echo ==============================================================================
echo.
pause
