import config 
import tweepy 
import configparser 
import pandas as pd  
import datetime
import twint # https://github.com/twintproject/twint

# configuration 
c = twint.Config() 
c.Search = "bitcoin"
c.Lang = "en"
c.Limit = 10
c.Since = "2021-12-04"
c.Until = "2021-12-30"
c.Min_likes = 10 
c.Min_retweets = 10 
c.Store_csv = True
c.Output = "custom_out.csv"

# running search
twint.run.Search(c)