from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return redirect('index')