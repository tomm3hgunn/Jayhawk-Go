# All requests from external services/website/API here
import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from oddsAndEvents.models import *
import datetime
import pytz

def scoresSearch(daysFrom="3"):
    load_dotenv()
    ODDS_API = os.environ["ODDS_API"]

    params = {"daysFrom": daysFrom, "apiKey": ODDS_API}
    baseUrl = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/scores"
    response = requests.get(baseUrl, params=params)
    json = response.json()
    return json


def oddSearch(region="us", markets="spreads"):
    load_dotenv()
    ODDS_API = os.environ["ODDS_API"]

    params = {
        "regions": region,
        "markets": markets,
        "apiKey": ODDS_API,
        "oddsFormat": "american",
        "bookmakers": "fanduel,barstool,williamhill_us,draftkings,betmgm",
    }
    baseUrl = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds"
    response = requests.get(baseUrl, params=params)
    remainingReq = response.headers["X-Requests-Remaining"]
    print(f"## Remaining Odds API requests: {remainingReq} ##")
    json = response.json()
    return json


def oddMoneyline():
    print("requested moneyline")
    json = oddSearch(markets="h2h")

    for game in json:
        awayTeam = game["away_team"]
        homeTeam = game["home_team"]
        commenceTime = game["commence_time"]
        gameID = game["id"]
        for bookmaker in game["bookmakers"]:
            book = bookmaker["title"]
            if book == "William Hill (US)":
                book = "Caesars Sportsbook"
            lastUpdate = bookmaker["last_update"]
            if awayTeam == bookmaker["markets"][0]["outcomes"][0]:
                awayPrice = bookmaker["markets"][0]["outcomes"][0]["price"]
                homePrice = bookmaker["markets"][0]["outcomes"][1]["price"]
            else:
                awayPrice = bookmaker["markets"][0]["outcomes"][1]["price"]
                homePrice = bookmaker["markets"][0]["outcomes"][0]["price"]
            cursor = Moneyline(
                homeTeam=homeTeam,
                awayTeam=awayTeam,
                bookmaker=book,
                commenceTime=commenceTime,
                lastUpdated=lastUpdate,
                gameID=gameID,
                homePrice=homePrice,
                awayPrice=awayPrice,
            )
            try:
                cursor.save()
            except:
                pass
    print("Moneyline Rows #: " + str(Moneyline.objects.count()))
    return json


def oddTotals():
    print("requested totals")
    json = oddSearch(markets="totals")
    # get all totals rows from db
    for game in json:
        # totals have over points, under points, over price, under price
        awayTeam = game["away_team"]
        homeTeam = game["home_team"]
        commenceTime = game["commence_time"]
        gameID = game["id"]
        for bookmaker in game["bookmakers"]:
            book = bookmaker["title"]
            if book == "William Hill (US)":
                book = "Caesars Sportsbook"
            lastUpdate = bookmaker["last_update"]
            if awayTeam == bookmaker["markets"][0]["outcomes"][0]:
                overPoints = bookmaker["markets"][0]["outcomes"][0]["point"]
                overPrice = bookmaker["markets"][0]["outcomes"][0]["price"]
                underPoints = bookmaker["markets"][0]["outcomes"][1]["point"]
                underPrice = bookmaker["markets"][0]["outcomes"][1]["price"]
            else:
                overPoints = bookmaker["markets"][0]["outcomes"][1]["point"]
                overPrice = bookmaker["markets"][0]["outcomes"][1]["price"]
                underPoints = bookmaker["markets"][0]["outcomes"][0]["point"]
                underPrice = bookmaker["markets"][0]["outcomes"][0]["price"]
            cursor = Totals(
                homeTeam=homeTeam,
                awayTeam=awayTeam,
                bookmaker=book,
                commenceTime=commenceTime,
                lastUpdated=lastUpdate,
                gameID=gameID,
                overPoints=overPoints,
                overPrice=overPrice,
                underPoints=underPoints,
                underPrice=underPrice,
            )
            try:
                cursor.save()
            except:
                pass

    print("Totals Rows #: " + str(Totals.objects.count()))
    return json


def oddSpreads():
    print("requested spreads")
    json = oddSearch(markets="spreads")

    # Every request, add data to database
    for game in json:
        awayTeam = game["away_team"]
        homeTeam = game["home_team"]
        commenceTime = game["commence_time"]
        gameID = game["id"]
        for bookmaker in game["bookmakers"]:
            book = bookmaker["title"]
            if book == "William Hill (US)":
                book = "Caesars Sportsbook"
            lastUpdate = bookmaker["last_update"]
            if awayTeam == bookmaker["markets"][0]["outcomes"][0]:
                awayPoints = bookmaker["markets"][0]["outcomes"][0]["point"]
                awayPrice = bookmaker["markets"][0]["outcomes"][0]["price"]
                homePoints = bookmaker["markets"][0]["outcomes"][1]["point"]
                homePrice = bookmaker["markets"][0]["outcomes"][1]["price"]
            else:
                awayPoints = bookmaker["markets"][0]["outcomes"][1]["point"]
                awayPrice = bookmaker["markets"][0]["outcomes"][1]["price"]
                homePoints = bookmaker["markets"][0]["outcomes"][0]["point"]
                homePrice = bookmaker["markets"][0]["outcomes"][0]["price"]
            cursor = Spreads(
                homeTeam=homeTeam,
                awayTeam=awayTeam,
                bookmaker=book,
                commenceTime=commenceTime,
                lastUpdated=lastUpdate,
                gameID=gameID,
                homePoints=homePoints,
                homePrice=homePrice,
                awayPoints=awayPoints,
                awayPrice=awayPrice,
            )
            try:
                cursor.save()
            except:
                pass

        # print number of rows in database
    print("Spread Rows #: " + str(Spreads.objects.count()))
        
    # cursor = Spreads(homeTeam="test", awayTeam="test", bookmaker="test", commenceTime="test", lastUpdated="test", gameID="test", homePoints="test", homePrice="test", awayPoints="test", awayPrice="test")
    # cursor.save()
    return json


# not sure yet where these func needs to be this can be temp
# lowest to highest might be they best display
# "Best" may be difficult because its gambling (maybe we could impliment "our pick")
# lowest to highest might be they best display


def sortSpreads():
    print("spread form lowest to highest")
    json = oddSearch(markets="spreads")
    # json.sort()
    return json


def sortTotals():
    print("Totals from lowest to highest")
    json = oddSearch(markets="totals")
    # json.sort()
    return json


def sortMoneyline():
    print("moneyline from lowest to highest")
    json = oddSearch(markets="h2h")
    # json.sort()
    return json
