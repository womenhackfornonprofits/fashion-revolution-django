from django.core.management import BaseCommand
from fashrevwall.twitter_client.TwitterClient import TwitterClient

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):

        # Show this when the user types help
        help = "Invoke the Twitter client and get some tweets."

        # A command must define handle()
        def handle(self, *args, **options):
            client = TwitterClient()
            client.get_images_by_hashtag("#hellofashionrevwall", 200)
