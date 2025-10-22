#!/usr/bin/env python3
"""
Setup script for YouTube Downloader
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="youtube-downloader",
    version="1.0.0",
    author="dusmamud",
    author_email="dusmamud@users.noreply.github.com",
    description="A comprehensive YouTube video and audio downloader with playlist and bulk download support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dusmamud/youtube-downloader",
    packages=find_packages(),
    py_modules=["youtube_downloader"],
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=2.20.0",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP",
        "Environment :: Console",
    ],
    keywords="youtube, downloader, video, audio, mp3, mp4, playlist, bulk",
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "youtube-downloader=youtube_downloader:main",
            "ytdl=youtube_downloader:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/dusmamud/youtube-downloader/issues",
        "Source": "https://github.com/dusmamud/youtube-downloader",
        "Documentation": "https://github.com/dusmamud/youtube-downloader/blob/main/docs/",
    },
)