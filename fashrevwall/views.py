from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils import timezone


from fashrevwall.wall.models import Tweet

class TweetListView(ListView):
    """
    The home page view and tweet images view.
    """
    #template_name = 'base.html'
    model = Tweet

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AboutView(TemplateView):
    """
    The About page view.
    """
    template_name = 'about.html'