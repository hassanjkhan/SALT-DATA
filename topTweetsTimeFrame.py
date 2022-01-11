import config 
import tweepy 
import configparser 
import pandas as pd  
import datetime
import twint 

# configuration 
c = twint.Config() 
c.Search = "bitcoin"
c.Lang = "en"
c.Limit = 10
c.Since = "2020-04-04"
c.Until = "2020-04-06"
c.Store_csv = True
c.Output = "custom_out.csv"

# running search
twint.run.Search(c)

# # read configs 
# api_key = config.api_key
# api_key_secret = config.api_key_secret
# access_token = config.access_token
# access_token_secret = config.access_token_secret 

# # authentication 
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
# api.wait_on_rate_limit = True
# start_date = datetime.date(2020, 12, 4)
# end_date = datetime.date(2021, 1, 13)
# delta = datetime.timedelta(days=1)

# cols = ['Time', 'User', 'Retweets', 'Likes', 'Tweet']
# data = [] 

# # while start_date <= end_date:
# #     print(start_date)
# #     public_tweets = api.search_tweets(q='bitcoin', until=start_date, count=50, result_type='popular')
# #     print(public_tweets)

# #     for tweet in public_tweets: 
# #         print(tweet.created_at)
# #         data.append([tweet.created_at, tweet.user.screen_name, tweet.retweet_count, tweet.favorite_count, tweet.text.encode('utf-8')])

# #     start_date += delta
# # these dates are of bitcoin bull run from  dec 4 2020 to jan 13 2021
# # the price went from 23,852 CAD to 47,293 CAD in that time frame

# df = pd.DataFrame(data, columns=cols)

# df.to_csv('topTweets.csv')