# All requests from external services/website/API here
import requests
from dotenv import load_dotenv
import os
from pprint import pprint


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

    params = {"regions": region, "markets": markets, "apiKey": ODDS_API,
              "oddsFormat": "american", "bookmakers": "fanduel,barstool,williamhill_us,draftkings,betmgm"}
    baseUrl = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds"
    response = requests.get(baseUrl, params=params)
    json = response.json()
    return json


def oddMoneyline():
    print("requested moneyline")
    json = oddSearch(markets="h2h")
    return json


def oddTotals():
    print("requested totals")
    json = oddSearch(markets="totals")
    return json


def oddSpreads():
    print("requested spreads")
    json = oddSearch(markets="spreads")
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
