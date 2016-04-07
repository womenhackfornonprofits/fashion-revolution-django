from django.conf.urls import url
from django.contrib import admin
from fashrevwall.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Index - homepage.
    url(r'^$', IndexView.as_view(), name="index"),

]
