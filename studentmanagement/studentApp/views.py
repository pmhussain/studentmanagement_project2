from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['STUDENT'])
def student_home(request):
    return render(request, 'studentApp/home.html')
