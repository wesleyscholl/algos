#!/bin/bash

# Quick Start Script for Algos Repository

echo "🚀 Setting up Algos Repository..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run tests
echo "🧪 Running tests..."
pytest tests/ -v

echo ""
echo "✅ Setup complete!"
echo ""
echo "📚 Quick Commands:"
echo "  • Run all tests:        pytest tests/"
echo "  • Run with coverage:    pytest --cov=implementations tests/"
echo "  • Run specific test:    pytest tests/test_hash_map.py"
echo "  • Run doctests:         python -m doctest implementations/*.py"
echo ""
echo "📖 Documentation:"
echo "  • README.md         - Pattern cheat sheet"
echo "  • CONTRIBUTING.md   - How to contribute"
echo "  • STUDY_GUIDE.md    - Study plan & tips"
echo ""
echo "Happy coding! 🎉"
