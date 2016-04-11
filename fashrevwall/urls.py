from django.conf.urls import url
from django.contrib import admin
from fashrevwall.views import TweetListView, AboutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Index - homepage.
    url(r'^$', TweetListView.as_view(), name="index"),
    url(r'^about/', AboutView.as_view(), name="about"),

]
