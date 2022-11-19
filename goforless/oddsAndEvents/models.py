from django.db import models

# Create your models here.
class Spreads(models.Model):
    """Model of SQL table to hold Spreads data"""

    homeTeam = models.CharField(max_length=200)
    awayTeam = models.CharField(max_length=200)
    bookmaker = models.CharField(max_length=200)
    commenceTime = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    gameID = models.CharField(max_length=200)
    homePoints = models.FloatField()
    homePrice = models.IntegerField()
    awayPoints = models.FloatField()
    awayPrice = models.IntegerField()

    def __str__(self):
        return  f"({self.bookmaker}) " + self.homeTeam + " vs. " + self.awayTeam + " " + self.lastUpdated.strftime("%m/%d/%Y, %H:%M:%S")
