#!/usr/bin/python

import json
import oauth2 as oauth
import tweepy

class secret_file():

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""


    def __init__(self):

        global consumer_key
        global consumer_secret
        global access_token
        global access_token_secret

        consumer_key="aaaaa"
        consumer_secret="bbbbbb"

        access_token="ccccccc"
        access_token_secret="dddddd"


        #consumer = oauth.consumer(key=consumer_key, secret=consumer_secret);
        #access_token = oauth.Token(key=access_token, secret= access_token_secret)
        #client = oauth.Client(consumer, access_token)

    def get_test(self):


        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()


        for tweet in public_tweets:
            print tweet.text
        return auth
