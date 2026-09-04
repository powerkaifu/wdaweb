@echo off
chcp 65001 >nul
title 泰山職訓 CMS 本地資料同步至線上工具

echo ==============================================================================
echo   正在將本地端 CMS 最新資料打包為備份包 (cms_data_backup.json)...
echo ==============================================================================
echo.

cd /d "%~dp0server"

set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% manage.py dumpdata cms --natural-foreign --natural-primary --indent 2 -o ../cms_data_backup.json

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] 打包資料時發生錯誤，請確認本地虛擬環境與資料庫狀態。
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ==============================================================================
echo   [OK] 本地資料已成功打包！(檔案：cms_data_backup.json)
echo.
echo   接下來，只要將這個檔案推送到 GitHub，線上 Render 就會自動載入：
echo     1. git add cms_data_backup.json
echo     2. git commit -m "chore: 同步本地資料至線上"
echo     3. git push
echo ==============================================================================
echo.
pause
