from django.shortcuts import render
from django.http import HttpResponse
from externalFiles import twitter_client
import json as simplejson
from django.views.decorators.csrf import csrf_exempt


def home(request):
	return render(request,'index.html')

@csrf_exempt
def getTweets(request):

	print(request)
	tweetsJson = simplejson.dumps({"Error" : "Sorry we ran into some error!"})

	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = simplejson.loads(body_unicode)
		username = body['username']
		print(username)
		tweets = twitter_client.get_tweets_data(username)		
		# Saving tweets into database
		for tweet in tweets:
			tweet_link = str("https://twitter.com/"+str(tweet.user.screen_name)+"/status/"+str(tweet.id))
			db_object = tweetmodel(user_name = tweet.user.screen_name, tweet_text = status.text, tweet_link = tweet_link, tweet_date = tweet.created_at, tweet_fav_count = tweet.favorite_count)
			db_object.save()
			

		if (len(tweets) != 0):
			tweetsJson = simplejson.dumps({"data" : tweets})
		else:
			tweetsJson = simplejson.dumps({"data" : "No Tweets with link found!"})
	return HttpResponse(tweetsJson);
