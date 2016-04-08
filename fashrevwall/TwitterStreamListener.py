import tweepy, sys

class TwitterStreamListener(tweepy.StreamListener):

 def on_status(self, status):
    print status.author.screen_name.encode('utf-8'), status.created_at, status.text.encode('utf-8')
    # TODO: Maybe write these to the postgres DB from here?

 def on_error(self, status_code):
    print >> sys.stderr, 'Encountered error with status code:', status_code
    return True # Don't kill the stream

 def on_timeout(self):
    print >> sys.stderr, 'Timeout...'
    return True # Don't kill the stream
