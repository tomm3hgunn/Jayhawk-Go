from django.http import HttpResponse
from .models import *

# ID parameter is dynamic
def index(request, id):
    # Display list name
    list = ToDoList.objects.get(id=id)
    name = list.name
    # user filter for multiple objects
    item = list.item_set.filter(todoList_id=list.id)
    # HTML string as parameter
    return HttpResponse(f"<h1>{name}<h1><br></br><p>{item[0]}<p>")


def depthOne(request):
    return HttpResponse("<h2>You are now at depth 1 of Hello World<h2>")