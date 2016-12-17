import tweepy
from textblob import TextBlob


#authorization info
consumer_key = 'foo.bar'
consumer_secret = 'foo.bar'

access_token = 'foo.bar'
access_token_secret =  'foo.bar'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#search public tweets containing this string
public_tweets = api.search('Politics')

#print out the tweets found, and their sentiment analysis
for tweet in public_tweets:
	print(tweet.text.encode("utf-8"))
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('\n')
