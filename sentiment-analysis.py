from textblob import TextBlob # https://textblob.readthedocs.io/en/dev/install.html
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # https://pypi.org/project/vaderSentiment/
import pandas as pd
#https://towardsdatascience.com/two-sentiment-analysis-libraries-and-how-they-perform-3de4a06342ec

def rounder(num):
    if num > 0: return 1
    if num < 0: return -1
    return 0

def sentiment_analysis():
    analyzer = SentimentIntensityAnalyzer()

    # Reading the data
    df = pd.read_csv("tweets.csv")

    TBpol = []
    Vpol = []
    TBpol_rounded = []
    Vpol_rounded = []

    for index, row in df.iterrows():
        text = row['tweets']
        # print(index , '->' , row['tweets'])
        TBpol.append(TextBlob(text).sentiment.polarity)
        Vpol.append(analyzer.polarity_scores(text)['compound'])
        TBpol_rounded.append(rounder(TextBlob(text).sentiment.polarity))
        Vpol_rounded.append(rounder(analyzer.polarity_scores(text)['compound']))

    df['TBPolarity'] = TBpol 
    df['VPolarity'] = Vpol
    df['TBRoundedPolarity'] = TBpol_rounded 
    df['VRoundedPolarity'] = Vpol_rounded

    print(df)

sentiment_analysis()