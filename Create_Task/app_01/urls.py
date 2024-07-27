from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('task-view/', views.task_view, name='task-view'),
    path('create-task/', views.create_task, name='create-task'),
    path('reviews/', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),
    path('update-task/<str:pk>/', views.update_task, name='update-task'),
    path('delete-task/<str:pk>/', views.delete_task, name='delete-task'),
    path('my-login/', views.my_login, name='my-login'),
    path('my-logout/', views.user_logout, name='my-logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]