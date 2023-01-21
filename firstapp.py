import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
import datetime
import streamlit as st



st.title(':blue[Twitter Scraping]')
title = st.text_input('Entre your Scraping Tweet Id:' )
st.write('The current Scraping tweets from', title)
x=st.slider("Select Your Range of tweets 500-1500",
            min_value=500,max_value=1500,step=50)
st.write("Tweet count:",x)
d=st.date_input(
    "Tweets between : From" ,
    datetime.date(2021, 1, 1))
c=st.date_input(
    "To" ,
    datetime.date(2023, 1, 21))


st.write(x ,'tweets between',d,'to',c)


# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{} since:{} until:{}'.format(title,d,c)).get_items()):
    if i>5000:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

st.table(tweets_df)

client = MongoClient('localhost',27017)
db=client.test_database
collection=db.test_collection

tweets_df.reset_index(inplace=True)
data_dict=tweets_df.to_dict("records")
data_dict
collection.insert_many(data_dict)
collection.find()

st.table(tweets_df)
