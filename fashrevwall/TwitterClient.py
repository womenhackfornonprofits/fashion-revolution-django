"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria using Twitter REST API and Tweepy.
"""
import json
import tweepy
from tweepy import OAuthHandler
from TwitterStreamListener import TwitterStreamListener

class TwitterClient:
    def __init__(self):
        self.api = self._get_twitter_api()

    def _get_twitter_api(self):
        """
        Since we are only reading public information from Twitter, we don't need
        access token/secret values.
        """
        with open('secrets.json') as secrets_file:
            secrets = json.load(secrets_file)

        consumer_key = secrets['consumer_key']
        consumer_secret = secrets['consumer_secret']
        access_token = secrets['access_token']
        access_secret = secrets['access_secret']

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
            try:
                image_url = tweet.entities['media'][0]['media_url']
            except KeyError:
                print "No media in tweet with ID: {}".format(tweet.id)
                continue
            print image_url
            images.append(image_url)
        return images

    def stream_by_hashtag(self, hashtag):
        streamingAPI = tweepy.streaming.Stream(self.auth, TwitterStreamListener())
        streamingAPI.filter(track=[hashtag])
