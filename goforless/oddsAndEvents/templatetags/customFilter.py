from django import template
import datetime
import pytz

register = template.Library()


@register.filter(name="formatDate")
def formatDate(value):
    """Formats date format of Y-m-dTH:M:SZ to Month, Day H:M AM/PM using Central Standard Time"""
    # convert to datetime object
    date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")

    # convert to Central Standard Time
    date = date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("US/Central"))

    # format date
    date = date.strftime("%B %d %I:%M %p")

    return date


@register.filter(name="hillToCaesars")
def hillToCaesers(value):
    """Converts William Hill (US) to Caesars Sportsbook"""

    bookmaker = value

    if bookmaker == "William Hill (US)":
        bookmaker = "Caesars Sportsbook"

    return bookmaker


@register.filter(name="getHomeTeam")
def getHomeTeam(outcomeList, homeTeam):
    # input is a dictionary outcomes with two items
    for outcome in outcomeList:
        if outcome["name"] == homeTeam:
            return outcome


@register.filter(name="getAwayTeam")
def getAwayTeam(outcomeList, awayTeam):
    # input is a dictionary outcomes with two items
    for outcome in outcomeList:
        if outcome["name"] == awayTeam:
            return outcome

@register.filter(name="toFloat")
def toFloat(value):
    """Converts string to float"""
    return float(value)