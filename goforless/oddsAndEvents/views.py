from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.


def index(request):
    return render(request, "sportz/index.html")
