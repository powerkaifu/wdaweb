@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵資料庫備份工具

echo ==============================================================================
echo   正在備份 泰山職訓 CMS 內容資料庫 (含期別、課綱、學員作品、FAQ、站台設定)...
echo ==============================================================================
echo.

cd /d %~dp0server

set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% -Xutf8 manage.py dumpdata cms --indent 2 --output ..\cms_data_backup.json

if %ERRORLEVEL% EQU 0 (
    if exist media (
        echo.
        echo   正在同步媒體檔案至 static 目錄...
        xcopy /E /I /Y /Q media static >nul 2>&1
    )
    echo.
    echo ==============================================================================
    echo   [OK] 資料庫備份與媒體同步成功！
    echo   輸出檔案路徑： %~dp0cms_data_backup.json
    echo.
    echo   【下一步：推送至 GitHub 即可全站生效】：
    echo     1. git add .
    echo     2. git commit -m "更新網站圖文內容"
    echo     3. git push origin main
    echo ==============================================================================
) else (
    echo.
    echo [ERROR] 備份失敗，請確認虛擬環境或資料庫是否正常。
)

echo.
pause
