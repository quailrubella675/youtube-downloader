#!/usr/bin/env python3
"""
Unit tests for YouTube Downloader
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from downloader import YouTubeDownloader
from utils import validate_url, format_duration, format_views

class TestYouTubeDownloader(unittest.TestCase):
    """Test cases for YouTubeDownloader class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.downloader = YouTubeDownloader("test_downloads")
    
    def test_init(self):
        """Test downloader initialization"""
        self.assertEqual(str(self.downloader.output_dir), "test_downloads")
        self.assertTrue(self.downloader.output_dir.exists())
    
    def test_video_qualities(self):
        """Test video quality options"""
        self.assertIn('720p', self.downloader.video_qualities)
        self.assertIn('1080p', self.downloader.video_qualities)
        self.assertIn('best', self.downloader.video_qualities)
    
    def test_audio_qualities(self):
        """Test audio quality options"""
        self.assertIn('320k', self.downloader.audio_qualities)
        self.assertIn('best', self.downloader.audio_qualities)
    
    def test_get_ydl_opts_video(self):
        """Test yt-dlp options for video"""
        opts = self.downloader.get_ydl_opts('video', '720p', 'mp4')
        self.assertIn('format', opts)
        self.assertIn('outtmpl', opts)
    
    def test_get_ydl_opts_audio(self):
        """Test yt-dlp options for audio"""
        opts = self.downloader.get_ydl_opts('audio', '320k', 'mp3')
        self.assertIn('format', opts)
        self.assertIn('postprocessors', opts)

class TestUtils(unittest.TestCase):
    """Test cases for utility functions"""
    
    def test_validate_url_valid(self):
        """Test URL validation with valid URLs"""
        valid_urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://youtube.com/watch?v=dQw4w9WgXcQ',
            'https://youtu.be/dQw4w9WgXcQ',
            'https://m.youtube.com/watch?v=dQw4w9WgXcQ'
        ]
        
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(validate_url(url))
    
    def test_validate_url_invalid(self):
        """Test URL validation with invalid URLs"""
        invalid_urls = [
            'https://google.com',
            'https://vimeo.com/123456',
            'not_a_url',
            ''
        ]
        
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(validate_url(url))
    
    def test_format_duration(self):
        """Test duration formatting"""
        test_cases = [
            (0, "Unknown"),
            (30, "00:30"),
            (90, "01:30"),
            (3661, "01:01:01"),
            (7200, "02:00:00")
        ]
        
        for seconds, expected in test_cases:
            with self.subTest(seconds=seconds):
                self.assertEqual(format_duration(seconds), expected)
    
    def test_format_views(self):
        """Test view count formatting"""
        test_cases = [
            (0, "Unknown"),
            (500, "500"),
            (1500, "1.5K"),
            (1500000, "1.5M"),
            (1500000000, "1.5B")
        ]
        
        for views, expected in test_cases:
            with self.subTest(views=views):
                self.assertEqual(format_views(views), expected)

if __name__ == '__main__':
    unittest.main()