#!/usr/bin/python

import json
import oauth2 as oauth
import tweepy

from secret_file import secret_file

class get_tweets(object):

    api = object()

    def __init__(self, secret_file):

        global api
        self.secret_file = secret_file

        print (secret_file)
        api = secret_file.get_api()
        print (type(api))
        #print ("auth",auth)
        #api = tweepy.API(auth)


    def main(self):
        print ("Main function")
        get_tweets = get_tweets()

    def get_timeline(self):
        print ("public timeline")
        public_tweets = api.home_timeline()

        for tweet in public_tweets:
            print (tweet.text)

    def get_user(self, user_name):
        user = api.get_user(user_name)
        print (user.screen_name)
        print (user.followers_count)
        #print user.tweets
        timeline = api.user_timeline(screen_name = user_name, count = 100, include_rts = True)

        for tweet in timeline:
            print (tweet.created_at, tweet.text, '\n')

    def get_all_followers(self):
        for follower in tweepy.Cursor(api.followers).item():
            follower.follow()

    def update_own_status(self, status):
        api.update_status(status)

if  __name__ == '__main__':

    print ("name == main")
    secret_file = secret_file()
    #print (secret_file)
    tweets = get_tweets(secret_file)

    tweets.get_user("realdonaldtrump")

    tweets.update_own_status("Hi, I am a twitter bot!")
