# All requests from external services/website/API here
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

def yelpSearch(term, location):
    # Load API token
    load_dotenv()
    YELP_API = os.environ["YELP_API"]

    baseUrl = "https://api.yelp.com/v3/businesses/search"
    params = {"term": term, "location": location}
    headers = {"Authorization": f"Bearer {YELP_API}"}
    response = requests.get(baseUrl, headers=headers, params=params)
    json = response.json()
    return json
