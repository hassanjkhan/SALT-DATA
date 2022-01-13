import pandas as pd

for i in range(5,7):
    print(i)
    df = pd.read_csv("csvFiles/topTweetsofMonthBear"+str(i)+".csv")
    # create dataframe 
    cols = ['Word', 'Frequency']
    data = {}
    for index, row in df.iterrows():
        tweet = row['tweet']
        listOfWords = tweet.split()
        for wordIndex in range(0,len(listOfWords)-2):
            doubleWord = listOfWords[wordIndex] + " " + listOfWords[wordIndex + 1] + " "+ listOfWords[wordIndex + 2]
            if doubleWord in data:
                data[doubleWord] = data[doubleWord] + 1
            else:
                data[doubleWord] = 1
            wordIndex += 1
csvData = []
for word in data:
    if data[word] > 5:
        print(word + " -> freq: " + str(data[word])) 
    csvData.append([word, data[word]])

df = pd.DataFrame(csvData, columns=cols)

df.to_csv('topBearTripleWords.csv')


