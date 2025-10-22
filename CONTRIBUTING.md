# Contributing to YouTube Downloader

Thank you for your interest in contributing to YouTube Downloader! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](../../issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages or logs

### Suggesting Features

1. Check existing [Issues](../../issues) for similar suggestions
2. Create a new issue with:
   - Clear description of the feature
   - Use case and benefits
   - Possible implementation approach

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python youtube_downloader.py --help
   python youtube_downloader.py "https://youtube.com/watch?v=test" -i
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Include testing information

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dusmamud/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

## Code Style Guidelines

- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small
- Use type hints where appropriate

## Testing

- Test your changes with various YouTube URLs
- Test different formats and qualities
- Test error handling scenarios
- Ensure cross-platform compatibility

## Documentation

- Update README.md if adding new features
- Add docstrings to new functions
- Update help text for new CLI options
- Include usage examples

## Pull Request Guidelines

- Keep PRs focused on a single feature/fix
- Write clear commit messages
- Update documentation as needed
- Ensure code passes all tests
- Be responsive to feedback

## Questions?

Feel free to open an issue for any questions about contributing!

Thank you for helping make YouTube Downloader better! 🎉