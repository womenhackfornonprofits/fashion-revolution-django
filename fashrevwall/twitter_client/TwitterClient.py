"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria using Twitter REST API and Tweepy.
"""
import os
import json
import tweepy
from tweepy import OAuthHandler
from .TwitterStreamListener import TwitterStreamListener
from fashrevwall.wall.models import Tweet

class TwitterClient:
    def __init__(self):
        self.api = self._get_twitter_api()

    def _get_twitter_api(self):
        """
        Get access to Twitter API using dev fashrevwall Twitter account.
        """
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']

        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)

        return tweepy.API(self.auth)


    def get_tweets_by_hashtag(self, hashtag, n):
        """
        Receives a string hashtag and returns the list of last n Tweets
        containing it.
        """
        tweets = []
        results = tweepy.Cursor(self.api.search, q=hashtag).items(n)
        for tweet in results:
            tweets.append(tweet)
        return tweets


    def get_images_by_hashtag(self, hashtag, n):
        """
        Receives a string hashtag and returns the list of last n Tweets
        containing it.
        """
        images = []
        tweets = self.get_tweets_by_hashtag(hashtag, n)
        for tweet in tweets:
            user = tweet.author.screen_name.encode('utf-8')
            try:
                image_url = tweet.entities['media'][0]['media_url']
            except KeyError:
                print "No media in tweet with ID: {}".format(tweet.id)
                continue
            t = Tweet.objects.create(user=user, image_url=image_url)
            t.save()


    def stream_by_hashtag(self, hashtag):
        streamingAPI = tweepy.streaming.Stream(self.auth, TwitterStreamListener())
        streamingAPI.filter(track=[hashtag])
