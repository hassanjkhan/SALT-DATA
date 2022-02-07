from numpy import column_stack, rint
import pandas as pd 
from langdetect import detect 

df = pd.read_csv('TrainingData/training-data-positive-sentiment.csv')
print('Num of rows -> '+str(len(df.index)))

cols = ['Date','text','Sentiment']
data = [] 

count = 0 

for index, row in df.head(30000).iterrows():
    print("count is "+str(count))
    count+=1 
    if row.empty:
        print("dropping row")
        # df.drop([index], inplace=False)
    else:
        tmp = False 
        try:
            lang = detect(df.at[index,'text'])
            tmp=True 
        except:
            print("dropping row")
            tmp=False 
            # df.drop([index], inplace=False)
        if tmp == False :
            print("dropping row")
            # df.drop([index], inplace=False)
        else:
            data.append([df.at[index,'Date'],df.at[index,'text'],df.at[index,'Sentiment']])
            print("keeping row")

res_df = pd.DataFrame(columns=cols, data=data)
res_df.to_csv('TrainingData/training-data-positive-sentiment-english.csv')
# pos_df = df[df['Sentiment'] == 'Positive']
# pos_df.to_csv('TrainingData/training-data-positive-sentiment.csv')

# df.drop_duplicates(inplace=True)
# df.to_csv('training-data-no-duplicates.csv')
# print('Num of rows -> '+str(len(df.index)))

# counter = 0 
# res_df = pd.DataFrame(columns=cols)

# for index, row in df['text'].iteritems():
#     print("counter is "+str(counter))
#     if counter < 5000:
#         print("new row count -> "+str(len(df.index)))
#         if row == "" or df.at[index,'Sentiment']!="Negative":
#             print("dropping row")
#             df.drop([index], inplace=False)
#         else:
#             try:
#                 lang = detect(row)
#             except:
#                 print("dropping row")
#                 df.drop([index], inplace=False)
#             if lang != "en":
#                 print("dropping row")
#                 df.drop([index], inplace=False)
#             else:
#                 counter+=1
#                 data.append([df.at[index,'Date'],df.at[index,'text'],df.at[index,'Sentiment']])
#                 print("keeping row")

#     else:
#         break

# result_df = pd.DataFrame(data, columns=cols)
# result_df.to_csv('training-negative.csv')