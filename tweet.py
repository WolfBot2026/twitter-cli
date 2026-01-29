#!/usr/bin/env python3
"""
Simple Twitter/X posting CLI tool
Supports posting tweets with optional media
"""

import sys
import json
import os
from pathlib import Path

def load_credentials():
    """Load Twitter API credentials from config file"""
    cred_file = Path.home() / ".twitter_credentials.json"
    
    if not cred_file.exists():
        print("❌ Twitter credentials not found!")
        print(f"\nPlease create: {cred_file}")
        print("\nWith this structure:")
        print(json.dumps({
            "api_key": "your_api_key",
            "api_secret": "your_api_secret",
            "access_token": "your_access_token",
            "access_token_secret": "your_access_token_secret",
            "bearer_token": "your_bearer_token"
        }, indent=2))
        print("\nGet these from: https://developer.twitter.com/en/portal/dashboard")
        return None
    
    with open(cred_file, 'r') as f:
        return json.load(f)

def post_tweet_v2(text, media_ids=None):
    """Post a tweet using Twitter API v2"""
    import requests
    
    creds = load_credentials()
    if not creds:
        return False
    
    # Use v2 endpoint
    url = "https://api.twitter.com/2/tweets"
    
    payload = {"text": text}
    if media_ids:
        payload["media"] = {"media_ids": media_ids}
    
    headers = {
        "Authorization": f"Bearer {creds['bearer_token']}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        data = response.json()
        tweet_id = data['data']['id']
        print(f"✅ Tweet posted successfully!")
        print(f"🔗 https://twitter.com/i/web/status/{tweet_id}")
        return True
    else:
        print(f"❌ Error posting tweet: {response.status_code}")
        print(response.json())
        return False

def post_tweet_v1(text, media_ids=None):
    """Post a tweet using Twitter API v1.1 (fallback)"""
    import requests
    from requests_oauthlib import OAuth1
    
    creds = load_credentials()
    if not creds:
        return False
    
    url = "https://api.twitter.com/1.1/statuses/update.json"
    
    auth = OAuth1(
        creds['api_key'],
        creds['api_secret'],
        creds['access_token'],
        creds['access_token_secret']
    )
    
    payload = {"status": text}
    if media_ids:
        payload["media_ids"] = ",".join(media_ids)
    
    response = requests.post(url, auth=auth, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        tweet_id = data['id_str']
        print(f"✅ Tweet posted successfully!")
        print(f"🔗 https://twitter.com/i/web/status/{tweet_id}")
        return True
    else:
        print(f"❌ Error posting tweet: {response.status_code}")
        print(response.json())
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: ./tweet.py 'Your tweet text here'")
        print("   or: ./tweet.py 'Tweet text' --media image.jpg")
        print("\nExamples:")
        print("  ./tweet.py 'Hello Twitter! 👋'")
        print("  ./tweet.py 'Check out my project!' --media screenshot.png")
        sys.exit(1)
    
    tweet_text = sys.argv[1]
    
    # Check length (Twitter limit is 280 characters)
    if len(tweet_text) > 280:
        print(f"❌ Tweet too long! {len(tweet_text)}/280 characters")
        print("\nConsider shortening or use a thread (not yet implemented)")
        sys.exit(1)
    
    print(f"📝 Preparing to tweet ({len(tweet_text)} characters)...")
    print(f"Text: {tweet_text}")
    
    # Try v2 first, fallback to v1
    success = post_tweet_v2(tweet_text)
    if not success:
        print("\n⚠️  v2 failed, trying v1.1...")
        success = post_tweet_v1(tweet_text)
    
    if not success:
        print("\n❌ Failed to post tweet. Check your credentials and API access.")
        sys.exit(1)

if __name__ == "__main__":
    main()
