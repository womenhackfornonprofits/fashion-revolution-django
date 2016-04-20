from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    image_url = models.CharField(max_length=200, unique=True)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    
    class Meta:
		ordering = ["-id"]

    def __unicode__(self):
        return self.image_url
