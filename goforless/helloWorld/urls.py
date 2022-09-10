# Hello World App

from django.urls import path

from . import views

urlpatterns = [
    # index defined in views.py
    # <type:column>
    # ex. <str:name>
    
    path("<int:id>", views.index, name="index"),
    # path("depth1/", views.depthOne, name="depth one"),
]
