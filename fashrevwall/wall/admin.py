from django.contrib import admin
from fashrevwall.wall.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    search_fields = ("user", "image_url") 
    list_display = ("id", "user", "image_url")
    ordering = ('-id',)


admin.site.register(Tweet, TweetAdmin)
