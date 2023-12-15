# twitter api
import tweepy
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
import pandas as pd

# Sentimental analysis
# Please insert Twitter API Credentials
# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# print api information
print(api)

# verify if the credentials are correct
try :
    api.verify_credentials()
    print("Authentication OK")
except :
    print("Error during authentication")

# check api rate limit for api calls
print("API rate limit: ", api.rate_limit_status()['resources']['search'])
# check time of reset
print("Reset time: ", api.rate_limit_status()['resources']['search']['/search/tweets']['reset'])

def tweets_getter(query, count, date):
    tweets = api.search_tweets(q=query, count=count, tweet_mode="extended", until=date, lang="en")
    tweets_df = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
    for i in range(len(tweets)):
        tweets_df.loc[i, "Time"] = tweets[i].created_at
        tweets_df.loc[i, "Tweet"] = tweets[i].full_text
        tweets_df.loc[i, "User"] = tweets[i].user.screen_name
        tweets_df.loc[i, "Location"] = tweets[i].user.location
        tweets_df.loc[i, "Retweets"] = tweets[i].retweet_count
        tweets_df.loc[i, "Likes"] = tweets[i].favorite_count
    return tweets_df

# Query: Twitter, Elon Musk, Mastodon, Jack Dorsey, Decentralized Social Network, Social Media, Twitter Takeover, Tesla
# Do this for 100 times
# Insert Desired Data
date_before = ""
#  make empty dataframes for each query
twitter = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
elon = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
mastodon = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
jack = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
decentralized = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
social = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
takeover = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])
tesla = pd.DataFrame(columns = ["Time", "Tweet", "User", "Location", "Retweets", "Likes"])

for i in range(10):
    # get tweets 100 times for each search query, use concat to add to the dataframe
    twitter = pd.concat([twitter, tweets_getter("Twitter", 100, date_before)])
    elon = pd.concat([elon, tweets_getter("Elon Musk", 100, date_before)])
    mastodon = pd.concat([mastodon, tweets_getter("Mastodon", 100, date_before)])
    jack = pd.concat([jack, tweets_getter("Jack Dorsey", 100, date_before)])
    decentralized = pd.concat([decentralized, tweets_getter("Decentralized Social Network", 100, date_before)])
    social = pd.concat([social, tweets_getter("Social Media", 100, date_before)])
    takeover = pd.concat([takeover, tweets_getter("Twitter Takeover", 100, date_before)])
    tesla = pd.concat([tesla, tweets_getter("Tesla", 100, date_before)])

# Turn all of the dataframes into separate csv files
twitter.to_csv("twitter.csv")
elon.to_csv("elon.csv")
mastodon.to_csv("mastodon.csv")
jack.to_csv("jack.csv")
decentralized.to_csv("decentralized.csv")
social.to_csv("social.csv")
takeover.to_csv("takeover.csv")
tesla.to_csv("tesla.csv")

# stopwords from nltk library
stop_words = set(stopwords.words('english'))

def sentiment(tweet):
    # do lemmatization, remove stop words, remove punctuation, remove numbers, emojis
    tweet = tweet.lower()
    tweet = tweet.split()
    tweet = [word for word in tweet if not word in stop_words]
    tweet = [word for word in tweet if word.isalpha()]
    tweet = [word for word in tweet if not word.isdigit()]
    tweet = " ".join(tweet)
    # sentiment analysis
    sent = TextBlob(tweet)
    return sent.sentiment.polarity

# add sentiment column to each dataframe
twitter["Sentiment"] = twitter["Tweet"].apply(sentiment)
elon["Sentiment"] = elon["Tweet"].apply(sentiment)
mastodon["Sentiment"] = mastodon["Tweet"].apply(sentiment)
jack["Sentiment"] = jack["Tweet"].apply(sentiment)
decentralized["Sentiment"] = decentralized["Tweet"].apply(sentiment)
social["Sentiment"] = social["Tweet"].apply(sentiment)
takeover["Sentiment"] = takeover["Tweet"].apply(sentiment)
tesla["Sentiment"] = tesla["Tweet"].apply(sentiment)

# go through each row of each dataframe and do sentiment analysis on tweet column using sentiment funciton
# add sentiment column to each dataframe
twitter["Sentiment"] = twitter["Tweet"].apply(sentiment)
elon["Sentiment"] = elon["Tweet"].apply(sentiment)
mastodon["Sentiment"] = mastodon["Tweet"].apply(sentiment)
jack["Sentiment"] = jack["Tweet"].apply(sentiment)
decentralized["Sentiment"] = decentralized["Tweet"].apply(sentiment)
social["Sentiment"] = social["Tweet"].apply(sentiment)
takeover["Sentiment"] = takeover["Tweet"].apply(sentiment)
tesla["Sentiment"] = tesla["Tweet"].apply(sentiment)

# print sentiment column of each dataframe
print(twitter['Tweet'], twitter["Sentiment"])
print(elon['Tweet'], elon["Sentiment"])

# drop all 0 sentiment rows
twitter = twitter[twitter["Sentiment"] != 0]
elon = elon[elon["Sentiment"] != 0]
mastodon = mastodon[mastodon["Sentiment"] != 0]
jack = jack[jack["Sentiment"] != 0]
decentralized = decentralized[decentralized["Sentiment"] != 0]
social = social[social["Sentiment"] != 0]
takeover = takeover[takeover["Sentiment"] != 0]
tesla = tesla[tesla["Sentiment"] != 0]

# print mean sentiment
print("Date:", date_before)
print("Twitter:", twitter["Sentiment"].mean())
print("Elon Musk:", elon["Sentiment"].mean())
print("Mastodon:", mastodon["Sentiment"].mean())
print("Jack Dorsey:", jack["Sentiment"].mean())
print("Decentralized Social Network:", decentralized["Sentiment"].mean())
print("Social Media:", social["Sentiment"].mean())
print("Twitter Takeover:", takeover["Sentiment"].mean())
print("Tesla:", tesla["Sentiment"].mean())