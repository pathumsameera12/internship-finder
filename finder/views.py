from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_job(request):
    logout(request)
    return redirect('index')

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    user = request.user
    company = Company.objects.get(user=user)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        email = request.POST['email']
        time_date = request.POST['time_date']  # You may need to adjust the date input handling
        skill = request.POST['skill']
        job_type = request.POST['job_type']
        location = request.POST['location']
        category = request.POST['category']


        try:
            job = Job.objects.create(
                company=company,
                title=title,
                description=description,
                email=email,
                time_date=time_date,
                skill=skill,
                job_type=job_type,
                location=location,
                category=category,

            )
            job.save()
            messages.success(request, 'Job added successfully!')
            return redirect('index')  # Redirect to the same page or any other page as needed

        except Exception as e:
            messages.error(request, f'There was an error adding the job: {str(e)}')

    return render(request, 'add_job.html',{'user_type': 'company','profile': company,})
