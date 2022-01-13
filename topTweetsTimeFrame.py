import config 
import tweepy 
import configparser 
import pandas as pd  
import datetime
import twint # https://github.com/twintproject/twint

# configuration 
months = [5,6]
# # these dates are of bitcoin bull run from  dec 4 2020 to jan 13 2021
# # the price went from 23,852 CAD to 47,293 CAD in that time frame
for i in months:
    c = twint.Config() 
    c.Search = "bitcoin"
    c.Lang = "en"
    c.Limit = 200
    c.Since = "2020-"+str(i)+"-09"
    c.Until = "2021-"+str(i)+"-30"
    c.Min_likes = 100 
    c.Min_retweets = 100 
    c.Store_csv = True
    c.Output = "topTweetsofMonthBear" + str(i) + ".csv"

    # running search
    twint.run.Search(c)