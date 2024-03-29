
# coding: utf-8

# In[2]:


import string
import operator
import sys

def TopTweets(INPUT_FILE_PATH,Count,N):
    with open (INPUT_FILE_PATH, encoding = "utf-8") as file:
        tweets=file.readlines()
    lst = {}
    for line in tweets:   
        #print(dat)
        fileTmp = line.split()
        if fileTmp[0] in lst:
            lst[fileTmp[0]] +=1
        else:
            lst[fileTmp[0]] = 1
    lst = sorted(lst.items(), key = operator.itemgetter(1), reverse = True)

    outputFile = open('C:/Users/shrav/Documents/Python Scripts/TopTweets.txt', 'w', encoding = "utf-8")
    outputFile.write("The top " + Count + " users who have tweeted the most for the entire timeline: \n")
    for i in range (0,N):
        outputFile.write("User Name: " + lst[i][0] + " and Number of tweets: " + str(lst[i][1]) + "\n")
        
    outputFile.close

def MaxFollowers(INPUT_FILE_PATH,Count,N):
    with open (INPUT_FILE_PATH, encoding = "utf-8") as file:
        tweets=file.readlines()

    lst = {}
    for line in tweets:
        fileTmp = line.split()
        if fileTmp[0] not in lst:
            lst[fileTmp[0]] = fileTmp[-2]

    lst = sorted(lst.items(), key = operator.itemgetter(1), reverse = True)
    
    outputFile = open('C:/Users/shrav/Documents/Python Scripts/MaxFollowers.txt', 'w', encoding = "utf-8")
    outputFile.write("The top " + Count + "users who has the maximum followers: " + "\n\n")

    for i in range (0, N):
        outputFile.write(str(i+1) + ". Username: " + lst[i][0] + " : Number of Followers: " + str(lst[i][1]) + "\n\n")
    outputFile.close


def TweetPerHour(INPUT_FILE_PATH,Count,N):
    
    with open (INPUT_FILE_PATH, encoding = "utf-8") as file:
        tweets=file.readlines()

    lst = {}
    for line in tweets:
        fileTmp = line.split()
        fileTmp2 = fileTmp[1].split(":")
        twitTmp = fileTmp[0] + " " + fileTmp2[1]
        if twitTmp in lst:
            lst[twitTmp]+=1
        else:
            lst[twitTmp]=1
    lst = sorted(lst.items(), key = operator.itemgetter(1), reverse = True)

    lst2={}
    totalUsersIn = 0
    for line in lst:
        totalUsersIn+=1
        if(line[0].split()[1]) in lst2:
            lst2[line[0].split()[1]]+=1
        else:
            lst2[line[0].split()[1]]=1
    lst2 = sorted(lst2.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = N*len(lst2)
    outputFile = open('C:/Users/shrav/Documents/Python Scripts/TweetPerHour.txt', 'w', encoding = "utf-8")
   
    outputFile.write("The top " + Count + " users who have tweeted the most per hour: " + "\n\n")
    for x in range (0,len(lst2)):
   
        mSearch = N
        
       
        for line in lst:
            if mSearch == 0:
                break
            if line[0].split()[1] == lst2[x][0]:
                outputFile.write("Username: " + line[0].split()[0] + "\n\n")
                
                mSearch-=1
    outputFile.close

def retweetCount(INPUT_FILE_PATH,Count,N):
    
    with open (INPUT_FILE_PATH, encoding = "utf-8") as file:
        tweets=file.readlines()

    lst = {}
    for line in tweets:
        fileTmp = line.split()
        y = len(fileTmp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += fileTmp[x] + " "
        tweet += " ::::;:::: " + fileTmp[0]
  
        if tweet not in lst:
            lst[tweet] = fileTmp[-1]

    outputFile = open('C:/Users/shrav/Documents/Python Scripts/RetweetCount.txt', 'w', encoding = "utf-8")
	   
    lst = sorted(lst.items(), key = operator.itemgetter(1), reverse = True)
    outputFile.write("The top "+ Count + " tweets that have the maximum retweet: " + "\n\n")

    for x in range (0, N):
        outputFile.write("\n Tweet: " +
                      lst[x][0].split("::::;::::")[0]  + "\n\n")
    outputFile.close


INPUT_FILE = input("Enter input file path: ")
INPUT_FILE_PATH = INPUT_FILE+ '.txt'
Count=input("Enter number of users who tweeted most: ")
N=int(Count)

TopTweets(INPUT_FILE_PATH,Count,N)
MaxFollowers(INPUT_FILE_PATH,Count,N)
TweetPerHour(INPUT_FILE_PATH,Count,N)
retweetCount(INPUT_FILE_PATH,Count,N)


# In[23]:


import tweepy       
import pandas as pd     
import numpy as np      
from textblob import TextBlob

def SentimentAnalysis(INPUT_FILE_PATH):
    tweets_all = []
    with open (INPUT_FILE_PATH, encoding = "utf-8") as file:
        tweets=file.readlines()
    lst = {}
    for line in tweets:       
        fileTmp = line.split('"')
        tweets_all.append(fileTmp[1])
    #print(tweets_all)
   
    outputFile = open('C:/Users/shrav/Documents/Python Scripts/SentimentResult.txt', 'w', encoding = "utf-8")
    
    for tweet in tweets_all:
        #print(tweet.text)
        analysis = TextBlob(tweet)
        #print(analysis.sentiment)
        if analysis.sentiment[0]>0:
             outputFile.write( 'Sentiment Result: Positive ' +'"'+tweet+'"'+"\n\n")
        elif analysis.sentiment[0]<0:
            outputFile.write( 'Sentiment Result: Negative '+'"'+tweet+'"'+"\n\n")
        else:
            outputFile.write( 'Sentiment Result: Neutral '+'"'+tweet+'"'+"\n\n")
    outputFile.close
    
INPUT_FILE = input("Enter input file path: ")
INPUT_FILE_PATH = INPUT_FILE+ '.txt'
SentimentAnalysis(INPUT_FILE_PATH)

