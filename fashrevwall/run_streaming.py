from TwitterClient import TwitterClient

def test_twitter_streaming():
    client = TwitterClient()
    client.stream_by_hashtag("#hello")

if __name__ == "__main__":
    test_twitter_streaming()
