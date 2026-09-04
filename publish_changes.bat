@echo off
chcp 65001 >nul
title 泰山職訓 CMS 一鍵雲端發布助手

echo ==============================================================================
echo   【泰山職訓 CMS 一鍵雲端發布助手】
echo   正在備份本地資料庫並同步媒體檔案...
echo ==============================================================================
echo.

cd /d %~dp0server

set PYTHON_EXE=venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

%PYTHON_EXE% -Xutf8 manage.py dumpdata cms --indent 2 --output ..\cms_data_backup.json

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] 資料庫備份失敗，請確認虛擬環境或資料庫是否正常。
    pause
    exit /b %ERRORLEVEL%
)

if exist media (
    echo   正在同步媒體檔案至 static 目錄...
    xcopy /E /I /Y /Q media static >nul 2>&1
)

cd /d %~dp0

echo.
echo ==============================================================================
echo   [OK] 本地資料庫備份與媒體同步完成！
echo ==============================================================================
echo.

set /p COMMIT_MSG="請輸入更新說明 (直接按 Enter 預設為「更新網站圖文內容」): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=更新網站圖文內容

git add .
git commit -m "%COMMIT_MSG%"

echo.
set /p PUSH_NOW="是否立即推送到 GitHub 雲端 (Y/N)？[預設 Y]: "
if /i "%PUSH_NOW%"=="" set PUSH_NOW=Y
if /i "%PUSH_NOW%"=="Y" (
    echo.
    echo   正在推送至 GitHub，線上網站將自動重新部署...
    git push origin main
    echo.
    echo ==============================================================================
    echo   [SUCCESS] 發布成功！GitHub Pages 與 Render 將於 2 分鐘內自動更新生效。
    echo ==============================================================================
) else (
    echo.
    echo   已完成本地 Commit，後續可隨時手動執行 git push origin main。
)

echo.
pause