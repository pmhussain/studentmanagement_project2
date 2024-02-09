from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import unauthenticated_user, admin_only
from django.contrib.auth.decorators import login_required
from studentmanagementApp.models import CustomUser
from .models import *

# Create your views here.
@login_required(login_url='login')
@admin_only
def hod_home(request):
    return render(request, 'hodApp/home.html')

@login_required(login_url='login')
# @admin_only
def add_student(request):
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic')
        mobileno = request.POST.get('mobileno')

        rno = request.POST.get('rno')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        print(profile_pic,rno,first_name,last_name,gender,address,email,mobileno,course_id,session_year_id)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is Already Exists")
            return redirect ('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "username("+username+") is Already taken")
            return redirect ('add_student')
        else:
            user = CustomUser(username=username, first_name=first_name,last_name=last_name, email=email, profile_pic=profile_pic, user_type='STUDENT', mobileno=mobileno,designation='Student')
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)
            student = Student(admin=user, rno=rno, Gender=gender, address=address, Course_id=course, session_year_id=session_year)
            student.save()
            messages.success(request, user.first_name+' '+user.last_name +' '+ 'is sucessfully added')
            return redirect(add_student)
    context = {
    'courses' : courses,
    'session_years' : session_years
    }
    return render(request, 'hodApp/add_student.html', context)

@login_required(login_url='login')
# @admin_only
def view_student(request):
    return render(request, 'hodApp/view_student.html')
