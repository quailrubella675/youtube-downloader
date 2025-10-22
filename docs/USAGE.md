# Usage Guide

## Quick Start

```bash
# Download a video
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Download audio as MP3
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3

# Download playlist
python youtube_downloader.py "PLAYLIST_URL" -p
```

## Command Line Interface

### Basic Syntax
```bash
python youtube_downloader.py [URL] [OPTIONS]
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-f, --format` | Download format: `video` or `audio` | `video` |
| `-q, --quality` | Quality setting (see quality options below) | `best` |
| `-o, --output` | Output format: `mp4`, `mp3`, `m4a` | `mp4` |
| `-d, --dir` | Output directory | `downloads` |
| `-p, --playlist` | Download entire playlist | False |
| `-b, --bulk` | Bulk download from file | None |
| `-i, --info` | Show video info without downloading | False |
| `--version` | Show version information | - |

## Quality Options

### Video Quality
- `144p` - 144p resolution (lowest)
- `240p` - 240p resolution
- `360p` - 360p resolution (SD)
- `480p` - 480p resolution
- `720p` - 720p resolution (HD)
- `1080p` - 1080p resolution (Full HD)
- `1440p` - 1440p resolution (2K)
- `2160p` - 2160p resolution (4K)
- `best` - Best available quality (default)
- `worst` - Worst available quality

### Audio Quality
- `128k` - 128 kbps
- `192k` - 192 kbps (good quality)
- `256k` - 256 kbps (high quality)
- `320k` - 320 kbps (highest quality)
- `best` - Best available quality (default)
- `worst` - Worst available quality

## Usage Examples

### Single Video Downloads

```bash
# Download video in best quality (MP4)
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download video in 720p
python youtube_downloader.py "VIDEO_URL" -q 720p

# Download to specific directory
python youtube_downloader.py "VIDEO_URL" -d "my_videos"

# Get video information only
python youtube_downloader.py "VIDEO_URL" -i
```

### Audio Downloads

```bash
# Download as MP3 (best quality)
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3

# Download as MP3 with specific bitrate
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3 -q 320k

# Download as M4A
python youtube_downloader.py "VIDEO_URL" -f audio -o m4a -q 256k
```

### Playlist Downloads

```bash
# Download entire playlist as videos
python youtube_downloader.py "PLAYLIST_URL" -p

# Download playlist as MP3 files
python youtube_downloader.py "PLAYLIST_URL" -p -f audio -o mp3

# Download playlist in specific quality
python youtube_downloader.py "PLAYLIST_URL" -p -q 720p
```

### Bulk Downloads

Create a text file with URLs (one per line):

**urls.txt:**
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/playlist?list=PLAYLIST_ID
# This is a comment - ignored
https://www.youtube.com/watch?v=VIDEO_ID_3
```

```bash
# Bulk download from file
python youtube_downloader.py -b urls.txt

# Bulk download as MP3
python youtube_downloader.py -b urls.txt -f audio -o mp3

# Bulk download with specific quality
python youtube_downloader.py -b urls.txt -q 1080p
```

## Interactive Mode

Run without arguments for interactive mode:

```bash
python youtube_downloader.py
```

This will prompt you to:
1. Enter a YouTube URL
2. Choose download type (single, playlist, or info)
3. Process the download

## Output Structure

```
downloads/
├── Single Video.mp4
├── Audio File.mp3
├── playlist_downloads/
│   ├── 01 - First Video.mp4
│   ├── 02 - Second Video.mp4
│   └── 03 - Third Video.mp4
└── Another Video.mp4
```

## Advanced Usage

### Custom Output Directory
```bash
python youtube_downloader.py "VIDEO_URL" -d "/path/to/custom/directory"
```

### Multiple Format Downloads
```bash
# Download video first
python youtube_downloader.py "VIDEO_URL" -f video -q 1080p

# Then download audio
python youtube_downloader.py "VIDEO_URL" -f audio -o mp3 -q 320k
```

### Batch Processing with Different Settings
```bash
# Create separate URL files for different qualities
python youtube_downloader.py -b hd_videos.txt -q 1080p
python youtube_downloader.py -b music.txt -f audio -o mp3 -q 320k
```

## Tips and Best Practices

### 1. Quality Selection
- Use `best` for highest available quality
- Use specific resolutions (720p, 1080p) for consistent quality
- For audio, 192k or 256k provides good quality/size balance

### 2. Storage Management
- Higher quality = larger file sizes
- 4K videos can be very large (1GB+ per video)
- Consider available disk space before bulk downloads

### 3. Network Considerations
- Higher quality downloads take longer
- Use lower quality on slow connections
- Bulk downloads may take significant time

### 4. File Organization
- Use custom directories for different projects
- Playlist downloads are automatically organized
- Consider date-based folder structures for regular downloads

### 5. Error Handling
- The tool continues with other downloads if one fails
- Check console output for error messages
- Retry failed downloads individually

## Troubleshooting Common Issues

### Video Unavailable
```bash
# Check if video exists and is public
python youtube_downloader.py "VIDEO_URL" -i
```

### Quality Not Available
```bash
# Check available qualities first
python youtube_downloader.py "VIDEO_URL" -i

# Use 'best' or 'worst' as fallback
python youtube_downloader.py "VIDEO_URL" -q best
```

### Permission Errors
```bash
# Use different output directory
python youtube_downloader.py "VIDEO_URL" -d "~/Downloads/youtube"
```

### Network Errors
- Check internet connection
- Try again later (temporary YouTube issues)
- Use VPN if region-blocked

## Integration Examples

### Shell Scripts

**download_music.sh:**
```bash
#!/bin/bash
python youtube_downloader.py -b music_urls.txt -f audio -o mp3 -q 320k -d "~/Music/YouTube"
```

**download_tutorials.bat:**
```batch
@echo off
python youtube_downloader.py -b tutorial_urls.txt -q 720p -d "C:\Tutorials"
pause
```

### Automation
```bash
# Cron job for regular downloads (Linux/macOS)
# Add to crontab: crontab -e
0 2 * * * /usr/bin/python3 /path/to/youtube_downloader.py -b /path/to/daily_urls.txt
```

For more advanced usage and troubleshooting, see [Troubleshooting Guide](TROUBLESHOOTING.md).