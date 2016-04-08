from django.db import models

class Tweet(models.Model):
    text = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
