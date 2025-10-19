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
    return render(request, 'core/login.html')