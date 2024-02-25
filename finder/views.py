from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        try:
            company = Company.objects.get(user=request.user)
            context = {'user_type': 'company', 'profile': company}
        except Company.DoesNotExist:

            student = Company.objects.get(user=request.user)
            context = {'user_type': 'student', 'profile': student}

        return render(request, 'index.html', context)

    return render(request, 'index.html')
def user_logout(request):
    logout(request)
    return redirect('index')

def company_registration(request):
    if request.method=="POST":
        company_name = request.POST['company_name']
        company_address = request.POST['address']
        company_bio = request.POST['company_bio']
        website = request.POST['company_web']
        contact_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']

        try:
            if User.objects.filter(username=email).exists():
                raise IntegrityError('Username already exists.')

            user = User.objects.create_user(email=email, username=email, password=password)
            company = Company.objects.create(user=user, company_name=company_name, company_address=company_address, company_bio=company_bio, website=website, contact_number=contact_number, email= email, type="company")

            user.save()
            company.save()
            messages.success(request, 'Account created successful!')
            return redirect('company_login')

        except IntegrityError as e:
            messages.success(request, f'Username already exists. Please choose a different username.')
            return render(request, 'company_registration.html',{'company_name': company_name, 'company_address': company_address, 'company_bio': company_bio, 'website': website, 'contact_number': contact_number, 'email': email, })

        except Exception as e:
            messages.success(request, 'There was an error in signup. {str(e)}')
            return render(request, 'company_registration.html')
    else:
        return render(request, 'company_registration.html')


def company_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            user1 = Company.objects.get(user=user)
            if user1.type == "company":
                login(request, user)

                return redirect('index')
        else:
            messages.success(request, 'Invalid username or password')
            return render(request, 'company_login.html')
    else:
        return render(request, 'company_login.html')
