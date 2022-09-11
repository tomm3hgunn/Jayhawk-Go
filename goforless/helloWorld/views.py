from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Home page
def home(request):
    return render(request, "helloWorld/home.html")

def toDo(request, id):
    # Display list name
    list = ToDoList.objects.get(id=id)
    name = list.name
    # user filter for multiple objects
    items = list.item_set.filter(todoList_id=list.id)

    # create dictionary before passing
    variables = {"name": name, "items": items}

    # pass actual HTML files through
    # last parameter is a dictionary that corresponds to the variables we will
    # use in the HTML file
    return render(request, "helloWorld/todo.html", variables)
