import config 
import tweepy 
import configparser 
import pandas as pd  

# read configs 
api_key = config.api_key
api_key_secret = config.api_key_secret
access_token = config.access_token
access_token_secret = config.access_token_secret 

# authentication 
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# fetch home timeline 
public_tweets = api.home_timeline() 

# create dataframe 
cols = ['Time', 'User', 'Tweet']
data = [] 
for tweet in public_tweets: 
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=cols)

df.to_csv('tweets.csv')