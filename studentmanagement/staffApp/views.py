from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_home(request):
    return render(request, 'staffApp/home.html')
