"""
Represents a client that connects to Twitter to retrieve tweets based on a
search criteria using Twitter REST API and Tweepy.
"""

import logging
log = logging.getLogger("fashrevwall")

import os
import tweepy
from tweepy import OAuthHandler
from datetime import date, timedelta
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


    def get_images_by_hashtag(self, hashtag):
        """
        Receives a string hashtag and returns the list of last 24h Tweets
        containing it.
        """
        tweets = []
        # Tweepy only allows for queries with day, but no time, so we can only
        # query since yesteday
        yesterday = date.today() - timedelta(1)
        results = tweepy.Cursor(self.api.search, q=hashtag, since=yesterday)
        log.info("Obtained results, processing...")
        for tweet in results.items():
            if hasattr(tweet, "retweeted_status"):
                log.info("This tweet is a retweet, skipping...")
                continue
            user = tweet.author.screen_name.encode('utf-8')
            created_at = tweet.created_at
            try:
                image_url = tweet.entities['media'][0]['media_url']
                log.info("This tweet contains an image URL: " + image_url)
            except KeyError:
                # Some tweets with given hashtag might not have images in them
                log.info("This tweet doesn't contain an image.")
                continue
            num_tweets = Tweet.objects.count()
            log.info("There are " + str(num_tweets) + " tweets in the DB.")
            if num_tweets >= 10000:
                log.info("Maximum number of tweets stored in the DB reached.")
                oldest_tweet = Tweet.objects.order_by('created_at')[0]
                log.info("Deleting tweet created on " + str(oldest_tweet.created_at))
                oldest_tweet.delete()
            try:
                log.info("Trying to store tweet with text: " + tweet.text + " , and image: " + image_url + " , created at: " + str(tweet.created_at))
                t = Tweet.objects.create(user=user, image_url=image_url, created_at=created_at)
                t.save()
                log.info("New tweet created on date " + str(t.created_at) + " ingested.\n\n")
            except IntegrityError:
                log.info("Skipping tweet ingestion because image url is already in DB.")
                # We only want images to be in the DB once so that field has
                # been set to unique. If we try to insert the same image_url
                # twice, the code breaks with an IntegrityError, so skip those
                continue
