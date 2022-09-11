from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# premade
def premade(request):
    return render(request,"web/index.html")

# Home page
def home(request):
    return render(request, "helloWorld/home.html")


def toDo(request, id):
    # Display list name
    list = ToDoList.objects.get(id=id)
    name = list.name
    # user filter for multiple objects
    # items = list.item_set.filter(todoList_id=list.id)
    items = list.item_set.all()

    # create dictionary before passing
    variables = {"name": name, "items": items}

    # POST new item in list
    print(request.POST)
    if request.method == "POST":
        # which button was pressed in parameter
        if request.POST.get("save"):  # if save button was pressed
            # iterate through items to check whether checkbox is complete
            for item in items:
                print(request.POST.get("checkbox" + str(item.id)))
                if request.POST.get("checkbox" + str(item.id)) == "click":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem"):
            text = request.POST.get("field")
            # Make own text validity check
            if len(text) > 2:
                list.item_set.create(text=text, complete=False)
            else:
                print("invalid")
    # pass actual HTML files through
    # last parameter is a dictionary that corresponds to the variables we will
    # use in the HTML file
    return render(request, "helloWorld/todo.html", variables)


def create(request):
    # Check if request is a POST
    # Needing to modify the database
    if request.method == "POST":
        form = CreateList(request.POST)  # data from form in a dictionary
        # Clean data
        if form.is_valid():
            name = form.cleaned_data["name"]
            newList = ToDoList(name=name)
            newList.save()  # save to database

        # Redirect to some page after submitting
        return HttpResponseRedirect(f"/{newList.id}")
    else:
        form = CreateList()
    variables = {"form": form}
    return render(request, "helloWorld/create.html", variables)
