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
    task_db_obj = get_object_or_404(Task, id=pk)
    form_pre_filled_obj = TaskForm(request.POST or None, instance=task_db_obj)
    
    if request.method == 'POST' and form_pre_filled_obj.is_valid():
        form_pre_filled_obj.save()
        return redirect('task-view')
    
    context = {
        "UpdateTaskForm": form_pre_filled_obj
    }
    
    return render(request, 'app_01/update-task.html', context)


def delete_task(request, pk):
    task_db_obj = get_object_or_404(Task, id=pk)
    
    if request.method == 'POST':
        task_db_obj.delete()
        return redirect('task-view')
    
    context = {
        "DeleteTaskForm": TaskForm(instance=task_db_obj),
        "task": task_db_obj
    }
    
    return render(request, 'app_01/delete-task.html', context)


def register(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'app_01/register.html', context)
