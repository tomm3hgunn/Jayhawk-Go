from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *
from oddsAndEvents.models import *

# Create your views here.

books = ["fanduel", "barstoolsportsbook", "williamhill(us)", "draftkings", "betmgm"]


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

    variables = {"spreads": spreadsJson, "totals": totalsJson, "moneyline": moneylineJson, "books": books}
    return render(request, "sportz/matches.html", variables)


def team(request):
    return render(request, "sportz/team.html")


def about(request):
    return render(request, "sportz/about.html")


def contact(request):
    return render(request, "sportz/contact.html")


def matchup(request, homeTeam, awayTeam):
    spreadsJson = oddSpreads()
    totalsJson = oddTotals()
    moneylineJson = oddMoneyline()

    # Get data from table
    # x axis is time last updated
    # y axis is points or price
    # line graph
    # line for each book (5)
    labels = {"FanDuel": [], "BarstoolSportsbook": [], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    homePoints = {"FanDuel": [], "BarstoolSportsbook": [], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    awayPoints = {"FanDuel": [], "BarstoolSportsbook": [], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    homePrice = {"FanDuel": [], "BarstoolSportsbook": [], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    awayPrice = {"FanDuel": [], "BarstoolSportsbook": [], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}

    # query = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam)
    # order query by sportbooks
    fanduelData = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="FanDuel")
    barstoolData = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Barstool Sportsbook")
    williamHillData = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Caesars Sportsbook")
    draftKingsData = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="DraftKings")
    betMgmData = Spreads.objects.filter(homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="BetMGM")
    for entry in fanduelData:
        labels["FanDuel"].append(entry.lastUpdated)
        homePoints["FanDuel"].append(entry.homePoints)
        awayPoints["FanDuel"].append(entry.awayPoints)
        homePrice["FanDuel"].append(entry.homePrice)
        awayPrice["FanDuel"].append(entry.awayPrice)
    for entry in barstoolData:
        labels["BarstoolSportsbook"].append(entry.lastUpdated)
        homePoints["BarstoolSportsbook"].append(entry.homePoints)
        awayPoints["BarstoolSportsbook"].append(entry.awayPoints)
        homePrice["BarstoolSportsbook"].append(entry.homePrice)
        awayPrice["BarstoolSportsbook"].append(entry.awayPrice)
    for entry in williamHillData:
        labels["CaesersSportsbook"].append(entry.lastUpdated)
        homePoints["CaesersSportsbook"].append(entry.homePoints)
        awayPoints["CaesersSportsbook"].append(entry.awayPoints)
        homePrice["CaesersSportsbook"].append(entry.homePrice)
        awayPrice["CaesersSportsbook"].append(entry.awayPrice)
    for entry in draftKingsData:
        labels["DraftKings"].append(entry.lastUpdated)
        homePoints["DraftKings"].append(entry.homePoints)
        awayPoints["DraftKings"].append(entry.awayPoints)
        homePrice["DraftKings"].append(entry.homePrice)
        awayPrice["DraftKings"].append(entry.awayPrice)
    for entry in betMgmData:
        labels["BetMGM"].append(entry.lastUpdated)
        homePoints["BetMGM"].append(entry.homePoints)
        awayPoints["BetMGM"].append(entry.awayPoints)
        homePrice["BetMGM"].append(entry.homePrice)
        awayPrice["BetMGM"].append(entry.awayPrice)

    variables = {
        "spreads": spreadsJson,
        "totals": totalsJson,
        "moneyline": moneylineJson,
        "books": books,
        "homeTeam": homeTeam,
        "awayTeam": awayTeam,
        "labels": labels,
        "homePoints": homePoints,
        "awayPoints": awayPoints,
        "homePrice": homePrice,
        "awayPrice": awayPrice,
    }
    return render(request, "sportz/matchup.html", variables)
