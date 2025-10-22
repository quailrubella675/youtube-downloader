# 🧪 Testing Guide - YouTube Downloader

Yahan step-by-step guide hai ki project ko kaise test karenge aur verify karenge ki sab kuch sahi se kaam kar raha hai.

## 🚀 Quick Testing (Sabse Pehle Ye Karo)

### Windows Users:
```cmd
# Quick test script run karo
quick_test.bat
```

### Linux/macOS Users:
```bash
# Quick test script run karo
chmod +x quick_test.sh
./quick_test.sh
```

### Manual Quick Test:
```bash
# 1. Dependencies install karo
pip install -r requirements.txt

# 2. Help command test karo
python youtube_downloader.py --help

# 3. Video info test karo (koi download nahi hoga)
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
```

## 🔍 Comprehensive Testing

### Detailed Test Suite:
```bash
# Complete test suite run karo
python test_project.py
```

Ye script check karega:
- ✅ Dependencies installed hai ya nahi
- ✅ File structure correct hai ya nahi  
- ✅ Modules import ho rahe hai ya nahi
- ✅ Basic functionality kaam kar rahi hai ya nahi
- ✅ Unit tests pass ho rahe hai ya nahi

## 📋 Manual Testing Steps

### 1. **Dependencies Check**
```bash
# Python version check
python --version

# Required packages check
python -c "import yt_dlp; print('yt-dlp OK')"
python -c "import colorama; print('colorama OK')"

# FFmpeg check (audio conversion ke liye)
ffmpeg -version
```

### 2. **Basic Functionality Test**
```bash
# Help command
python youtube_downloader.py --help

# Version check
python youtube_downloader.py --version

# Video info (no download)
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
```

### 3. **Download Tests (Actual Downloads)**

#### Single Video Test:
```bash
# Video download test (small file)
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 144p

# Audio download test
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f audio -o mp3 -q 128k
```

#### Interactive Mode Test:
```bash
# Interactive mode
python youtube_downloader.py
# Phir URL enter karo aur options select karo
```

#### Bulk Download Test:
```bash
# Test URLs file banao
echo "https://www.youtube.com/watch?v=dQw4w9WgXcQ" > test_urls.txt
echo "https://www.youtube.com/watch?v=L_jWHffIx5E" >> test_urls.txt

# Bulk download test
python youtube_downloader.py -b test_urls.txt -i
```

### 4. **Error Handling Test**
```bash
# Invalid URL test
python youtube_downloader.py "https://invalid-url.com" -i

# Private video test (should handle gracefully)
python youtube_downloader.py "https://www.youtube.com/watch?v=invalid123" -i
```

## 🎯 Test Cases Checklist

### ✅ **Basic Functionality**
- [ ] Help command works (`--help`)
- [ ] Version command works (`--version`)
- [ ] Video info retrieval works (`-i`)
- [ ] Interactive mode works (no arguments)

### ✅ **Download Features**
- [ ] Single video download (MP4)
- [ ] Audio download (MP3)
- [ ] Audio download (M4A)
- [ ] Quality selection works
- [ ] Custom output directory works

### ✅ **Advanced Features**
- [ ] Playlist download works (`-p`)
- [ ] Bulk download works (`-b`)
- [ ] Different quality options work
- [ ] Error handling works properly

### ✅ **Cross-Platform**
- [ ] Works on Windows
- [ ] Works on Linux
- [ ] Works on macOS
- [ ] Dependencies install correctly

## 🐛 Common Issues & Solutions

### Issue 1: "yt-dlp not found"
```bash
# Solution:
pip install --upgrade yt-dlp
```

### Issue 2: "FFmpeg not found"
```bash
# Windows: Download from https://ffmpeg.org/
# macOS: brew install ffmpeg
# Linux: sudo apt install ffmpeg
```

### Issue 3: "Permission denied"
```bash
# Solution: Change output directory
python youtube_downloader.py "VIDEO_URL" -d "C:\Users\%USERNAME%\Downloads"
```

### Issue 4: "Module not found"
```bash
# Solution: Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## 📊 Expected Test Results

### ✅ **Success Indicators:**
- Help command shows all options
- Video info shows title, duration, uploader
- Downloads create files in `downloads/` folder
- No Python errors or crashes
- Colored output appears correctly

### ❌ **Failure Indicators:**
- Python import errors
- "Command not found" errors
- Network timeout errors (check internet)
- FFmpeg errors (install FFmpeg)

## 🚀 Performance Testing

### Speed Test:
```bash
# Test download speed with different qualities
time python youtube_downloader.py "VIDEO_URL" -q 144p
time python youtube_downloader.py "VIDEO_URL" -q 720p
```

### Memory Test:
```bash
# Monitor memory usage during large downloads
# Use Task Manager (Windows) or htop (Linux)
```

## 📝 Test Report Template

```
YouTube Downloader Test Report
=============================

Date: ___________
OS: _____________
Python Version: _________

✅ Dependencies: PASS/FAIL
✅ Basic Commands: PASS/FAIL  
✅ Video Download: PASS/FAIL
✅ Audio Download: PASS/FAIL
✅ Playlist Download: PASS/FAIL
✅ Bulk Download: PASS/FAIL
✅ Error Handling: PASS/FAIL

Issues Found:
- 
- 

Overall Status: READY/NEEDS_FIXES
```

## 🎉 Success Criteria

Project ready hai agar:
- ✅ All basic commands work
- ✅ Video info retrieval works
- ✅ At least one download format works
- ✅ No critical errors
- ✅ Dependencies install successfully

## 💡 Next Steps After Testing

1. **If tests pass:** Project ready for use!
2. **If tests fail:** Check error messages and fix issues
3. **For contributors:** Run `python -m pytest tests/` for unit tests
4. **For deployment:** All tests should pass before sharing

---

**Happy Testing! 🎉**

Agar koi problem aaye to error message carefully padho aur [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) check karo.