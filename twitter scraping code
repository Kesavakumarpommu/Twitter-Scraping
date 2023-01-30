import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient
import datetime
import streamlit as st


st.title(':blue[Twitter Scraping]')
st.markdown("<h1 style='text-align: right; color:gray;font-size:26px'>-by kesavakumar pommu</h1>", unsafe_allow_html=True)
a = st.text_input('Entre your Scraping Tweet Id:' )
st.write('The current Scraping tweets from', a)

f=a
x=st.slider("Select Your Range of tweets 10-1000",
            min_value=10,max_value=1000,step=5)
x=int(x)
st.write("Tweet count:",x)
b=st.date_input(
    "Tweets between : From" ,
    datetime.date(2022, 11, 1))
c=st.date_input(
    "To" ,
    datetime.date(2023, 1, 31))


st.write(x ,'tweets between',b,'to',c)

d={'x':f,'y':b,'z':c}



if st.button("Click Here"):




    tweets_list = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('{x} since:{y} until:{z}'.format_map(d)).get_items()):
        if i > x:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

    st.table(tweets_df)




# client = MongoClient('localhost',27017)
# db=client.test_database
# collection=db.test_collection
#
# tweets_df.reset_index(inplace=True)
# data_dict=tweets_df.to_dict("records")
#
# collection.insert_many(data_dict)
# print(collection)
#
