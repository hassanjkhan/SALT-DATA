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


until_pretense = '2022-03-'
date = 1
data = [] 

for i in range(date,20):
    
    # fetch tweets 
    public_tweets = api.search_tweets(q='bitcoin', until=until_pretense + str(i), count=100, result_type='popular')

    # create dataframe 
    cols = ['Time', 'User', 'Retweets', 'Likes', 'Tweet']
    for tweet in public_tweets: 
        data.append([tweet.created_at, tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count, tweet.text.encode('utf-8')])

df = pd.DataFrame(data, columns=cols)

df.to_csv('topTweets.csv')