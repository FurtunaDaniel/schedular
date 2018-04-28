# from django.urls import path, url, include
from django.views.generic.base import RedirectView
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.teamDetails, name="teamDetails"),
    # http://localhost:8000/team/
]
