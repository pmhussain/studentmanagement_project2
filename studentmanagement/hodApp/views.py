from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import unauthenticated_user, admin_only
from django.contrib.auth.decorators import login_required
from studentmanagementApp.models import CustomUser

# Create your views here.
@login_required(login_url='login')
@admin_only
def hod_home(request):
    return render(request, 'hodApp/home.html')

@login_required(login_url='login')
# @admin_only
def add_student(request):
    return render(request, 'hodApp/add_student.html')

@login_required(login_url='login')
# @admin_only
def view_student(request):
    return render(request, 'hodApp/view_student.html')
