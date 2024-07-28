from django.shortcuts import render
from .models import Todo

def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, "tasks/todo_list.html", {"tasks": tasks})
