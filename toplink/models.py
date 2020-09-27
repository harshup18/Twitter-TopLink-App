from django.db import models

class tweetmodel(models.Model): 
    user_name = models.CharField(max_length = 300) 
    tweet_link = models.CharField(max_length = 300)
    tweet_date = models.CharField(max_length = 300)
    tweet_fav_count = models.CharField(max_length = 300)
    tweet_text = models.CharField(max_length = 500)