"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria using Twitter REST API and Tweepy.
"""
import os
import tweepy
from tweepy import OAuthHandler
from datetime import date, datetime, timedelta
from .TwitterStreamListener import TwitterStreamListener
from fashrevwall.wall.models import Tweet
from django.db import IntegrityError

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


    def get_images_by_hashtag(self, hashtag, n):
        """
        Receives a string hashtag and returns the list of last n Tweets
        containing it.
        """
        tweets = []
        # Work out date of latest tweet in DB, and query since that date only
        since = self.get_latest_tweet_date()
        print "since: " + str(since)
        if since:
            previous_query = date.today() - timedelta(1)
            print previous_query
            results = tweepy.Cursor(self.api.search, q=hashtag, since=previous_query)
        else:
            yesterday = date.today() - timedelta(1)
            print yesterday
            results = tweepy.Cursor(self.api.search, q=hashtag, since=yesterday)
        print "Obtained results, processing..."
        print results.items()
        for tweet in results.items():
            print tweet.author.screen_name.encode('utf-8'), tweet.created_at, tweet.text.encode('utf-8')
            user = tweet.author.screen_name.encode('utf-8')
            created_at = tweet.created_at
            try:
                image_url = tweet.entities['media'][0]['media_url']
                print "This tweet contains an image URL: " + image_url
            except KeyError:
                # Some tweets with given hashtag might not have images in them
                print "This tweet doesn't contain an image."
                continue
            print "Checking how many tweets are in the DB..."
            num_tweets = len(Tweet.objects.all())
            print "There are " + str(num_tweets)
            if num_tweets == 10000:
                print "Maximum number of tweets stored in the DB reached."
                oldest_tweet = Tweet.objects.order_by('created_at')[0]
                print "Deleting tweet created on " + str(oldest_tweet.created_at)
                oldest_tweet.delete()
            try:
                t = Tweet.objects.create(user=user, image_url=image_url, created_at=created_at)
                t.save()
                print "New tweet created on date " + str(t.created_at) + " ingested.\n\n"
            except IntegrityError:
                # We only want images to be in the DB once so that field has
                # been set to unique. If we try to insert the same image_url
                # twice, the code breaks with an IntegrityError, so skip those
                continue

    def get_latest_tweet_date(self):
        """
        Gets date of latest tweeted tweet.
        """
        try:
            latest_tweet = Tweet.objects.order_by('created_at').reverse()[0]
        except IndexError:
            return None

        return latest_tweet.created_at


    def stream_by_hashtag(self, hashtag):
        streamingAPI = tweepy.streaming.Stream(self.auth, TwitterStreamListener())
        streamingAPI.filter(track=[hashtag])
