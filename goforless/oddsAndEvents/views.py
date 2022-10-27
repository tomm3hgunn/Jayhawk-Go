from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.


def index(request):
    json = oddSpreads()
    variables = {"data": json}
    return render(request, "sportz/index.html", variables)
