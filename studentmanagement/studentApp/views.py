from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from hodApp.models import *
from staffApp.models import *

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['STUDENT'])
def student_home(request):
    return render(request, 'studentApp/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['STUDENT'])
def student_view_attendance(request):
    student = Student.objects.get(admin=request.user)
    course = Course.objects.get(name=student.Course_id)
    subjects = Subject.objects.filter(course=course.id)
    session_years = Session_Year.objects.all()
    action = request.GET.get('action')
    attendace_report=None
    attendace_date=None
    if action is not None:
        if request.method == 'POST':
            attendace_date = request.POST.get('attendace_date')
            subject_id = request.POST.get('subject_id')
            attendace_report=Attendance_Report.objects.filter(student=student)
            print(attendace_report)
    context = {
    'subjects' : subjects,
    'session_years' : session_years,
    'attendace_report' : attendace_report,
    'action' : action,
    'attendace_date' : attendace_date
    }
    return render(request, 'studentApp/student_view_attendance.html', context)
