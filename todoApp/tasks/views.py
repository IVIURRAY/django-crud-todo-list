from django.shortcuts import render, HttpResponse, redirect

from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': Task.objects.all(),
        'form': form
    }

    return render(request, 'index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'update.html', context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == "POST":
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', context)
