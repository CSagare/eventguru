from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.utils import timezone
from datetime import date

def login_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'lanner':
                return redirect('dashboard')  # Redirect to event list if user is an organizer
            elif user.user_type == 'normal':
                
                    return redirect('index')  # Redirect to save preferences if no preferences exist
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Check user type and redirect accordingly
            if user.user_type == 'lanner':
                login(request, user)
                return redirect('login')
            elif user.user_type == 'normal':
                    login(request, user)
                    return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    # messages.success(request, ('You have been logged out'))

    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')
