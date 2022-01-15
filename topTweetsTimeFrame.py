import config 
import tweepy 
import configparser 
import pandas as pd  
import datetime
import twint # https://github.com/twintproject/twint


# # these dates are of bitcoin bull run from  dec 4 2020 to jan 13 2021
# # the price went from 23,852 CAD to 47,293 CAD in that time frame
'''
BULL RUN TIMELINES: 
2017: (1000 USD -> 19,500 USD) whole year was uptrend 
    Bull01: 2017-04-01 -> 2017-10-15 (~1000 USD -> ~4200 USD)
    Bull02: 2017-10-20 -> 2017-12-17 (~4200 USD -> ~19,200 USD)
2018: had runs but couldnt support high levels, leading to crash @ EOY 2018  
    Bull03: 2018-02-01 -> 2018-03-04 (~7000 USD -> ~11,500 USD)
    Bull04: 2018-04-05 -> 2018-05-04 (~6800 USD -> ~10,000 USD) 
2019: had a very good recovery from EOY 2018 crash 
    Bull05: 2019-04-01 -> 2019-07-07 (~4200 USD -> ~13,000 USD) 
    Bull06: 2019-07-20 -> 2019-08-10 (~9000 USD -> ~12,000 USD)
    Bull07: 2019-10-18 -> 2019-11-05 (~7000 USD -> ~9500 USD)
2020: had strong start then crash but overall recovered well by EOY 2020 
    Bull08: 2020-03-13 -> 2020-08-30 (~5000 USD -> ~12,300 USD)
    Bull09: 2020-10-01 -> 2020-12-31 (~10,000 -> ~29,000 USD) 
2021: huge bull run to start, bear market from may-july, ended year on good bull run 
    Bull10: 2021-01-01 -> 2021-04-09 (~30,000 USD -> ~64,000 USD)
    Bull11: 2021-07-20 -> 2021-11-30 (~32,000 USD -> ~68,000 USD)

BEAR RUN TIMELINES: 
2018: 
    Bear01: 2018-01-05 -> 2018-02-04 (~17,000 USD -> ~7000 USD)
    Bear02: 2018-03-20 -> 20218-04-10 
    Bear03: 2018-05-05 -> 2018-07-12 
    Bear04: 2018-09-06 -> 2018-12-31 
2019: 
    Bear05: 2019-01-01 -> 2019-03-28 
    Bear06: 2019-07-10 -> 2019-07-30 
    Bear07: 2019-09-22 -> 2019-10-23 
    Bear08: 2019-11-08 -> 2019-12-31 
2020:
    Bear09: 2020-02-22 -> 2020-03-15 
2021:
    Bear10: 2021-01-13 -> 2021-02-04 
    Bear11: 2021-05-11 -> 2021-07-23 
    Bear12: 2021-11-19 -> 2021-12-31 
'''

# configuration 
months = range(11,13)

for i in months:
    c = twint.Config() 
    c.Search = "bitcoin"
    c.Lang = "en"
    c.Limit = 3000
    if (i==months[0]):
        c.Since = "2021-"+str(i)+"-19"
    else:
        c.Since = "2021-"+str(i)+"-01"
    if (i==months[1]):
        c.Until = "2021-"+str(i)+"-31"
    else:
        if(i==2):
            c.Until = "2021-"+str(i)+"-28"
        else:
            c.Until = "2021-"+str(i)+"-30"
    c.Min_likes = 100 
    c.Min_retweets = 100 
    c.Store_csv = True
    c.Output = "topTweetsBear12-" + str(i) + ".csv"

    # running search
    twint.run.Search(c)