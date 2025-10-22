@echo off
echo ========================================
echo   YouTube Downloader - Quick Test
echo ========================================
echo.

echo 1. Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo.
echo 2. Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo 3. Testing help command...
python youtube_downloader.py --help
if %errorlevel% neq 0 (
    echo ERROR: Script failed to run!
    pause
    exit /b 1
)

echo.
echo 4. Testing video info (no download)...
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
if %errorlevel% neq 0 (
    echo ERROR: Video info test failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   ✅ ALL TESTS PASSED!
echo   Project is working correctly!
echo ========================================
echo.
echo Try these commands:
echo   python youtube_downloader.py "VIDEO_URL" -i
echo   python youtube_downloader.py "VIDEO_URL" -f audio -o mp3
echo.
pause