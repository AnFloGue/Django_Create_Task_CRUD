from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import (Member, CarModel, Task, Review)
from .forms import TaskForm
from django.core.exceptions import ObjectDoesNotExist


def homepage(request):
    carmodel = CarModel.objects.all()
    members = Member.objects.all()
    
    context = {
        'carmodel': carmodel,
        'members': members,
    }
    return render(request, 'app_01/index.html', context)


def register(request):
    members = Member.objects.all()
    cars = CarModel.objects.all()
    
    context = {
        'members': members,
        'cars': cars,
    }
    return render(request, 'app_01/register.html', context)


def cars(request):
    autos_list = [
        {
            'model': 'Porch',
            'color': 'blue',
            'year': 1902,
        },
        {
            'model': 'Ferrari',
            'color': 'red',
            'year': 2020,
        },
        {
            'model': 'Tesla',
            'color': 'white',
            'year': 2020,
        },
        {
            'model': 'BMW',
            'color': 'black',
            'year': 2019,
        },
        {
            'model': 'Audi',
            'color': 'silver',
            'year': 2018,
        }
    ]
    context = {'autos': autos_list}
    print(type(context))
    for key, value in context.items():
        print(f"key {key} values {value}")
    return render(request, 'app_01/cars.html', context)


def task(request):
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
    return render(request, 'app_01/task.html', context)


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
            return redirect('task')
    
    context = {
        "TaskForm": form
    }
    
    return render(request, 'app_01/create-task.html', context)
