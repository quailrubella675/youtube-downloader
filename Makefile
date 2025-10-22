# YouTube Downloader Makefile

.PHONY: help install install-dev test lint format clean build upload

# Default target
help:
	@echo "YouTube Downloader - Available commands:"
	@echo ""
	@echo "  install      Install dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting (flake8)"
	@echo "  format       Format code (black)"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build package"
	@echo "  upload       Upload to PyPI (requires credentials)"
	@echo "  run          Run the downloader interactively"
	@echo ""

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

# Testing
test:
	python -m pytest tests/ -v

test-cov:
	python -m pytest tests/ --cov=src --cov-report=html --cov-report=term

# Code quality
lint:
	flake8 src/ youtube_downloader.py tests/
	mypy src/ youtube_downloader.py

format:
	black src/ youtube_downloader.py tests/

format-check:
	black --check src/ youtube_downloader.py tests/

# Cleaning
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Building
build: clean
	python setup.py sdist bdist_wheel

# Upload (requires twine and credentials)
upload: build
	twine upload dist/*

# Development
run:
	python youtube_downloader.py

# Example downloads for testing
test-download:
	python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -i

# Setup development environment
setup-dev: install-dev
	@echo "Development environment setup complete!"
	@echo "Run 'make test' to verify installation"