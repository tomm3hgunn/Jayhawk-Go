from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.


def index(request):
    json = oddSpreads()
    variables = {"data": json}
    return render(request, "sportz/index.html", variables)

def news(request):
    return render(request, "sportz/news.html")

def matches(request):
    return render(request, "sportz/matches.html")

def team(request):
    return render(request, "sportz/team.html")

def about(request):
    return render(request, "sportz/about.html")

def contact(request):
    return render(request, "sportz/contact.html")