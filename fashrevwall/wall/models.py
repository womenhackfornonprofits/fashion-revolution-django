from datetime import date
from django.db import models


class Tweet(models.Model):
    image_url = models.CharField(max_length=200, unique=True)
    user = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.image_url
