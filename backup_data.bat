@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵資料庫備份工具

echo ==============================================================================
echo   正在備份 泰山職訓 CMS 內容資料庫 (含期別、課綱、學員作品、FAQ、站台設定)...
echo ==============================================================================
echo.

cd /d %~dp0server
venv\Scripts\python.exe -Xutf8 manage.py dumpdata cms --indent 2 --output ..\cms_data_backup.json

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ==============================================================================
    echo   [OK] 資料庫備份成功！
    echo   備份檔案路徑： %~dp0cms_data_backup.json
    echo ==============================================================================
) else (
    echo.
    echo [ERROR] 備份失敗，請確認虛擬環境或資料庫是否正常。
)

echo.
pause
