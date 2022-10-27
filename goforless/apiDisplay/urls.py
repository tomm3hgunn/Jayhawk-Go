from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("spreads/", views.spreads, name="spreads"),
    path("totals/", views.totals, name="totals"),
    path("outrights/", views.outrights, name="outrights"),
    path("moneyline/", views.moneyline, name="h2h"),
]
