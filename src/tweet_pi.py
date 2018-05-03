#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from os import path
import datetime

CONSUMER_KEY = 'here is yout consumer key'
CONSUMER_SECRET = 'here is your consumer secret key'
ACCESS_TOKEN = 'access token'
ACCESS_TOKEN_SECRET = 'access token secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

recent_tweet = api.home_timeline()[0].id


sentence = ""
sentence = ""
image_file = "iku.jpg"

def ikuikureply():
    keyword = str(input("please enter keyword!: "))
    file_name = image_file
    # return recent 20 tweet
    twi_lst =  [[tweet.text, tweet.author.screen_name, tweet.id] for tweet in api.home_timeline()]
    if twi_lst[0][2] == recent_tweet:
        for obj in twi_lst:
            if keyword in  obj[0]:
                target_screen_name = "@" + obj[1]
                target_id = obj[2]
                api.create_favorite(target_id)
                image_url = path.abspath(__file__)[:-11] + file_name
                api.update_with_media(
                    image_url,
                    status = " ".join([target_screen_name, sentence]),
                    in_reply_to_status_id = target_id
                )

try:
    print(path.abspath(__file__)[:-11] + image_file)
    ikuikureply()
    print("now tweeting")
    print("go well!")
except tweepy.error.TweepError as e:
    print("error response code: " + str(e.response.status))
    print("error messate: " + str(e.response.reason))
        
