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
        user = CustomUser.objects.get(id=student.admin.id)
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


## COURSE Functions
@login_required(login_url='login')
@admin_only
def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = Course(name=course_name)
        course.save()
        messages.success(request, course_name + ' course is sucessfully created')
        return redirect ('view_course')
    return render(request, 'hodApp/add_course.html')

@login_required(login_url='login')
@admin_only
def view_course(request):
    courses = Course.objects.all()
    context ={
         'courses':courses,
    }
    return render(request, 'hodApp/view_course.html',context)

@login_required(login_url='login')
@admin_only
def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course.name = course_name
        course.save()
        messages.success(request, course_name + ' course is sucessfully updated..')
        return redirect('view_course')
    context ={
         'course':course,
    }
    return render(request, 'hodApp/edit_course.html',{'course':course})

@login_required(login_url='login')
@admin_only
def delete_course(request,id):
    course=Course.objects.get(id=id)
    if request.method == 'POST':
        course_name = course.name
        course.delete()
        messages.warning(request,course_name+ ' course is sucessfully deleted..')
        return redirect('view_course')
    context ={
         'course':course,
    }
    return render(request, 'hodApp/delete_course.html',context)

@login_required(login_url='login')
@admin_only
def add_staff(request):

    if request.method == "POST":
        username = request.POST.get('username')
        staff_id = request.POST.get('staff_id')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic','img_avatar.png')

        mobileno = request.POST.get('mobileno')

        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is Already Exists")
            return redirect ('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "username("+username+") is Already taken")
            return redirect ('add_student')
        else:
            user = CustomUser(username=username, first_name=first_name,last_name=last_name, email=email, profile_pic=profile_pic, user_type='STAFF', mobileno=mobileno,designation=designation)
            user.set_password(password)
            user.save()
            staff = Staff(admin=user, staff_id=staff_id, Gender=gender, address=address, designation=designation)
            staff.save()
            messages.success(request, user.first_name+' '+user.last_name +' '+ 'is sucessfully added')
            return redirect('view_staff')

    return render(request, 'hodApp/add_staff.html')

@login_required(login_url='login')
@admin_only
def view_staff(request):
    stafff = Staff.objects.all().order_by('-created_at')
    context = {
    'stafff' : stafff,
    }
    return render(request, 'hodApp/view_staff.html',context)

@login_required(login_url='login')
@admin_only
def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    context = {
    'staff' : staff,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic')
        mobileno = request.POST.get('mobileno')

        staff_id = request.POST.get('staff_id')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        designation = request.POST.get('designation')
        #
        user = CustomUser.objects.get(id=staff.admin.id)
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
        staff = Staff.objects.get(id=id)
        staff.staff_id=staff_id
        staff.Gender=gender
        staff.address=address
        staff.designation=designation
        staff.save()
        return redirect('view_staff')
    return render(request, 'hodApp/edit_staff.html',context)


@login_required(login_url='login')
@admin_only
def delete_staff(request,admin):
    staffadmin = CustomUser.objects.get(username=admin) # getting student admin
    if request.method == 'POST':
        user = staffadmin.first_name +" " + staffadmin.last_name
        staffadmin.delete() #deleting student admin so that student also deleted
        messages.success(request, user + ' is sucessfully deleted')
        return redirect ('view_staff')
    context = {
    'staffadmin':staffadmin
    }
    return render(request, 'hodApp/delete_staff.html',context)


@login_required(login_url='login')
@admin_only
def add_session(request):
    if request.method == "POST":
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        if Session_Year.objects.filter(session_start=session_start).exists():
            messages.warning(request, "Session_start Year is Already Exists")
            return redirect ('add_session')
        if Session_Year.objects.filter(session_end=session_end).exists():
            messages.warning(request, "Session_end Year is Already Exists")
            return redirect ('add_session')
        session = Session_Year(session_start=session_start,session_end=session_end )
        session.save()
        messages.success(request, session_start +" - "+session_end+ ' course is sucessfully created')
        return redirect ('view_session')
    return render(request, 'hodApp/add_session.html')


@login_required(login_url='login')
@admin_only
def view_session(request):
    sessions = Session_Year.objects.all().order_by('-session_start')
    context ={
         'sessions':sessions,
    }
    return render(request, 'hodApp/view_session.html', context)


@login_required(login_url='login')
@admin_only
def edit_session(request,id):
    session=Session_Year.objects.get(id=id)
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        
        session.session_start = session_start
        session.session_end = session_end
        session.save()
        messages.success(request, 'session is sucessfully updated..')
        return redirect('view_session')
    context ={
         'session':session,
    }
    return render(request, 'hodApp/edit_session.html',context)


@login_required(login_url='login')
@admin_only
def delete_session(request,id):
    session=Session_Year.objects.get(id=id)
    if request.method == 'POST':
        session.delete()
        messages.warning(request,'Session is sucessfully deleted..')
        return redirect('view_session')
    context ={
         'session':session,
    }
    return render(request, 'hodApp/delete_session.html', context)
