__author__ = 'shinsakairi'

#Import the necessary methods from tweepy library
import os

import tweepy

from slistener import StrListener


#Variables that contains the user credentials to access Twitter API, replace the token&key with yours
access_token = "your access_token"
access_token_secret = "your token secret
consumer_key = "your consumer_key "
consumer_secret = "your key secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

threads = []

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    tweets_num = input("How many tweets do you want to download?(Input numbers):")
    data_dir = raw_input("Where do you what to store the data?(Input dir like './'):")
    data_dir = data_dir.strip()
    data_dir = data_dir.rstrip()
    os.makedirs(data_dir + '/data')
    os.makedirs(data_dir + '/html')

    l = StrListener(api, tweets_num, data_dir)
    stream = tweepy.Stream(auth, l)
    print("Connecting to twitter, download in process, please wait...")

    try:
        stream.sample()
    except:
        #print "Error!"
        stream.disconnect()

