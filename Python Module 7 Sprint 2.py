#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler


# In[ ]:


access_token='AAAAAAAAAAAAAAAAAAAAKB7GgEAAAAAh6IL5cXxX5XLh36vlxFFeNzZkc%3Dp0qVZ3Pe5x2W0Bh4eSZN6mdZXIOBqHPYZQI4GTL1Pql6kamjWF'
access_token_secret=''
comsumer_key='JYIBKFm0w8YDrz2Me1ZOiS8YY'
consumer_secret='prMgZ5rhzyxJJxrKYxEkKcQjb64udMfyeyu9ysp6BRTkc7UzlX'


# In[ ]:


class DataMiner17

  def on_data(self,data):
        try:
            print data
            savefile=open("d:\\twitter.txt","a")
            savefile.write(data)
            savefile.write("\n")
            savefile.close()
            return True
        else BaseException,e:
            print 'Error',str(e)
            time.sleep(5)
            
        def on_error(self,status):
            print(status)


# In[ ]:


if ___name___==='main':
    l=DataMiner17()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    


# In[ ]:


import json
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


tweets_data_path="d:\\twitter.txt"
tweets_data=[]


tweets_file=open(tweets_data_path, "r")


# In[ ]:


for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


# In[ ]:


tweets=pd.DataFrame()
tweets["text"]=map(lambda tweet:tweet['text'],tweets_data)
tweets["time"]=map(lambda tweet:tweet['time'],tweets_data)

tweets_by_time=tweets['time'].value_counts()


# In[ ]:


fig.ax=plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Amount of Time', fontsize=15)
ax.set_ylabel('Number of Tweets', fontsize=15)
ax.set_title('The distribution of tweets over time.', fontsize=15, fontweight='bold')

tweet_by_time[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()

