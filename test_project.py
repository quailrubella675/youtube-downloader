#!/usr/bin/env python3
"""
Project Testing Script
Quick tests to verify the YouTube Downloader is working correctly
"""

import sys
import subprocess
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"\n{Fore.CYAN}🧪 Testing: {description}")
    print(f"{Fore.YELLOW}Command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"{Fore.GREEN}✅ SUCCESS")
            if result.stdout.strip():
                print(f"{Fore.WHITE}Output: {result.stdout.strip()}")
            return True
        else:
            print(f"{Fore.RED}❌ FAILED")
            if result.stderr.strip():
                print(f"{Fore.RED}Error: {result.stderr.strip()}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}❌ TIMEOUT (30s)")
        return False
    except Exception as e:
        print(f"{Fore.RED}❌ ERROR: {str(e)}")
        return False

def check_dependencies():
    """Check if all required dependencies are installed"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}🔍 CHECKING DEPENDENCIES")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    dependencies = [
        ("python --version", "Python installation"),
        ("pip --version", "Pip package manager"),
        ("python -c \"import yt_dlp; print('yt-dlp version:', yt_dlp.version.__version__)\"", "yt-dlp library"),
        ("python -c \"import colorama; print('colorama installed')\"", "colorama library"),
        ("ffmpeg -version", "FFmpeg (for audio conversion)")
    ]
    
    results = []
    for cmd, desc in dependencies:
        success = run_command(cmd, desc)
        results.append((desc, success))
    
    return results

def test_basic_functionality():
    """Test basic functionality of the downloader"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}🚀 TESTING BASIC FUNCTIONALITY")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    # Test video URL for Rick Roll (safe, always available)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    tests = [
        ("python youtube_downloader.py --help", "Help command"),
        ("python youtube_downloader.py --version", "Version command"),
        (f"python youtube_downloader.py \"{test_url}\" -i", "Video info retrieval (no download)"),
    ]
    
    results = []
    for cmd, desc in tests:
        success = run_command(cmd, desc)
        results.append((desc, success))
    
    return results

def test_module_imports():
    """Test if all modules can be imported correctly"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}📦 TESTING MODULE IMPORTS")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    import_tests = [
        ("python -c \"import sys; sys.path.insert(0, 'src'); from downloader import YouTubeDownloader; print('✅ downloader module OK')\"", "Downloader module"),
        ("python -c \"import sys; sys.path.insert(0, 'src'); from utils import validate_url, format_duration; print('✅ utils module OK')\"", "Utils module"),
        ("python -c \"import sys; sys.path.insert(0, 'src'); import downloader, utils; print('✅ All modules OK')\"", "All custom modules")
    ]
    
    results = []
    for cmd, desc in import_tests:
        success = run_command(cmd, desc)
        results.append((desc, success))
    
    return results

def test_file_structure():
    """Check if all required files exist"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}📁 CHECKING FILE STRUCTURE")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    required_files = [
        "youtube_downloader.py",
        "requirements.txt",
        "README.md",
        "src/__init__.py",
        "src/downloader.py",
        "src/utils.py",
        "tests/test_downloader.py",
        "docs/INSTALLATION.md",
        "docs/USAGE.md",
        "LICENSE"
    ]
    
    results = []
    for file_path in required_files:
        exists = Path(file_path).exists()
        status = "✅ EXISTS" if exists else "❌ MISSING"
        color = Fore.GREEN if exists else Fore.RED
        print(f"{color}{status}: {file_path}")
        results.append((file_path, exists))
    
    return results

def run_unit_tests():
    """Run the unit tests"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}🧪 RUNNING UNIT TESTS")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    test_commands = [
        ("python -m pytest tests/ -v", "Unit tests with pytest"),
        ("python tests/test_downloader.py", "Direct test execution")
    ]
    
    results = []
    for cmd, desc in test_commands:
        success = run_command(cmd, desc)
        results.append((desc, success))
    
    return results

def print_summary(all_results):
    """Print test summary"""
    print(f"\n{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.MAGENTA}📊 TEST SUMMARY")
    print(f"{Fore.MAGENTA}{'='*60}")
    
    total_tests = 0
    passed_tests = 0
    
    for category, results in all_results.items():
        print(f"\n{Fore.CYAN}📋 {category}:")
        for test_name, success in results:
            status = "✅ PASS" if success else "❌ FAIL"
            color = Fore.GREEN if success else Fore.RED
            print(f"  {color}{status}: {test_name}")
            total_tests += 1
            if success:
                passed_tests += 1
    
    print(f"\n{Fore.MAGENTA}{'='*60}")
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    
    if success_rate >= 80:
        color = Fore.GREEN
        status = "🎉 EXCELLENT"
    elif success_rate >= 60:
        color = Fore.YELLOW
        status = "⚠️  GOOD"
    else:
        color = Fore.RED
        status = "❌ NEEDS WORK"
    
    print(f"{color}{status}: {passed_tests}/{total_tests} tests passed ({success_rate:.1f}%)")
    
    if success_rate >= 80:
        print(f"{Fore.GREEN}🚀 Project is ready to use!")
    elif success_rate >= 60:
        print(f"{Fore.YELLOW}⚠️  Project mostly works, check failed tests")
    else:
        print(f"{Fore.RED}❌ Project needs fixes before use")

def main():
    """Main testing function"""
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("=" * 60)
    print("    🎥 YouTube Downloader - Project Test Suite")
    print("=" * 60)
    print(f"{Style.RESET_ALL}")
    
    all_results = {}
    
    # Run all test categories
    all_results["Dependencies"] = check_dependencies()
    all_results["File Structure"] = test_file_structure()
    all_results["Module Imports"] = test_module_imports()
    all_results["Basic Functionality"] = test_basic_functionality()
    all_results["Unit Tests"] = run_unit_tests()
    
    # Print summary
    print_summary(all_results)
    
    print(f"\n{Fore.CYAN}💡 Next Steps:")
    print(f"{Fore.WHITE}1. Fix any failed tests above")
    print(f"{Fore.WHITE}2. Try downloading a test video:")
    print(f"{Fore.YELLOW}   python youtube_downloader.py \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\" -i")
    print(f"{Fore.WHITE}3. Test actual download:")
    print(f"{Fore.YELLOW}   python youtube_downloader.py \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\" -f audio -o mp3")

if __name__ == "__main__":
    main()