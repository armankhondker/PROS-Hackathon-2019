import tweepy
import csv
from textblob import TextBlob
import re

consumer_key= '5Bt339IyUsg0QdX5vbevyk4bO'
consumer_secret= 'R5H5eP7ebouTb9qS04sfi6R6Yi5LzImszrA8KJEHAul5oXlpn6'

access_token='1131250496717709312-lZBpVPv5iEBQ4EuxeIkvZzCHppa6uB'
access_token_secret='Ugscei2cYZrT3N30NrhERsDIlGYQYP0ovE2kAAo9gTvxC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dell Laptop', result_type = 'mixed', count = 100, lang = 'en')
public_tweets1 = api.search('Dell Laptop', result_type = 'recent', count = 100, lang = 'en')

def clean_tweet( tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

with open('tweets.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tweet", "Sentiment Score", "Subjectivity Score"])
    totalSent = 0
    totalSubj = 0
    count = 0 
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        print(tweet.text)
        print(analysis.sentiment)
        print("")
        score = analysis.sentiment.polarity
        subject = analysis.sentiment.subjectivity
        count= count + 1
        totalSent= totalSent + score
        totalSubj= totalSubj + subject
        writer.writerow([clean_tweet(tweet.text), score, subject])
    for tweet in public_tweets1:
        analysis = TextBlob(tweet.text)
        print(tweet.text)
        print(analysis.sentiment)
        print("")
        score = analysis.sentiment.polarity
        subject = analysis.sentiment.subjectivity
        count= count + 1
        totalSent= totalSent + score
        totalSubj= totalSubj + subject
        writer.writerow([clean_tweet(tweet.text), score, subject])
    writer.writerow(['Average Sentmient Score', totalSent/count])
    writer.writerow(['Average Subjectivity Score', totalSubj/count])

print("Logged tweeted sentiments of {0} tweets to tweets.csv".format(len(public_tweets) + len(public_tweets1)))
print("The Average Sentiment Score is {0}".format(totalSent/count))
print("The Average Subjectivity Score is {0}".format(totalSubj/count))
