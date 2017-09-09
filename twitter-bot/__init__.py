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
        #random.seed()
        self.TWITTERBOT_CONFIG = {}
        self.TWITTER_AUTHORIZED_CONNECTION = None

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
                self.TWITTERBOT_CONFIG[paramter] = value


        print(TWITTERBOT_CONFIG)

        #Update Fields

        #Create a connection to twitter
        self.TWITTER_CONNECTION = Twitter(auth=OAuth(self.BOT_CONFIG["OAUTH_TOKEN"],
                                                     self.BOT_CONFIG["OAUTH_SECRET"],
                                                     self.BOT_CONFIG["CONSUMER_KEY"],
                                                     self.BOT_CONFIG["CONSUMER_SECRET"]))


        def get_followers_list(self):
        """
            Returns the set of users that are currently following the user.
        """

        followers_list = []
        with open(self.BOT_CONFIG["FOLLOWERS_FILE"], "r") as in_file:
            for line in in_file:
                followers_list.append(int(line))



    #def create_stream(self, api):
        #myStreamListener = MyStreamListener()
        #myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener())
        #myStream.filter(track=['Trump'], async=True)
