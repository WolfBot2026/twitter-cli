# 🐦 Twitter CLI Tool

A simple command-line tool for posting tweets from the terminal or scripts.

## 🎯 What Problem Does This Solve?

**Yesterday you asked:** "How can I set you up to post to my Twitter?"

**The friction:** No easy way to programmatically post tweets without building a full integration.

**The solution:** A simple Python CLI tool that:
- Posts tweets with one command
- Handles Twitter API authentication
- Works from terminal, scripts, or can be called by me (WolfBot)
- Checks character limits
- Provides clear error messages
- Falls back to v1.1 API if v2 fails

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install requests requests-oauthlib
```

### 2. Get Twitter API Credentials

Visit: https://developer.twitter.com/en/portal/dashboard

1. Create a Developer Account (if you don't have one)
2. Create a new Project & App
3. Generate these credentials:
   - API Key
   - API Secret Key  
   - Access Token
   - Access Token Secret
   - Bearer Token

### 3. Save Credentials

Create `~/.twitter_credentials.json`:

```json
{
  "api_key": "your_api_key_here",
  "api_secret": "your_api_secret_here",
  "access_token": "your_access_token_here",
  "access_token_secret": "your_access_token_secret_here",
  "bearer_token": "your_bearer_token_here"
}
```

**Security:** This file will only be readable by you. Never commit it to git!

```bash
chmod 600 ~/.twitter_credentials.json
```

### 4. Make Script Executable

```bash
chmod +x ~/clawd/nightly-builds/2026-01-29/tweet.py
```

### 5. Optional: Add to PATH

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
alias tweet='python3 ~/clawd/nightly-builds/2026-01-29/tweet.py'
```

Then reload:
```bash
source ~/.bashrc
```

## 📖 Usage

### Basic Tweet

```bash
./tweet.py "Hello Twitter! 👋"
```

Or with alias:
```bash
tweet "Just deployed my new React app! 🚀"
```

### Examples

```bash
# Share a project
tweet "🐺 Built a fitness tracker app today! Check it out: https://wolfbot2026.github.io/fitness-tracker/"

# Quick update
tweet "Coffee and code ☕💻"

# With emoji
tweet "💪 Finished my workout! Core day complete 🔥"
```

### Character Limit Check

The tool automatically checks the 280-character limit:

```bash
tweet "This is a really long tweet that might exceed the 280 character limit..."
# Output: ❌ Tweet too long! 287/280 characters
```

## 🔧 How It Works

1. **Loads credentials** from `~/.twitter_credentials.json`
2. **Validates tweet length** (280 chars max)
3. **Tries Twitter API v2** first (newer, cleaner)
4. **Falls back to v1.1** if v2 fails
5. **Returns tweet URL** on success

## 🤖 WolfBot Integration

Once you have credentials set up, I (WolfBot) can use this to post tweets for you!

Example commands you could give me:
- "Tweet about my new fitness tracker app"
- "Post a thread about the projects I built today"
- "Share my GitHub portfolio on Twitter"

I'll use this tool to post on your behalf (with your approval, of course).

## 🛡️ Security Notes

- **Credentials are stored locally** in your home directory
- **Never commit** `.twitter_credentials.json` to git
- **Set proper permissions:** `chmod 600 ~/.twitter_credentials.json`
- **OAuth tokens** can be revoked anytime from Twitter Developer Portal
- **Read/Write access** required - make sure your app has posting permissions

## 📊 API Endpoints Used

- **v2:** `POST https://api.twitter.com/2/tweets` (Bearer token)
- **v1.1:** `POST https://api.twitter.com/1.1/statuses/update.json` (OAuth 1.0a)

## 🔮 Future Enhancements

Ideas for v2 (let me know if you want these):

- [ ] **Thread support** - Post multiple tweets as a thread
- [ ] **Media upload** - Attach images/videos
- [ ] **Reply to tweets** - Respond to specific tweet IDs
- [ ] **Schedule tweets** - Queue tweets for later
- [ ] **Draft management** - Save and edit drafts
- [ ] **Analytics** - Track tweet performance
- [ ] **Hashtag suggestions** - Auto-suggest relevant hashtags

## 🐛 Troubleshooting

### "Twitter credentials not found"
Create `~/.twitter_credentials.json` with your API keys.

### "Error 401: Unauthorized"
Check your credentials are correct and have read/write permissions.

### "Error 403: Forbidden"
Your app may not have "Read and Write" permissions. Check Twitter Developer Portal.

### "Error 429: Too Many Requests"
You've hit rate limits. Twitter limits tweets per 15-minute window.

## 📚 Resources

- [Twitter API Documentation](https://developer.twitter.com/en/docs)
- [Get API Keys](https://developer.twitter.com/en/portal/dashboard)
- [Rate Limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)

## 📝 Notes

- Built on: 2026-01-29 (Nightly Builder Task)
- Purpose: Quick CLI tool for posting tweets
- Tested: No (needs credentials to test)
- Python: 3.7+
- Dependencies: `requests`, `requests-oauthlib`

---

**Built by WolfBot 🐺** • Making it easier to share your wins on Twitter!
