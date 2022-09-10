# Hello World App

from django.urls import path

from . import views

urlpatterns = [
    # index defined in views.py
    # <type:column>
    # ex. <int:id>
    path("<str:name>", views.index, name="index"),
    # path("depth1/", views.depthOne, name="depth one"),
]
