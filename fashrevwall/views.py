from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils import timezone

from fashrevwall.wall.models import Tweet


class TweetListView(ListView):
    """
    The home page view and tweet images view.
    """

    def get_queryset(self):
    	"""Returns latest n tweets in multiples of 3"""
    	tweet_count = Tweet.objects.count()
    	limit = tweet_count - tweet_count % 3
    	return Tweet.objects.order_by('-created_at')[:limit]

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AboutView(TemplateView):
    """
    The About page view.
    """
    template_name = 'about.html'