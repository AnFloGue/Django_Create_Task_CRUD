from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('task/', views.task, name='task'),
    path('create-task/', views.create_task, name='create-task'),
    path('reviews/', views.reviews, name='reviews'),

]