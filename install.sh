#!/bin/bash

echo "Installing YouTube Downloader..."
echo

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo
echo "Installation complete!"
echo
echo "Usage examples:"
echo "  python3 youtube_downloader.py \"VIDEO_URL\""
echo "  python3 youtube_downloader.py \"PLAYLIST_URL\" -p"
echo "  python3 youtube_downloader.py -b urls.txt"
echo

# Make the script executable
chmod +x youtube_downloader.py