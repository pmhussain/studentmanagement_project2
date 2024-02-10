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
@admin_only
def add_student(request):
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic','img_avatar.png')

        mobileno = request.POST.get('mobileno')

        rno = request.POST.get('rno')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        print("course_id",course_id)
        print("session_year_id",session_year_id)
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
            return redirect(view_student)
    context = {
    'courses' : courses,
    'session_years' : session_years
    }
    return render(request, 'hodApp/add_student.html', context)

@login_required(login_url='login')
@admin_only
def view_student(request):
    students = Student.objects.all().order_by('-created_at')
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()
    context = {
    'students' : students,
    'courses' : courses,
    'session_years' : session_years
    }
    return render(request, 'hodApp/view_student.html', context)

@login_required(login_url='login')
@admin_only
def edit_student(request,id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all()
    session_years = Session_Year.objects.all()
    context = {
    'student' : student,
    'courses' : courses,
    'session_years' : session_years
    }
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
        #
        user = CustomUser.objects.get(username=username)
        user.username=username # present databaseuser(user.username) = updateduser(username) which you get in POST request
        if password!=None and password!="":
            user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        if profile_pic!=None and profile_pic!="":
            user.profile_pic=profile_pic
        user.mobileno=mobileno
        user.save()

        #
        student = Student.objects.get(id=id)
        student.rno=rno
        student.Gender=gender
        student.address=address
        #
        course = Course.objects.get(id=course_id)
        student.Course_id=course
        print(student.Course_id)
        session_year=Session_Year.objects.get(id=session_year_id)
        student.session_year_id=session_year
        student.save()
        return redirect('view_student')

    return render(request, 'hodApp/edit_student.html', context)

@login_required(login_url='login')
@admin_only
def delete_student(request,admin):
    studentadmin = CustomUser.objects.get(username=admin) # getting student admin
    if request.method == 'POST':
        user = studentadmin.first_name +" " + studentadmin.last_name
        studentadmin.delete() #deleting student admin so that student also deleted
        messages.success(request, user + ' is sucessfully deleted')
        return redirect ('view_student')
    context = {
    'studentadmin':studentadmin
    }
    return render(request, 'hodApp/delete_student.html',context)
