# Unofficial Google Search Bot for Telegram
Telegram bot (support both inline/chat) that return search results (web/image)
from Google

## What's Different in This Version
This version uses the `google-search-results` library instead of Google's Custom Search API, which means:
- **No API key required** ✅
- **No daily quota limits** ✅
- **Unlimited searches** ✅
- Uses web scraping (may be rate-limited by Google)

## How to use
Clone and host your own bot. The setup is simpler without needing Google API credentials.

## Run instruction
```
git clone https://github.com/abnjo/Toooogle
cd Toooogle
pip install -e .
PYTHONPATH=src python3 src/app/__init__.py
```
You might want to do this in a venv env

After setting up these you'll have to fill in your config.json with your Telegram bot token

### Hosting on pythonanywhere
One easy option to host the bot freely is on PAW. In your web console you should
set the source directory to src and modify the WSGI config file based on the
sample given in this repo (misc/pythonanywhere_com_wsgi.py)

## config.json
This file holds constants that should be kept outside of the repo.
config.json should be a text file of valid serialized JSON. The following fields
must be present:
- telegram_bot_token
  - Your telegram bot token. You need to obtain it via @BotFather following the
  instructions outlined at https://core.telegram.org/bots
- allow_only_users
  - You could limit who could use the bot hosted by you. You can either
  whitelist a user by id or username. Example: [999999,"fancy_user"] would allow
  the 2 users to use your hosted bot. An empty list would allow all
- paw_app
  - Useful only when you are hosting on PAW (See
  [Hosting on pythonanywhere](#hosting-on-pythonanywhere) for more details)
  - url
    - The URL of your web app
  - webhook_secret
    - Any string, must be valid URL character

## Dependency
- Python 3
- Telepot (https://github.com/nickoala/telepot)
- google-search-results (https://github.com/taosdata/google-search-results)
- requests
- flask
