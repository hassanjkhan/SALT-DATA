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

text_query = 'bitcoin'
since_date = '202012041900' # 'yyyyMMddHHmm'
until_date = '202101131900' 
# these dates are of bitcoin bull run from  dec 4 2020 to jan 13 2021
# the price went from 23,852 CAD to 47,293 CAD in that time frame
max_tweets = 10
api.wait_on_rate_limit = True
# Creation of query method using parameters
#public_tweets = tweepy.Cursor(api.search_full_archive,label="",tag="",query=text_query, since=since_date, until=until_date).items(max_tweets)
#public_tweets = api.search_full_archive(label, query, *, tag, fromDate, toDate, maxResults, next)¶
#public_tweets = api.search_full_archive("staging",since_date, until_date)
public_tweets=tweepy.Cursor(api.search_full_archive,label='staging', query=text_query, fromDate=since_date,toDate=until_date).items(max_tweets)
# create dataframe 
cols = ['Time', 'User', 'Tweet']
data = [] 
for tweet in public_tweets: 
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=cols)

df.to_csv('tweetsFrame.csv')