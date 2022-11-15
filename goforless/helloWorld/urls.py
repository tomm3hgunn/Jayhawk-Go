# Hello World App

from django.urls import path

from . import views

urlpatterns = [
    # index defined in views.py
    # <type:column>
    # ex. <str:name>
    path("", views.home, name="home"),  # home page
    path("<int:id>", views.toDo, name="toDo"),  # some list
    path("create/", views.create, name="createList"),
    path("premade/",views.premade, name="premade")
    
]
