from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.


def index(request):
    return render(request, "apiDisplay/index.html")


def yelp(request):
    json = yelpSearch("food", "lenexa")
    variables = {"data": json}
    return render(request, "apiDisplay/yelp.html", variables)