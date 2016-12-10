import tweepy
from textblob import TextBlob


#authorization info
consumer_key = 'INSERT_CONSUMER_KEY'
consumer_secret = 'INSERT_CONSUMER_KEY_SECRET'

access_token = 'INSERT_ACCESS_TOKEN'
access_token_secret =  'INSERT_ACCESS_TOKEN_SECRET'

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