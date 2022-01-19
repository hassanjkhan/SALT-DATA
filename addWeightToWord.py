from textblob import TextBlob # https://textblob.readthedocs.io/en/dev/install.html
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # https://pypi.org/project/vaderSentiment/
import pandas as pd # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
import csv
from nltk.corpus import stopwords
import typing
import sentimentAnalysis

# globalAnalyzer = SentimentIntensityAnalyzer()

# def rounder(num):
#     if num > 0.05: return 1
#     if num < -0.05: return -1
#     return 0

# def remove_stop_words(sentence): # sentence is one string
#     stopcorpus: typing.List = stopwords.words('english')
#     sentenceList = sentence.split(" ")

#     for word in stopcorpus:
#         if word in sentenceList:
#             sentenceList.remove(word)

#     sentence = " ".join(sentenceList)
#     return sentence

def sentiment_analysis():
    df = pd.read_csv("csvFiles/topBullTweets/topBullTweets.csv")
    TBpol = []
    Vpol = []
    TBpol_rounded = []
    Vpol_rounded = []

    for index, row in df.iterrows():
        text = remove_stop_words(row['Text'])
        TBpol.append(TextBlob(text).sentiment.polarity)
        Vpol.append(globalAnalyzer.polarity_scores(text)['compound'])
        TBpol_rounded.append(rounder(TextBlob(text).sentiment.polarity))
        Vpol_rounded.append(rounder(globalAnalyzer.polarity_scores(text)['compound']))

    df['TBPolarity'] = TBpol 
    df['VPolarity'] = Vpol
    df['TBRoundedPolarity'] = TBpol_rounded 
    df['VRoundedPolarity'] = Vpol_rounded

    df.to_csv("csvFiles/sentiment.csv", sep=',')

# print(globalAnalyzer.lexicon)
sentiment_analysis()