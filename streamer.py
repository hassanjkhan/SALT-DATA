from tweepy.models import Status
import config 
import tweepy 
import configparser 
import pandas as pd  
import csv 

class TwitterStreamListener(tweepy.Stream): 
    # handles data received from the stream 
    # stream is the choice instead of search because stream is real time 
  
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = config.api_key
        self.consumer_secret = config.api_key_secret
        self.access_token = config.access_token
        self.access_token_secret = config.access_token_secret
        super().__init__(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        self.counter = 0
        self.limit = 5
        self.csvfile = open('tweets.csv', 'a')
        self.csvWriter = csv.writer(self.csvfile)
        self.csvWriter.writerow(['Time', 'User', 'Retweets', 'Likes', 'Text'])

    # function that gets the tweets from the stream into the 'status' object
    def on_status(self, status):
        row = [status.created_at, status.user.name, status.retweet_count, status.favorite_count, status.text.encode('utf-8')]
        self.csvWriter.writerow(row)
        self.counter += 1 
        if self.counter < self.limit:
            return True 
        else:
            self.disconnect() 

    # function will be triggered whenever there is an error streaming tweets 
    # status_code contains the type of error that has occured 
    def on_error(self, status_code): 
        print('ERROR has status code: ' + str(status_code))
        return True # in order to continue listening

    # function will be triggered whenever there is a network issue preventing listener from fetching the stream 
    def on_timeout(self):
        print('Timeout...')
        return True # in order to continue listening

if __name__ == "__main__":
    # read configs 
    api_key = config.api_key
    api_key_secret = config.api_key_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret 
    # authentication 
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    listener = TwitterStreamListener(api_key, api_key_secret, access_token, access_token_secret)
    listener.filter(track=['#covid','#Covid'])