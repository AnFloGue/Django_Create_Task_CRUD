from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('task-view/', views.task_view, name='task-view'),
    path('create-task/', views.create_task, name='create-task'),
    path('reviews/', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),

]