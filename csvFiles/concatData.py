import pandas as pd 
import glob 
import os 
import sys 

# Call the File with one argument, the NAME of the folder which contains the files you wish to merge 
# EX: python concatData.py Bull01 will merge all csv's in Bull01
def concat(*argv):
    argCount = len(sys.argv)
    if argCount != 2:
        print("Pass the name of the folder which contains the files you wish to merge! Exiting now")
        exit() 
    else:
        path = os.getcwd() + "\\"+ str(sys.argv[1])
        # print("current path is -> " + path)
        # for i in range(1,argCount):
        #     print(str(i) + str(sys.argv[i]))
        joinedFiles = os.path.join(path ,"topTweets*.csv")
        joinedList = glob.glob(joinedFiles)
        df = pd.concat(map(pd.read_csv, joinedList), ignore_index=True)
        df.to_csv(str(sys.argv[1])+"\\topBearTweets.csv")

if __name__ == "__main__":
    concat()