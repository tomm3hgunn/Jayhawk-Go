from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *

# Create your views here.

books = ["fanduel", "barstoolsportsbook",
         "williamhill(us)", "draftkings", "betmgm"]


def index(request):
    scoresJson = scoresSearch()
    variables = {"scores": scoresJson}
    return render(request, "sportz/index.html", variables)


def news(request):
    return render(request, "sportz/news.html")


def matches(request):
    spreadsJson = oddSpreads()
    totalsJson = oddTotals()
    moneylineJson = oddMoneyline()

    # This is taking too many requests from the API. Make a separate branch for this or do not commit to dev until this is feature complete.
    # sortSpreadsJson = sortSpreads()
    # sortTotalsJson = sortTotals()
    # sortMoneylineJson = sortMoneyline()

    variables = {"spreads": spreadsJson, "totals": totalsJson,
                 "moneyline": moneylineJson, "books": books}
    return render(request, "sportz/matches.html", variables)


def team(request):
    return render(request, "sportz/team.html")


def about(request):
    return render(request, "sportz/about.html")


def contact(request):
    return render(request, "sportz/contact.html")


def preferences(request):
    return render(request, "sportz/preferences.html")


def matchup(request, homeTeam, awayTeam):
    spreadsJson = oddSpreads()
    totalsJson = oddTotals()
    moneylineJson = oddMoneyline()
    variables = {"spreads": spreadsJson, "totals": totalsJson, "moneyline": moneylineJson,
                 "books": books, "homeTeam": homeTeam, "awayTeam": awayTeam}
    return render(request, "sportz/matchup.html", variables)
