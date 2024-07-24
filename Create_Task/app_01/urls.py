from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('member/', views.register, name='member'),
    path('cars/', views.cars, name='cars'),
    path('register/', views.register, name='register'),
    path('task/', views.task, name='task'),
    path('reviews/', views.reviews, name='reviews'),
    path('create-task/', views.create_task, name='create-task'),
]