import tweepy, sys
from fashrevwall.wall.models import Tweet

class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        user = status.author.screen_name.encode('utf-8')
        try:
            image_url = status.entities['media'][0]['media_url']
        except KeyError:
            print "No media in tweet with ID: {}".format(tweet.id)
            return
        tweet = Tweet.objects.create(user=user, image_url=image_url)
        tweet.save()


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
