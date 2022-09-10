from django.contrib import admin

# import models
from .models import *

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
