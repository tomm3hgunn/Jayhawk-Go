from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .services import *
from oddsAndEvents.models import *

# added for preferences
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UpdatePreferencesForm


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


# https://dev.to/earthcomfy/django-user-profile-3hik
# https://dev.to/earthcomfy/django-update-user-profile-33ho
@login_required
def preferences(request):
    if request.method == 'POST':
        preferences_form = UpdatePreferencesForm(
            request.POST, instance=request.user.preferences)

        if preferences_form.is_valid():
            preferences_form.save()
            messages.success(
                request, 'Your preferences were updated successfully')
            return redirect(to='preferences')
    else:
        preferences_form = UpdatePreferencesForm(
            instance=request.user.preferences)

    return render(request, "sportz/preferences.html", {'preferences_form': preferences_form})


def matchup(request, homeTeam, awayTeam):
    spreadsJson = oddSpreads()
    totalsJson = oddTotals()
    moneylineJson = oddMoneyline()

    # Get data from table
    # x axis is time last updated
    # y axis is points or price
    # line graph
    # line for each book (5)
    labelsSpread = {"FanDuel": [], "BarstoolSportsbook": [],
                    "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    labelsTotal = {"FanDuel": [], "BarstoolSportsbook": [],
                   "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    labelsMoneyline = {"FanDuel": [], "BarstoolSportsbook": [],
                       "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    homePoints = {"FanDuel": [], "BarstoolSportsbook": [],
                  "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    awayPoints = {"FanDuel": [], "BarstoolSportsbook": [],
                  "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    homePrice = {"FanDuel": [], "BarstoolSportsbook": [],
                 "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    awayPrice = {"FanDuel": [], "BarstoolSportsbook": [],
                 "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    overPoints = {"FanDuel": [], "BarstoolSportsbook": [],
                  "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    underPoints = {"FanDuel": [], "BarstoolSportsbook": [],
                   "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    overPrice = {"FanDuel": [], "BarstoolSportsbook": [],
                 "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    underPrice = {"FanDuel": [], "BarstoolSportsbook": [],
                  "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    homePriceMoneyline = {"FanDuel": [], "BarstoolSportsbook": [
    ], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}
    awayPriceMoneyline = {"FanDuel": [], "BarstoolSportsbook": [
    ], "CaesersSportsbook": [], "DraftKings": [], "BetMGM": []}

    # * Spreads
    fanduelData = Spreads.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="FanDuel")
    barstoolData = Spreads.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Barstool Sportsbook")
    williamHillData = Spreads.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Caesars Sportsbook")
    draftKingsData = Spreads.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="DraftKings")
    betMgmData = Spreads.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="BetMGM")
    for entry in fanduelData:
        labelsSpread["FanDuel"].append(entry.lastUpdated)
        homePoints["FanDuel"].append(entry.homePoints)
        awayPoints["FanDuel"].append(entry.awayPoints)
        homePrice["FanDuel"].append(entry.homePrice)
        awayPrice["FanDuel"].append(entry.awayPrice)
    for entry in barstoolData:
        labelsSpread["BarstoolSportsbook"].append(entry.lastUpdated)
        homePoints["BarstoolSportsbook"].append(entry.homePoints)
        awayPoints["BarstoolSportsbook"].append(entry.awayPoints)
        homePrice["BarstoolSportsbook"].append(entry.homePrice)
        awayPrice["BarstoolSportsbook"].append(entry.awayPrice)
    for entry in williamHillData:
        labelsSpread["CaesersSportsbook"].append(entry.lastUpdated)
        homePoints["CaesersSportsbook"].append(entry.homePoints)
        awayPoints["CaesersSportsbook"].append(entry.awayPoints)
        homePrice["CaesersSportsbook"].append(entry.homePrice)
        awayPrice["CaesersSportsbook"].append(entry.awayPrice)
    for entry in draftKingsData:
        labelsSpread["DraftKings"].append(entry.lastUpdated)
        homePoints["DraftKings"].append(entry.homePoints)
        awayPoints["DraftKings"].append(entry.awayPoints)
        homePrice["DraftKings"].append(entry.homePrice)
        awayPrice["DraftKings"].append(entry.awayPrice)
    for entry in betMgmData:
        labelsSpread["BetMGM"].append(entry.lastUpdated)
        homePoints["BetMGM"].append(entry.homePoints)
        awayPoints["BetMGM"].append(entry.awayPoints)
        homePrice["BetMGM"].append(entry.homePrice)
        awayPrice["BetMGM"].append(entry.awayPrice)

    # * Totals
    fanduelData = Totals.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="FanDuel")
    barstoolData = Totals.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Barstool Sportsbook")
    williamHillData = Totals.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Caesars Sportsbook")
    draftKingsData = Totals.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="DraftKings")
    betMgmData = Totals.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="BetMGM")
    for entry in fanduelData:
        labelsTotal["FanDuel"].append(entry.lastUpdated)
        overPoints["FanDuel"].append(entry.overPoints)
        underPoints["FanDuel"].append(entry.underPoints)
        overPrice["FanDuel"].append(entry.overPrice)
        underPrice["FanDuel"].append(entry.underPrice)
    for entry in barstoolData:
        labelsTotal["BarstoolSportsbook"].append(entry.lastUpdated)
        overPoints["BarstoolSportsbook"].append(entry.overPoints)
        underPoints["BarstoolSportsbook"].append(entry.underPoints)
        overPrice["BarstoolSportsbook"].append(entry.overPrice)
        underPrice["BarstoolSportsbook"].append(entry.underPrice)
    for entry in williamHillData:
        labelsTotal["CaesersSportsbook"].append(entry.lastUpdated)
        overPoints["CaesersSportsbook"].append(entry.overPoints)
        underPoints["CaesersSportsbook"].append(entry.underPoints)
        overPrice["CaesersSportsbook"].append(entry.overPrice)
        underPrice["CaesersSportsbook"].append(entry.underPrice)
    for entry in draftKingsData:
        labelsTotal["DraftKings"].append(entry.lastUpdated)
        overPoints["DraftKings"].append(entry.overPoints)
        underPoints["DraftKings"].append(entry.underPoints)
        overPrice["DraftKings"].append(entry.overPrice)
        underPrice["DraftKings"].append(entry.underPrice)
    for entry in betMgmData:
        labelsTotal["BetMGM"].append(entry.lastUpdated)
        overPoints["BetMGM"].append(entry.overPoints)
        underPoints["BetMGM"].append(entry.underPoints)
        overPrice["BetMGM"].append(entry.overPrice)
        underPrice["BetMGM"].append(entry.underPrice)

    # * Moneyline
    fanduelData = Moneyline.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="FanDuel")
    barstoolData = Moneyline.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Barstool Sportsbook")
    williamHillData = Moneyline.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="Caesars Sportsbook")
    draftKingsData = Moneyline.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="DraftKings")
    betMgmData = Moneyline.objects.filter(
        homeTeam=homeTeam, awayTeam=awayTeam, bookmaker="BetMGM")
    for entry in fanduelData:
        labelsMoneyline["FanDuel"].append(entry.lastUpdated)
        homePriceMoneyline["FanDuel"].append(entry.homePrice)
        awayPriceMoneyline["FanDuel"].append(entry.awayPrice)
    for entry in barstoolData:
        labelsMoneyline["BarstoolSportsbook"].append(entry.lastUpdated)
        homePriceMoneyline["BarstoolSportsbook"].append(entry.homePrice)
        awayPriceMoneyline["BarstoolSportsbook"].append(entry.awayPrice)
    for entry in williamHillData:
        labelsMoneyline["CaesersSportsbook"].append(entry.lastUpdated)
        homePriceMoneyline["CaesersSportsbook"].append(entry.homePrice)
        awayPriceMoneyline["CaesersSportsbook"].append(entry.awayPrice)
    for entry in draftKingsData:
        labelsMoneyline["DraftKings"].append(entry.lastUpdated)
        homePriceMoneyline["DraftKings"].append(entry.homePrice)
        awayPriceMoneyline["DraftKings"].append(entry.awayPrice)
    for entry in betMgmData:
        labelsMoneyline["BetMGM"].append(entry.lastUpdated)
        homePriceMoneyline["BetMGM"].append(entry.homePrice)
        awayPriceMoneyline["BetMGM"].append(entry.awayPrice)

    variables = {
        "spreads": spreadsJson,
        "totals": totalsJson,
        "moneyline": moneylineJson,
        "books": books,
        "homeTeam": homeTeam,
        "awayTeam": awayTeam,
        "labelsSpread": labelsSpread,
        "labelsTotal": labelsTotal,
        "homePoints": homePoints,
        "awayPoints": awayPoints,
        "homePrice": homePrice,
        "awayPrice": awayPrice,
        "overPoints": overPoints,
        "underPoints": underPoints,
        "overPrice": overPrice,
        "underPrice": underPrice,
        "homePriceMoneyline": homePriceMoneyline,
        "awayPriceMoneyline": awayPriceMoneyline,
        "labelsMoneyline": labelsMoneyline,
    }
    return render(request, "sportz/matchup.html", variables)
