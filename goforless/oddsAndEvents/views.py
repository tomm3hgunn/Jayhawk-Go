from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.

books = ["fanduel", "barstoolsportsbook", "williamhill(us)", "draftkings", "betmgm"]

def index(request):
    return render(request, "sportz/index.html")


def news(request):
    return render(request, "sportz/news.html")


def matches(request):
    spreadsJson = oddSpreads()
    totalsJson = oddTotals()
    moneylineJson = oddMoneyline()
    variables = {"spreads": spreadsJson, "totals": totalsJson, "moneyline": moneylineJson, "books": books}
    return render(request, "sportz/matches.html", variables)

#copy of spreadsJson
cpySpreads = spreadsJson

def team(request):
    return render(request, "sportz/team.html")


def about(request):
    return render(request, "sportz/about.html")


def contact(request):
    return render(request, "sportz/contact.html")
