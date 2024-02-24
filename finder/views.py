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
            company = Company.objects.create(company_name=company_name, company_address=company_address, company_bio=company_bio, website=website, contact_number=contact_number, email= email)

            user.save()
            company.save()
            messages.success(request, 'Account created successful!')
            return render(request, "company_login.html")

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
            login(request, user)
            company = Company.objects.get(email=email)

            #return redirect('index', company_name=user.id)
            return render(request, 'index.html', {'company_id': user.id, "company_name": company.company_name})

        else:
            messages.success(request, 'Invalid username or password')
            return render(request, 'company_login.html')
    else:
        return render(request, 'company_login.html')
