#!/usr/bin/python
import feedparser
# https://github.com/kurtmckee/feedparser
import praw
#http://pythonforengineers.com/build-a-reddit-bot-part-1/
from dateutil.parser import *
#parse rss
class submission:
	def __init__(self, link, title):
		self.link = link
		self.title = title

blogs_to_check = ["http://www.scottaaronson.com/blog/?feed=rss2", "http://slatestarcodex.com/feed/",\
 "http://agentyduck.blogspot.com/feeds/posts/default", "http://waitbutwhy.com/feed", "https://rationalconspiracy.com/feed/"]
links_to_submit = []



for blog_url in blogs_to_check:
	feed = feedparser.parse( blog_url )
	for article in feed["items"]:
	
		if 'title' in article:
			print article["title"]

		if 'date' in article:
			date= article["date"]

#	elif 'published_parsed' in article:      
#		date= article["published_parsed"]

		elif 'published' in article: 			###slatestarcodex, agentyduck, waitbutwhy, shtetl optimized 
			date= article["published"]

		parsed_date = parse(date)
		print parsed_date

		
		links_to_submit.append([article["title", parsed_date]])
		print "\n"

"""
#Determines which particular RSS fields this blog is using 
	for x in article:
		print x
"""
#praw 
agent_name = ("Rational_Blog_Autosubmitter 0.1")
reddit_instance = praw.Reddit(user_agent = agent_name)
