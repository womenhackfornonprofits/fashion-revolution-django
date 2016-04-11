from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    image_url = models.CharField(max_length=200, unique=True)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.image_url
