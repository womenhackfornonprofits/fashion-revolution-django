import pytest
from .TwitterClient import TwitterClient
from .TwitterStreamListener import TwitterStreamListener

def test_api():
    client = TwitterClient()
    api = client.api
    assert api.host == 'api.twitter.com'

def test_twitter_client():
    client = TwitterClient()
    tweets = client.get_tweets_by_hashtag("#helloworld", 10)
    assert len(tweets) >= 0

@pytest.mark.xfail
def test_twitter_client_images():
    client = TwitterClient()
    images = client.get_images_by_hashtag("#helloworld", 10)
