# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### 1. "yt-dlp not found" or "No module named 'yt_dlp'"

**Solution:**
```bash
# Install or upgrade yt-dlp
pip install --upgrade yt-dlp

# If using virtual environment, ensure it's activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

#### 2. "FFmpeg not found" (for audio conversion)

**Symptoms:** Audio downloads fail or no MP3/M4A files created

**Solutions:**

**Windows:**
```bash
# Download FFmpeg from https://ffmpeg.org/download.html
# Extract to C:\ffmpeg
# Add C:\ffmpeg\bin to PATH environment variable
# Test: ffmpeg -version
```

**macOS:**
```bash
# Install using Homebrew
brew install ffmpeg

# Or using MacPorts
sudo port install ffmpeg
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

#### 3. Permission Denied Errors

**Linux/macOS:**
```bash
# Make script executable
chmod +x youtube_downloader.py

# Or run with python explicitly
python3 youtube_downloader.py "VIDEO_URL"
```

**Windows:**
```bash
# Run Command Prompt as Administrator
# Or change output directory
python youtube_downloader.py "VIDEO_URL" -d "C:\Users\%USERNAME%\Downloads"
```

### Download Issues

#### 1. "Video unavailable" or "Private video"

**Causes:**
- Video is private, deleted, or region-blocked
- Age-restricted content
- Live streams that have ended

**Solutions:**
```bash
# Check video info first
python youtube_downloader.py "VIDEO_URL" -i

# Try different URL format
# Instead of: https://www.youtube.com/watch?v=VIDEO_ID
# Try: https://youtu.be/VIDEO_ID
```

#### 2. "Requested format not available"

**Symptoms:** Specific quality not found

**Solutions:**
```bash
# Check available formats
python youtube_downloader.py "VIDEO_URL" -i

# Use 'best' or 'worst' as fallback
python youtube_downloader.py "VIDEO_URL" -q best

# Try different quality
python youtube_downloader.py "VIDEO_URL" -q 720p
```

#### 3. Slow Download Speeds

**Solutions:**
```bash
# Use lower quality for faster downloads
python youtube_downloader.py "VIDEO_URL" -q 480p

# Download audio only (smaller files)
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3
```

#### 4. Downloads Keep Failing

**Solutions:**
```bash
# Update yt-dlp (YouTube changes frequently)
pip install --upgrade yt-dlp

# Try again later (temporary YouTube issues)

# Check internet connection
ping google.com

# Use VPN if region-blocked
```

### Playlist Issues

#### 1. "Playlist not found" or Empty Playlist

**Solutions:**
```bash
# Ensure playlist is public
# Check playlist URL format:
# Correct: https://www.youtube.com/playlist?list=PLAYLIST_ID
# Incorrect: https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID

# Try extracting playlist ID manually
```

#### 2. Partial Playlist Downloads

**Symptoms:** Only some videos download from playlist

**Solutions:**
- Some videos in playlist may be private/unavailable
- Check console output for specific errors
- Tool continues with available videos

### File and Directory Issues

#### 1. "No space left on device"

**Solutions:**
```bash
# Check disk space
df -h  # Linux/macOS
dir    # Windows

# Use different output directory
python youtube_downloader.py "VIDEO_URL" -d "/path/with/more/space"

# Download lower quality
python youtube_downloader.py "VIDEO_URL" -q 480p
```

#### 2. "Filename too long" Errors

**Solutions:**
- YouTube video titles can be very long
- Tool automatically truncates filenames
- If issues persist, use shorter output directory path

#### 3. Special Characters in Filenames

**Symptoms:** Files not created or weird filenames

**Solutions:**
- Tool automatically handles most special characters
- Files saved with sanitized names
- Original title preserved in metadata

### Network Issues

#### 1. SSL Certificate Errors

**Solutions:**
```bash
# Update certificates
pip install --upgrade certifi

# Update yt-dlp
pip install --upgrade yt-dlp
```

#### 2. Connection Timeouts

**Solutions:**
```bash
# Check internet connection
ping youtube.com

# Try again later
# Use VPN if needed
```

#### 3. Rate Limiting

**Symptoms:** "Too many requests" errors

**Solutions:**
- Wait before retrying
- YouTube may temporarily block rapid requests
- Spread out bulk downloads over time

### Audio Conversion Issues

#### 1. MP3 Files Not Created

**Check:**
1. FFmpeg installed and in PATH
2. Sufficient disk space
3. Write permissions in output directory

**Solutions:**
```bash
# Test FFmpeg
ffmpeg -version

# Try M4A instead (doesn't require conversion)
python youtube_downloader.py "VIDEO_URL" -f audio -o m4a

# Reinstall FFmpeg
```

#### 2. Poor Audio Quality

**Solutions:**
```bash
# Use higher bitrate
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3 -q 320k

# Try M4A format (often better quality)
python youtube_downloader.py "VIDEO_URL" -f audio -o m4a -q best
```

### Bulk Download Issues

#### 1. "No valid URLs found in file"

**Check:**
- File exists and readable
- URLs are one per line
- No extra spaces or characters
- Lines starting with # are comments (ignored)

**Example valid file:**
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
# This is a comment
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

#### 2. Some URLs Fail in Bulk Download

**Normal behavior:**
- Tool continues with other URLs
- Failed URLs listed at end
- Check individual URLs manually

### Performance Issues

#### 1. High Memory Usage

**Solutions:**
- Download one video at a time instead of bulk
- Use lower quality settings
- Close other applications

#### 2. CPU Usage

**Solutions:**
- Audio conversion (MP3) is CPU-intensive
- Use M4A format to avoid conversion
- Download during off-peak hours

## Advanced Troubleshooting

### Debug Mode

Add verbose output for debugging:

```bash
# Enable verbose output (modify script if needed)
# Or check yt-dlp directly:
yt-dlp --verbose "VIDEO_URL"
```

### Manual yt-dlp Testing

```bash
# Test yt-dlp directly
yt-dlp "VIDEO_URL"

# List available formats
yt-dlp -F "VIDEO_URL"

# Download specific format
yt-dlp -f "best[height<=720]" "VIDEO_URL"
```

### Environment Issues

#### Python Version Conflicts

```bash
# Check Python version
python --version

# Use specific Python version
python3.9 youtube_downloader.py "VIDEO_URL"

# Check installed packages
pip list | grep yt-dlp
```

#### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### System-Specific Issues

#### Windows

```bash
# Use PowerShell instead of Command Prompt
# Ensure Python in PATH
# May need to use 'py' instead of 'python'
py youtube_downloader.py "VIDEO_URL"
```

#### macOS

```bash
# Use python3 explicitly
python3 youtube_downloader.py "VIDEO_URL"

# Install Xcode Command Line Tools if needed
xcode-select --install
```

#### Linux

```bash
# Install python3-venv if needed
sudo apt install python3-venv

# Use python3 and pip3
python3 -m pip install -r requirements.txt
```

## Getting Help

### Before Reporting Issues

1. **Update everything:**
   ```bash
   pip install --upgrade yt-dlp colorama
   ```

2. **Test with simple video:**
   ```bash
   python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
   ```

3. **Check system requirements:**
   - Python 3.7+
   - FFmpeg (for audio conversion)
   - Internet connection

### Reporting Bugs

Include in your bug report:
- Operating system and version
- Python version (`python --version`)
- Error message (full text)
- Command used
- Video URL (if not private)
- Steps to reproduce

### Community Support

- Check existing [GitHub Issues](../../issues)
- Search for similar problems
- Provide detailed information when asking for help

## Quick Fixes Summary

| Problem | Quick Fix |
|---------|-----------|
| yt-dlp not found | `pip install --upgrade yt-dlp` |
| FFmpeg not found | Install FFmpeg, add to PATH |
| Permission denied | Change output directory or run as admin |
| Video unavailable | Check if video is public, try different URL |
| Format not available | Use `-q best` or `-q worst` |
| Slow downloads | Use lower quality `-q 480p` |
| SSL errors | `pip install --upgrade certifi` |
| Playlist issues | Check playlist is public and URL format |
| Audio conversion fails | Check FFmpeg installation |
| Bulk download fails | Check file format and URL validity |

Most issues are resolved by updating yt-dlp and ensuring FFmpeg is properly installed.