from django.db import models

# Create your models here.
# * Model information in an organized way to store
# Exactly like creating table in SQL, except with Django
# class Name(models.Model):


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    # String overload for printing
    def __str__(self):
        return self.name


class Item(models.Model):
    # Create a ToDO object (don't know it's contents)
    # Delete item when ToDo is deleted
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
