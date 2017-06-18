#!/usr/bin/python

import json
import oauth2 as oauth
import tweepy

from get_tweets import get_tweets

#https://dev.twitter.com/overview/api/response-codes

class twitter_bot(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the StreamListener
            return False

    def create_stream(self, api):
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener())
        myStream.filter(track=['Trump'], async=True)
