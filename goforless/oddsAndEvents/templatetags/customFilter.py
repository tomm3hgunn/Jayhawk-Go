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
