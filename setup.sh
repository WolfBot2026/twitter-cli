#!/bin/bash
# Quick setup script for Twitter CLI tool

echo "🐦 Twitter CLI Tool Setup"
echo "=========================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install requests requests-oauthlib --quiet
echo "✅ Dependencies installed"
echo ""

# Make script executable
chmod +x ~/clawd/nightly-builds/2026-01-29/tweet.py
echo "✅ Script made executable"
echo ""

# Check if credentials exist
CRED_FILE="$HOME/.twitter_credentials.json"
if [ -f "$CRED_FILE" ]; then
    echo "✅ Credentials file found at $CRED_FILE"
else
    echo "⚠️  Credentials file not found"
    echo ""
    echo "Create $CRED_FILE with this structure:"
    echo ""
    cat << 'EOF'
{
  "api_key": "your_api_key_here",
  "api_secret": "your_api_secret_here",
  "access_token": "your_access_token_here",
  "access_token_secret": "your_access_token_secret_here",
  "bearer_token": "your_bearer_token_here"
}
EOF
    echo ""
    echo "Get credentials from: https://developer.twitter.com/en/portal/dashboard"
    echo ""
fi

# Offer to add alias
echo ""
echo "📝 Add this alias to your ~/.bashrc or ~/.zshrc:"
echo ""
echo "alias tweet='python3 ~/clawd/nightly-builds/2026-01-29/tweet.py'"
echo ""
echo "Then run: source ~/.bashrc"
echo ""

echo "✅ Setup complete!"
echo ""
echo "Test with: python3 ~/clawd/nightly-builds/2026-01-29/tweet.py 'Hello Twitter! 👋'"
