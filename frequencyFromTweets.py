import pandas as pd

df = pd.read_csv("csvFiles/topBullTweets/topBullTweets.csv")
# create dataframe 
cols = ['Word', 'Frequency']
data = {}
for index, row in df.iterrows():
    tweet = row['tweet']
    listOfWords = tweet.split()
    for wordIndex in range(0,len(listOfWords)):
        word = listOfWords[wordIndex] #+ " " + listOfWords[wordIndex + 1] + " " + listOfWords[wordIndex + 2]  + " " + listOfWords[wordIndex + 3]+ " " + listOfWords[wordIndex + 4] +  " " + listOfWords[wordIndex + 5]
        if word in data:
            data[word] = data[word] + 1
        else:
            data[word] = 1
        wordIndex += 1
csvData = []
for word in data:
    if data[word] > 0:
        print(word + " -> freq: " + str(data[word])) 
    csvData.append([word, data[word]])

df = pd.DataFrame(csvData, columns=cols)

df.to_csv('csvFiles/topBullTweets/topBullWords.csv')


