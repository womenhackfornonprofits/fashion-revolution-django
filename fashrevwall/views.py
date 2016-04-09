from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    The home page view.
    """
    template_name = 'base.html'

class AboutView(TemplateView):
    """
    The About page view.
    """
    template_name = 'about.html'