import os
import sys
import time
import random
import yaml
import json
#import oauth2 as oauth
import tweepy
from os import getenv
#from get_tweets import get_tweets
#from logs import Logs


#https://dev.twitter.com/overview/api/response-codes

class twitter_bot(tweepy.StreamListener):


    def __init__(self):
        random.seed()


    def on_status(self, status):
        print(status.text)


    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the StreamListener
            return False

    def bot_setup(self, config_file="config.yaml"):
        with open(config.yaml, 'r') as stream:
            for line in stream:
                line = line.split(":")
                paramter = line[0].strip
                value = line[1].strip()


    #def create_stream(self, api):
        #myStreamListener = MyStreamListener()
        #myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener())
        #myStream.filter(track=['Trump'], async=True)
