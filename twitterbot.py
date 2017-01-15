import tweepy
from textblob import TextBlob


#authorization info
consumer_key = 
consumer_secret = 

access_token = 
access_token_secret =  

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#search public tweets containing this string
# public_tweets = api.search(input('Please enter your search query: '))

#print out the tweets found, and their sentiment analysis
# for tweet in public_tweets:
# 	print(tweet.text.encode("utf-8"))
# 	print('Author: ' + str(tweet.user.screen_name))
# 	print('Created: ' + str(tweet.created_at))
# 	print('Location: ' + str(tweet.place))
# 	print('Favorites: ' + str(tweet.favorite_count))
# 	print('Retweets: ' + str(tweet.retweet_count))
# 	analysis = TextBlob(tweet.text) 
# 	print(analysis.sentiment)
# 	print('\n')

input_file = open('filename.txt', 'r')
output_file = open('output.txt', 'wt')
try:
	for i, line in enumerate(input_file):
		print(len(line))
		if len(line) < 16:
			try:
				user = api.get_user(line)
				#print(line + str(user.created_at))
			except tweepy.TweepError as e:
				if e.api_code == 50:
					print(e.reason)
					output_file.write(str(line))
				pass
finally:
    input_file.close()
print ('{0} line(s) printed'.format(i+1))