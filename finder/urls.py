from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path('logout/', views.user_logout, name='logout'),
    path("company_registration/", views.company_registration),
    path("company_login/", views.company_login, name='company_login'),
    path('add_job/', views.add_job, name='add_job'),
    path('company_profile/<int:comp_id>/', views.company_profile, name='company-profile'),
    path('my_joblist/<int:comp_id>/', views.my_joblist, name='my_joblist'),
    path('user_register/', views.user_register),
    path('user_login/', views.user_login, name='user_login'),

]