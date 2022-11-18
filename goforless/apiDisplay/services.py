# All requests from external services/website/API here
import requests
from dotenv import load_dotenv
import os
from pprint import pprint


def oddSearch(region="us", markets="spreads"):
    load_dotenv()
    ODDS_API = os.environ["ODDS_API"]

    params = {"regions": region, "markets": markets, "apiKey": ODDS_API, "oddsFormat": "american"}
    baseUrl = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds"
    response = requests.get(baseUrl, params=params)
    json = response.json()
    pprint(json[0])
    return json

def oddMoneyline():
    json = oddSearch(markets="h2h")
    return json

def oddTotals():
    json = oddSearch(markets="totals")
    return json

def oddSpreads():
    json = oddSearch(markets="spreads")
    return json