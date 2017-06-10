#!/usr/bin/python

import json
import oauth2 as oauth
import tweepy
from secret_file import secret_file

class get_tweets(object):

    def __init__(self, secret_file):
        self.secret_file = secret_file

        auth = secret_file.get_auth
        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
        for tweets in public_tweets:
            print tweet.text

    def main(self):
        print ("Main function")
        get_tweets = get_tweets()

if  __name__ == '__main__':

    print ("name == main")
    secret_file = secret_file()
    tweets = get_tweets(secret_file)
