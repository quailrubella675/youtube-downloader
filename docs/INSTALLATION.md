# Installation Guide

## Prerequisites

- **Python 3.7+** - Download from [python.org](https://www.python.org/downloads/)
- **FFmpeg** - Required for audio conversion (MP3/M4A)

## FFmpeg Installation

### Windows
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your PATH environment variable
4. Restart command prompt and test: `ffmpeg -version`

### macOS
```bash
# Using Homebrew (recommended)
brew install ffmpeg

# Using MacPorts
sudo port install ffmpeg
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### Linux (CentOS/RHEL/Fedora)
```bash
# CentOS/RHEL
sudo yum install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

## Installation Methods

### Method 1: Clone Repository (Recommended)

```bash
# Clone the repository
git clone https://github.com/dusmamud/youtube-downloader.git
cd youtube-downloader

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Download ZIP

1. Download ZIP from GitHub
2. Extract to desired location
3. Open terminal in extracted folder
4. Run: `pip install -r requirements.txt`

### Method 3: Direct Installation

```bash
# Install dependencies directly
pip install yt-dlp colorama

# Download the main script
curl -O https://raw.githubusercontent.com/dusmamud/youtube-downloader/main/youtube_downloader.py
```

## Verification

Test the installation:

```bash
# Check help
python youtube_downloader.py --help

# Test with video info (no download)
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i
```

## Troubleshooting

### Common Issues

#### 1. "yt-dlp not found"
```bash
pip install --upgrade yt-dlp
```

#### 2. "FFmpeg not found" (for audio conversion)
- Ensure FFmpeg is installed and in PATH
- Test: `ffmpeg -version`

#### 3. "Permission denied" (Linux/macOS)
```bash
chmod +x youtube_downloader.py
```

#### 4. "Module not found" errors
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

#### 5. SSL Certificate errors
```bash
# Update certificates
pip install --upgrade certifi
```

### Python Version Issues

If you have multiple Python versions:

```bash
# Use specific Python version
python3.9 -m pip install -r requirements.txt
python3.9 youtube_downloader.py "VIDEO_URL"
```

### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Development Installation

For contributors:

```bash
# Clone repository
git clone https://github.com/dusmamud/youtube-downloader.git
cd youtube-downloader

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/
```

## System-Specific Notes

### Windows
- Use Command Prompt or PowerShell
- Ensure Python is in PATH
- May need to use `py` instead of `python`

### macOS
- Use Terminal
- May need to use `python3` instead of `python`
- Xcode Command Line Tools may be required

### Linux
- Use terminal
- May need to use `python3` and `pip3`
- Some distributions require `python3-venv` package

## Next Steps

After installation, see:
- [Usage Guide](USAGE.md) - How to use the downloader
- [Examples](../README.md#examples) - Common usage examples
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions