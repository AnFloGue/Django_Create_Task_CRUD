from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
