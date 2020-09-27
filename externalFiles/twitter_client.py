import tweepy 
# from externalFiles import twitter_creds
from collections import defaultdict 
from datetime import datetime, timedelta
from urllib.parse import urlparse

api_key = 'BrPmCtci4vKe0xweI4oLLAGsv'
api_secret_key = '11yVywjn8aFShUpfRhZVsCJLFY6aWsBVOm6uJ3dfZmzssLyhIN'
access_token = '2559429854-bYFGSiKu2qHta1GFfbzNGkDj3rEWyP2xA9Cdr3Y'
access_token_secret = 'mtUR5hvwp7Im3JVwJwXMCGrnXXjrq1WvsYNA1oabjere7'

# #Twitter API credentials
# api_key = twitter_creds.API_KEY
# api_secret_key = twitter_creds.API_SECRET_KEY
# access_token = twitter_creds.ACCESS_TOKEN
# access_token_secret = twitter_creds.ACCESS_TOKEN_SECRET


def extract_domain(url):
    uri = urlparse(url)
    domain_name = f"{uri.netloc}"
    return domain_name


def has_url(tweet):
	# print(tweet['urls'])
	tweetList = tweet['urls']
	if (len(tweetList) != 0):
		return 1, tweetList[0]['expanded_url']
	else:
		return 0, " "

def get_followers(api, screen_name):
	  
	c = tweepy.Cursor(api.followers, screen_name) 
	  
	count = 0

	for follower in c.items(): 
	    count += 1

	friends = []

	# printing the latest 20 followers of the user 
	# for follower in tweepy.Cursor(api.followers, screen_name).items(count):  
	#     friends.append(follower.screen_name)

	print("--Fetching friends---")

	# Printing friends of user 
	for friend in tweepy.Cursor(api.friends, screen_name).items():
		friends.append(friend.screen_name)

	return friends


def get_url_tweets(api, followers):

	print("--Fetching friends tweets---")
	# Setting date range
	start_date = datetime.now()-timedelta(7)
	end_date = datetime.now()

	tweetWithUrls = []
	urlList = []
	friendsTweetCount = defaultdict(int) 
	urlDomains = defaultdict(int) 
	count = 0 


	for user in followers:
		print(user)
		tweetArray = api.user_timeline(user)
		for tweet in tweetArray:
			if tweet.created_at < end_date and tweet.created_at > start_date:
				count+=1
				flag, url = has_url(tweet.entities)
				if (flag):
					urlDomains[extract_domain(url)] += 1
					urlList.append(url)
					tweetWithUrls.append(tweet._json)
					friendsTweetCount[user] += 1
		
		# if tweets are more than 20 fetch them too

		# lastId = tweetArray[-1].id;

		# while (tweetArray[-1].created_at > start_date):
			
		# 	extraTweetArray = api.user_timeline(user,max_id = tweetArray[-1].id)
			
		# 	if (lastId == extraTweetArray[-1].id):
		# 		break

		# 	for tweet in extraTweetArray:
		# 		if tweet.created_at < end_date and tweet.created_at > start_date:
		# 			count+=1
		# 			if (has_url(tweet.entities)):
		# 				tweetWithUrls.append(tweet)
		# 				friendsTweetCount[user] = friendsTweetCount.get(user,0) + 1


	print(count)					
	print("------")

	return tweetWithUrls, urlDomains, friendsTweetCount



# if __name__ == '__main__':

def get_tweets_data(screen_name):

	# authorization of api key and api secret key 
	auth = tweepy.OAuthHandler(api_key, api_secret_key) 
	  
	# set access to user's access token and access secret  
	auth.set_access_token(access_token, access_token_secret) 
	  
	# calling the api  
	api = tweepy.API(auth, wait_on_rate_limit=True)
	
	# Get followers function call
	followers = get_followers(api, screen_name)

	mostSharedDomain = ""
	friendWithMaxUrlTweet = ""
	print("User Friends Fetched")
	print(followers)


	# Fetch friends tweets for last 7 days
	tweetsWithUrls, urlDomains, friendsTweetCount = get_url_tweets(api, followers)
	if(len(urlDomains) != 0):
		mostSharedDomain = max(urlDomains, key=urlDomains.get)
	if (len(friendsTweetCount)):	
		friendWithMaxUrlTweet = max(friendsTweetCount, key=friendsTweetCount.get) 
		leastActiveFriend = min(friendsTweetCount, key=friendsTweetCount.get)
	
	tweetAnalysis = {}
	tweetAnalysis['mostSharedDomain'] = mostSharedDomain
	tweetAnalysis['mostSharedDomainCount'] = urlDomains[mostSharedDomain]
	tweetAnalysis['friendWithMaxUrlTweet'] = friendWithMaxUrlTweet
	tweetAnalysis['friendWithMaxUrlTweetCount'] = friendsTweetCount[friendWithMaxUrlTweet]
	tweetAnalysis['leastActiveFriend'] = leastActiveFriend
	tweetAnalysis['leastActiveFriendCount'] = friendsTweetCount[leastActiveFriend]




	tweetsWithUrls.append(tweetAnalysis)

	print("-----DONE-----")
	return tweetsWithUrls