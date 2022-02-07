from textblob import TextBlob # https://textblob.readthedocs.io/en/dev/install.html
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # https://pypi.org/project/vaderSentiment/
import pandas as pd # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk 
import typing

#https://towardsdatascience.com/two-sentiment-analysis-libraries-and-how-they-perform-3de4a06342ec

globalAnalyzer = SentimentIntensityAnalyzer()

def rounder(num):
    if num > 0.1: return 1
    if num < -0.1: return -1
    return 0

def lemmatization_of_sentence(sentence): # returns lemmatized sentence 
    sentenceList = sentence.split(" ")
    lemmatizer = WordNetLemmatizer()
    for word in sentenceList:
        word = lemmatizer.lemmatize(word)

def parts_of_speech(sentence):
    tokens = nltk.word_tokenize(sentence)
    print(nltk.pos_tag(tokens))

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

    globalAnalyzer.lexicon.update(words)

def sentiment_analysis():
    update_vader_lexicon("csv/cryptoWords.csv")

    df = pd.read_csv("tweets.csv")
    TBpol = []
    Vpol = []
    TBpol_rounded = []
    Vpol_rounded = []

    for index, row in df.iterrows():
        text = row['Text']

        # text preprocessing 
        # add step 1 
        lemmatizedSentence = lemmatization_of_sentence(text) # step 2
        cleanedSentence = remove_stop_words(lemmatizedSentence) # step 3

        # sentiment analysis
        TBpol.append(TextBlob(cleanedSentence).sentiment.polarity)
        Vpol.append(globalAnalyzer.polarity_scores(cleanedSentence)['compound'])
        TBpol_rounded.append(rounder(TextBlob(cleanedSentence).sentiment.polarity))
        Vpol_rounded.append(rounder(globalAnalyzer.polarity_scores(cleanedSentence)['compound']))

    df['TBPolarity'] = TBpol 
    df['VPolarity'] = Vpol
    df['TBRoundedPolarity'] = TBpol_rounded 
    df['VRoundedPolarity'] = Vpol_rounded

    df.to_csv("csvFiles/sentiment.csv", sep=',')

# print(globalAnalyzer.lexicon)
# sentiment_analysis()

# parts_of_speech("Coinbase user acquisition accelerated in the past two weeks to approx 1.2million/month run rate (ATH) Data: #bitcoin")
# lemmatization_of_sentence("Coinbase user acquisition accelerated in the past two weeks to approx 1.2million/month run rate (ATH) Data: #bitcoin")

#print(remove_stop_words("i love you"))