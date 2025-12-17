# Contributing to AI NPC System

First off, thank you for considering contributing to AI NPC System! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Docker version, etc.)
- **Logs** if applicable

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear title** describing the enhancement
- **Provide detailed description** of the suggested functionality
- **Explain why this enhancement would be useful**
- **List examples** of how it would be used

### 🔧 Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/NPC.git
cd NPC

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

## Code Style Guidelines

### Python
- Follow **PEP 8** style guide
- Use **type hints** for function parameters and returns
- Write **docstrings** for classes and functions
- Keep functions **small and focused**
- Use **meaningful variable names**

Example:
```python
def calculate_reputation_change(
    personality: PersonalityType,
    player_message: str
) -> int:
    """
    Calculate reputation change based on interaction.
    
    Args:
        personality: The NPC's personality type
        player_message: The message from the player
        
    Returns:
        Reputation change value (-10 to +10)
    """
    # Implementation
    pass
```

### API Endpoints
- Use **RESTful conventions**
- Include **proper status codes**
- Add **comprehensive docstrings**
- Handle **errors gracefully**

### Testing
- Write **unit tests** for new features
- Ensure **existing tests pass**
- Test **edge cases**

## Project Structure

```
NPC/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── models.py        # Pydantic models
│   ├── memory.py        # Redis operations
│   ├── personality.py   # Personality system
│   ├── llm_service.py   # LLM integration
│   └── config.py        # Configuration
├── tests/               # Test files (to be added)
├── docs/                # Additional documentation
└── examples/            # Usage examples
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
feat: add voice synthesis support
fix: resolve Redis connection timeout
docs: update API documentation
test: add personality engine tests
refactor: improve memory management
```

**Format:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding/updating tests
- `refactor`: Code refactoring
- `style`: Code style changes
- `chore`: Maintenance tasks

## Areas for Contribution

### High Priority
- [ ] Unit and integration tests
- [ ] WebSocket support for real-time chat
- [ ] Voice synthesis integration
- [ ] Multi-language support
- [ ] Performance optimizations

### Medium Priority
- [ ] NPC-to-NPC conversations
- [ ] Advanced quest chains
- [ ] Emotion detection in messages
- [ ] Custom personality creation UI
- [ ] Analytics dashboard

### Documentation
- [ ] Video tutorials
- [ ] Integration guides (Unity, Unreal)
- [ ] Architecture deep dive
- [ ] Performance tuning guide

## Questions?

Feel free to:
- Open an issue with the `question` label
- Reach out to [@EchoSingh](https://github.com/EchoSingh)

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all.

### Our Standards
- ✅ Be respectful and inclusive
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the community
- ❌ No harassment or trolling
- ❌ No spam or self-promotion
- ❌ No sharing of private information

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🙏
