# from django.urls import path, url, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # http://localhost:8000/team/

]
