#!/usr/bin/env python3
"""
YouTube Video Downloader - Main CLI Interface
Supports single videos, playlists, bulk downloads with various formats and resolutions
"""

import sys
import argparse
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from downloader import YouTubeDownloader
from utils import load_urls_from_file, print_banner, validate_url, format_duration, format_views
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)


def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description='YouTube Video/Audio Downloader',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://youtube.com/watch?v=VIDEO_ID"
  %(prog)s "PLAYLIST_URL" -p -f audio -o mp3
  %(prog)s -b urls.txt -q 720p
  %(prog)s "VIDEO_URL" -i
        """
    )
    
    parser.add_argument('url', nargs='?', help='YouTube URL to download')
    parser.add_argument('-f', '--format', choices=['video', 'audio'], default='video',
                       help='Download format (default: video)')
    parser.add_argument('-q', '--quality', default='best',
                       help='Quality (video: 144p,240p,360p,480p,720p,1080p,1440p,2160p,best,worst | audio: best,worst,128k,192k,256k,320k)')
    parser.add_argument('-o', '--output', choices=['mp4', 'mp3', 'm4a'], default='mp4',
                       help='Output format (default: mp4)')
    parser.add_argument('-d', '--dir', default='downloads',
                       help='Output directory (default: downloads)')
    parser.add_argument('-p', '--playlist', action='store_true',
                       help='Download entire playlist')
    parser.add_argument('-b', '--bulk', help='Bulk download from file (one URL per line)')
    parser.add_argument('-i', '--info', action='store_true',
                       help='Show video info without downloading')
    parser.add_argument('--version', action='version', version='YouTube Downloader v1.0.0')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    downloader = YouTubeDownloader(args.dir)
    
    # Handle different modes
    if args.bulk:
        urls = load_urls_from_file(args.bulk)
        if urls:
            print(f"{Fore.CYAN}Loaded {len(urls)} URLs from file")
            downloader.bulk_download(urls, args.format, args.quality, args.output)
        else:
            print(f"{Fore.RED}No valid URLs found in file: {args.bulk}")
            return 1
    
    elif args.url:
        if not validate_url(args.url):
            print(f"{Fore.RED}Invalid YouTube URL: {args.url}")
            return 1
            
        if args.info:
            info = downloader.get_video_info(args.url)
            if info:
                print(f"{Fore.GREEN}📹 Video Information:")
                print(f"  Title: {info['title']}")
                print(f"  Duration: {format_duration(info['duration'])}")
                print(f"  Uploader: {info['uploader']}")
                print(f"  Views: {format_views(info['view_count'])}")
                print(f"  Upload Date: {info['upload_date']}")
            else:
                return 1
        
        elif args.playlist:
            result = downloader.download_playlist(args.url, args.format, args.quality, args.output)
            if not result.get('success', False):
                return 1
        
        else:
            if not downloader.download_single(args.url, args.format, args.quality, args.output):
                return 1
    
    else:
        # Interactive mode
        interactive_mode(downloader, args)
    
    return 0

def interactive_mode(downloader: YouTubeDownloader, args):
    """Interactive CLI mode"""
    print(f"{Fore.YELLOW}🎯 Interactive Mode")
    print("Enter YouTube URL (or 'quit' to exit):")
    
    while True:
        url = input(f"{Fore.CYAN}URL: {Style.RESET_ALL}").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print(f"{Fore.GREEN}Goodbye! 👋")
            break
            
        if not url:
            continue
            
        if not validate_url(url):
            print(f"{Fore.RED}Invalid YouTube URL. Please try again.")
            continue
        
        print(f"\n{Fore.YELLOW}📋 Select download type:")
        print("1. 🎥 Single video/audio")
        print("2. 📁 Entire playlist") 
        print("3. ℹ️  Get video info only")
        print("4. 🔙 Enter new URL")
        
        choice = input(f"{Fore.CYAN}Choice (1-4): {Style.RESET_ALL}").strip()
        
        if choice == '1':
            if not downloader.download_single(url, args.format, args.quality, args.output):
                print(f"{Fore.RED}Download failed. Try again with different settings.")
        elif choice == '2':
            result = downloader.download_playlist(url, args.format, args.quality, args.output)
            if not result.get('success', False):
                print(f"{Fore.RED}Playlist download failed.")
        elif choice == '3':
            info = downloader.get_video_info(url)
            if info:
                print(f"\n{Fore.GREEN}📹 Video Information:")
                print(f"  Title: {info['title']}")
                print(f"  Duration: {format_duration(info['duration'])}")
                print(f"  Uploader: {info['uploader']}")
                print(f"  Views: {format_views(info['view_count'])}")
                print(f"  Upload Date: {info['upload_date']}")
        elif choice == '4':
            continue
        else:
            print(f"{Fore.RED}Invalid choice. Please select 1-4.")
            continue
        
        print(f"\n{Fore.MAGENTA}{'='*50}")

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Download interrupted by user. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {str(e)}")
        sys.exit(1)