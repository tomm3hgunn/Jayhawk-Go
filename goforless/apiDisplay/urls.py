from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"), path("yelp/",views.yelp,name="yelp")]
