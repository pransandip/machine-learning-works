"""
The purpose of this script is to build upon the twitter_streamer.py script --
by importing its TwitterStreamer class and loading the collected, streamed tweets
into a MongoDB database.
"""
## Importing Related Modules
import config

#create a Mongo database called twitter_data
LOCAL_DB = config.LOCAL_CLIENT.twitter_data

#create a Mongo collection inside twitter_data
LOCAL_COLL = LOCAL_DB.tweet_dicts_stream

def load_tweets(tweet):
    LOCAL_COLL.insert_one(tweet)