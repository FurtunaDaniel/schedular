from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    output = "<h1>Hi there! This will be the index of team </h1>"
    return HttpResponse(output)

