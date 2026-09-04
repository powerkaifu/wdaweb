@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵資料庫還原工具

echo ==============================================================================
echo   正在還原 泰山職訓 CMS 內容資料庫...
echo ==============================================================================
echo.

if not exist "%~dp0cms_data_backup.json" (
    echo [ERROR] 找不到備份檔案：%~dp0cms_data_backup.json
    echo 請確認備份檔案是否存在於專案根目錄中。
    pause
    exit /b 1
)

cd /d %~dp0server
venv\Scripts\python.exe -Xutf8 manage.py loaddata ..\cms_data_backup.json

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==============================================================================
    echo   [OK] 資料庫還原成功！所有期別、作品與設定已同步至最新狀態。
    echo ==============================================================================
) else (
    echo.
    echo [ERROR] 還原失敗，請檢查資料結構或 Migration 狀態。
)

echo.
pause
