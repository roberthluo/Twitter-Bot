#!/usr/bin/python

import json
import oauth2 as oauth
import tweepy


class get_tweets(object):

    def __init__(self, secret_file):
        self.secret_file = secret_file

        auth = secret_file.get_auth
        api = tweepy.API(auth)

        print(api)
