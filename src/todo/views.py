from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_add(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form':form,
    }
    return render(request, "todo/todo_add.html", context)

