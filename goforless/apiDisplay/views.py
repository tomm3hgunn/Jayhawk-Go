from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.


def index(request):
    return render(request, "apiDisplay/index.html")


def spreads(request):
    json = oddSpreads()
    variables = {"data": json}
    return render(request, "apiDisplay/spreads.html", variables)


def totals(request):
    json = oddTotals()
    variables = {"data": json}
    return render(request, "apiDisplay/totals.html", variables)

def moneyline(request):
    json = oddMoneyline()
    variables = {"data": json}
    return render(request, "apiDisplay/moneyline.html", variables)
