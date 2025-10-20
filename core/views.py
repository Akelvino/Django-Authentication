from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

from .forms import RegisterForm

# Create your views here.
@login_required
def Home(request):
    return render(request, 'core/index.html')

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Accout created successfully.Login now")
            return redirect('login')
    else:
        form = RegisterForm()
        
    return render(request, 'core/register.html',{'form':form})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have loged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
            
    return render(request, 'core/login.html')

def LogoutView(request):
    logout(request)
    
    return redirect('login')