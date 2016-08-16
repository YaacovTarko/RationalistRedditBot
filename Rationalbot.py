#!/usr/bin/python

import feedparser     # https://github.com/kurtmckee/feedparser
import praw           #http://pythonforengineers.com/build-a-reddit-bot-part-1/
from dateutil.parser import *   #parse rss dates
import datetime       #https://docs.python.org/3/library/datetime.html#timedelta-objects

now = datetime.datetime.now()
now += datetime.timedelta(hours=7) #account for the fact that I'm in the pacific timezone, and the dates provided by RSS are in GMT. 
#If you're running this script somewhere else, change time accordingly

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

		elif 'published' in article: 			#used for slatestarcodex, agentyduck, waitbutwhy, shtetl optimized 
			date= article["published"]

		#time formatting
		#Converts to type datetime.datetime 
		parsed_date = parse(date)
		print parsed_date 
		parsed_date_unaware = parsed_date.replace(tzinfo=None)  #strips time zone info to allow arithmetic operations with 'now'


		#check if the article was published recently
		published_recently = (datetime.timedelta(hours=24) > (now - parsed_date_unaware))
		if published_recently:
			links_to_submit.append([article["title"], article["link"]])
		print "\n"

		print len(links_to_submit)
		
	"""		
#Determines which particular RSS fields this blog is using 
		for x in article:
			print x
		print "\n"
	"""
#praw 
agent_name = ("Rational_Blog_Autosubmitter 0.1")
reddit_instance = praw.Reddit(user_agent = agent_name)


