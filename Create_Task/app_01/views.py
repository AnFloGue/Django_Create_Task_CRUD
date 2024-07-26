# In `views.py`
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Review
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
    except ObjectDoesNotExist:
        return HttpResponse('No tasks found', status=404)
    
    if query_data_all.exists():
        context = {
            'tasks': query_data_all,
            "single_task_id": query_data_all[0].id,
            "single_task_title": query_data_all[0].title,
            "single_task_created": query_data_all[0].created,
            "single_task_updated": query_data_all[0].updated,
            "single_task_description": query_data_all[0].description,
        }
    else:
        context = {
            'tasks': query_data_all,
            "single_task_id": None,
            "single_task_title": None,
            "single_task_description": None,
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


def update_task(request, pk):
    task = Task.objects.get(id=pk)
   
    form = TaskForm(instance=task)
    for form in form:
        print(f"Printed Form: {form}")
    
    
    return render(request, 'app_01/update-task.html', {'form': form})


def register(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'app_01/register.html', context)
