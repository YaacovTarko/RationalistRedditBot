# RationalistRedditBot
A bot to autosubmit content from popular rationalist blogs to reddit.com/r/rationality

Note: This script attempts to read the bot's username and password from a file called config_bot.py in the same directory as the script. To allow the bot to login, create a file called config_bot.py in the directory with the following contents:

REDDIT_USERNAME = '' #YOUR USERNAME as string
REDDIT_PASSWORD = '' # YOUR PASSWORD as string


Note: If you're running this script outside of the Pacific timezone, you'll need to modify the code slightly as indicated in the comments


Dependencies: 
feedparser  https://pypi.python.org/pypi/feedparser#downloads
praw https://praw.readthedocs.io/en/stable/

To install these modules type: 
pip install --user feedparser
pip install --user praw
into your command line


TODO: 
- authenticate via Oauth2, instead of with username and password
- make sure that if one of the RSS feeds goes down, the script keeps working for the others   ✅
- make it work regardless of time zone
