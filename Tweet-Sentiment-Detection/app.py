import twitter_streamer
import database 

if __name__ == "__main__":
    
    twitter_streamer = twitter_streamer.TwitterStreamer(['Data Science'])
    twitter_streamer.stream_tweets(10, database.load_tweets)
    