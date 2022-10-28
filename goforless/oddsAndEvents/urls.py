from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("news" , views.news, name="news"),
    path("matches" , views.matches, name="matches"),
    path("team", views.team, name="team"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
