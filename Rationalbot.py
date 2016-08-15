#!/usr/bin/python
import feedparser
# https://github.com/kurtmckee/feedparser
import praw
#http://pythonforengineers.com/build-a-reddit-bot-part-1/


#parse rss

class to_submit:
	def __init__(self, link, title):
		self.link = link
		self.title = title

ssc_rss_url = "http://waitbutwhy.com/feed"
feed = feedparser.parse( ssc_rss_url )

for article in feed["items"]:
	if 'title' in article:
		print article["title"]
	if 'date' in article:
		print article["date"]
	print "\n"


#praw 
agent_name = ("SSC_autosubmitter_bot 0.1")
reddit_instance = praw.Reddit(user_agent = agent_name)
