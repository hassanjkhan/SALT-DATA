from textblob import TextBlob # https://textblob.readthedocs.io/en/dev/install.html
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # https://pypi.org/project/vaderSentiment/
import pandas as pd # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
import csv
from nltk.corpus import stopwords
import typing

#https://towardsdatascience.com/two-sentiment-analysis-libraries-and-how-they-perform-3de4a06342ec

globalAnalyzer = SentimentIntensityAnalyzer()

def rounder(num):
    if num > 0.1: return 1
    if num < -0.1: return -1
    return 0

def remove_stop_words(sentence): # sentence is one string
    stopcorpus: typing.List = stopwords.words('english')
    sentenceList = sentence.split(" ")

    for word in stopcorpus:
        if word in sentenceList:
            sentenceList.remove(word)

    sentence = " ".join(sentenceList)
    return sentence
    
def update_vader_lexicon(csvFile):
    df = pd.read_csv(csvFile)
    words = {}
    
    for index, row in df.iterrows():
        word = row['Word']
        weight = row['Weight']
        words[word] = weight
        print(words)

    globalAnalyzer.lexicon.update(words)

def sentiment_analysis():
    update_vader_lexicon("cryptoWords.csv")
    
    df = pd.read_csv("tweets.csv")
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

    df.to_csv("sentiment.csv", sep=',')
    print(df)


sentiment_analysis()
#print(remove_stop_words("i love you"))