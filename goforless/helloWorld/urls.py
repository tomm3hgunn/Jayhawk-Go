# Hello World App

from django.urls import path

from . import views

urlpatterns = [
    # index defined in views.py
    # <type:column>
    # ex. <str:name>
    path("", views.home, name="home"),
    path("<int:id>", views.toDo, name="ToDo")
    # path("depth1/", views.depthOne, name="depth one"),
]
