from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import (Task, Review)
from .forms import TaskForm
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    all_task = Task.objects.all()
    all_reviews = Review.objects.all()
    
    context = {
        'all_task': all_task,
        'all_reviews': all_reviews,
    }
    return render(request, 'app_01/index.html', context)


def task_view(request):
    try:
        query_data_all = Task.objects.all()
        # Your code to handle the found object
    except ObjectDoesNotExist:
        # Fallback behavior: redirect or render a custom error page
        return HttpResponse('Task not found', status=404)
    all_tasks = Task.objects.all()
    context = {
        'tasks': all_tasks,
        'single_task': query_data_all
    }
    return render(request, 'app_01/task-view.html', context)


def reviews(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'app_01/reviews.html', context)


def create_task(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-view')
    
    context = {
        "TaskForm": form
    }
    
    return render(request, 'app_01/create-task.html', context)


def register(request):
    return render(request, 'app_01/register.html')
