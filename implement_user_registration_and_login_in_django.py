# First, install Django using pip
# >> pip install django

# Create a new Django project
# >> django-admin startproject myproject

# Create a new Django app
# >> python manage.py startapp myapp

# Define User model in models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

# Update settings.py to use CustomUser
AUTH_USER_MODEL = 'myapp.CustomUser'

# Run migrations
# >> python manage.py makemigrations
# >> python manage.py migrate

# Create registration and login views in views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        # Process registration form data
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# Define URLs in urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]

# Create register.html and login.html templates

# Add URLs to main project's urls.py
from django.urls import include

urlpatterns = [
    path('myapp/', include('myapp.urls')),
]

# Now users can register and login in the Django app
# Please Like and Subscribe