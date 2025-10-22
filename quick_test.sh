#!/bin/bash

echo "========================================"
echo "  YouTube Downloader - Quick Test"
echo "========================================"
echo

echo "1. Checking Python installation..."
python3 --version || python --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python not found!"
    exit 1
fi

echo
echo "2. Installing dependencies..."
pip3 install -r requirements.txt || pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies!"
    exit 1
fi

echo
echo "3. Testing help command..."
python3 youtube_downloader.py --help || python youtube_downloader.py --help
if [ $? -ne 0 ]; then
    echo "ERROR: Script failed to run!"
    exit 1
fi

echo
echo "4. Testing video info (no download)..."
python3 youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i || python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
if [ $? -ne 0 ]; then
    echo "ERROR: Video info test failed!"
    exit 1
fi

echo
echo "========================================"
echo "  ✅ ALL TESTS PASSED!"
echo "  Project is working correctly!"
echo "========================================"
echo
echo "Try these commands:"
echo "  python3 youtube_downloader.py \"VIDEO_URL\" -i"
echo "  python3 youtube_downloader.py \"VIDEO_URL\" -f audio -o mp3"
echo