@echo off
echo Installing YouTube Downloader...
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Installation complete!
echo.
echo Usage examples:
echo   python youtube_downloader.py "VIDEO_URL"
echo   python youtube_downloader.py "PLAYLIST_URL" -p
echo   python youtube_downloader.py -b urls.txt
echo.
pause