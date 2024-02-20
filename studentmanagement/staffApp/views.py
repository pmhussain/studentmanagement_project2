from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from hodApp.models import Staff

from django.contrib.auth.models import User, Group
from studentmanagementApp.decorators import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_home(request):
    return render(request, 'staffApp/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def notifications(request):
    staff = Staff.objects.get(admin=request.user)
    notifications = Staff_Notification.objects.filter(staff=staff)
    if request.method == 'POST':
        notification_status = request.POST.get('notification_status', None)
        notification_id = request.POST.get('notification_id')
        print('notification_status : ',notification_status)
        print('notification_id : ',notification_id)
        notification = Staff_Notification.objects.get(id=notification_id)
        notification.status = 1
        notification.save()
        return redirect('notifications')

    context={
    'notifications': notifications,
    }
    return render(request, 'staffApp/notifications.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_leave_aaply(request):

    if request.method == 'POST':
        leave_from_date = request.POST.get('leave_from_date')
        leave_to_date = request.POST.get('leave_to_date')
        leave_no_of_days = request.POST.get('leave_no_of_days')
        leave_reason = request.POST.get('leave_reason')
        print( leave_from_date, leave_to_date,leave_no_of_days,leave_reason )
        print(request.user, type(request.user))
        staff = Staff.objects.get(admin=request.user)
        staff_leave = Staff_Leave (staff=staff,
                                   leave_from_date=leave_from_date,
                                   leave_to_date=leave_to_date,
                                   leave_days=leave_no_of_days,
                                   leave_message=leave_reason)
        staff_leave.save()
        messages.success(request, ' Leave submitted sucessfully..!')
        return redirect('staff_leave_aaply')
    return render(request, 'staffApp/staff_leave_aaply.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_leave_view(request):
    staff = Staff.objects.get(admin=request.user)
    leaves = Staff_Leave.objects.filter(staff=staff).order_by('-created_at')
    for leave in leaves:
        print(leave)
    if request.method == 'POST':
        notification_status = request.POST.get('notification_status', None)
        notification_id = request.POST.get('notification_id')
        print('notification_status : ',notification_status)
        print('notification_id : ',notification_id)
        notification = Staff_Notification.objects.get(id=notification_id)
        notification.status = 1
        notification.save()
        return redirect('notifications')

    context={
    'leaves': leaves,
    }
    return render(request, 'staffApp/staff_leave_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_sendfeedback(request):
    if request.method == 'POST':
        staff_feedback = request.POST.get('staff_feedback')
        staff = Staff.objects.get(admin=request.user)
        feedback = Staff_Feedback (staff=staff, feedback=staff_feedback, feedback_reply="")
        feedback.save()
        messages.success(request, ' Feedback submitted sucessfully..!')
        return redirect('staff_sendfeedback')
    return render(request, 'staffApp/staff_sendfeedback.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def staff_feedbacks_view(request):
    staff = Staff.objects.get(admin=request.user)
    feedbacks = Staff_Feedback.objects.filter(staff=staff).order_by('-created_at')
    if request.method == 'POST':
        notification_status = request.POST.get('notification_status', None)
        notification_id = request.POST.get('notification_id')
        print('notification_status : ',notification_status)
        print('notification_id : ',notification_id)
        notification = Staff_Notification.objects.get(id=notification_id)
        notification.status = 1
        notification.save()
        return redirect('notifications')

    context={
    'feedbacks': feedbacks,
    }

    return render(request, 'staffApp/staff_feedbacks_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def take_attendance(request):
    courses = Course.objects.all()
    staff = Staff.objects.get(admin=request.user)
    subjects = Subject.objects.filter(staff=staff)
    session_years = Session_Year.objects.all().order_by('session_start')
    get_subject = None
    get_course = None
    get_session_year = None
    students = None
    action = request.GET.get('action')
    print("action : ", action)
    if action is not None:
        print('getting subject...')
        if request.method == 'POST':
            # attendace_date = request.POST.get('attendace_date')
            course_id = request.POST.get('course_id')
            get_course = Course.objects.get(id=course_id)
            session_year_id = request.POST.get('session_year_id')
            get_session_year = Session_Year.objects.get(id=session_year_id)
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            students = Student.objects.filter(Course_id=course_id, session_year_id=session_year_id)
            print(students)
    else:
        if request.method == 'POST':
            print('saving attendace...')
            attendace_date = request.POST.get('attendace_date')
            course_id = request.POST.get('course_id')
            course = Course.objects.get(id=course_id)
            session_year_id = request.POST.get('session_year_id')
            session_year = Session_Year.objects.get(id=session_year_id)
            subject_id = request.POST.get('subject_id')
            subject = Subject.objects.get(id=subject_id)
            attendace = Attendace(date=attendace_date, course=course,
                                   session_year=session_year, subject=subject)
            attendace.save()
            students = Student.objects.filter(Course_id=course_id, session_year_id=session_year_id)
            attended_students = request.POST.getlist('attended_students')
            print('attended_students : ', attended_students)
            for student in students:
                status = 'Absent'
                print(student.id)
                student_id = str(student.id)
                if student_id in attended_students:
                    status = "Present"
                student_attendacne = Attendance_Report (student=student, attendace=attendace, status=status)
                student_attendacne.save()
            messages.success(request, ' Attendace submitted sucessfully..!')
            return redirect('take_attendance')



    context = {
    'courses' : courses,
    'subjects' : subjects,
    'session_years' : session_years,
    'get_course' : get_course,
    'get_subject' : get_subject,
    'get_session_year' : get_session_year,
    'action' : action,
    'students' : students
    }
    return render(request, 'staffApp/take_attendance.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def view_attendance(request):
    print("user type : " , request.user.user_type)
    user_type = request.user.user_type
    if user_type == 'HOD':
        subjects = Subject.objects.all()
    elif user_type == 'STAFF':
        staff = Staff.objects.get(admin=request.user)
        subjects = Subject.objects.filter(staff=staff)
    session_years = Session_Year.objects.all()
    action = request.GET.get('action')
    get_date = None
    get_session_year = None
    get_subject = None
    attendace_date=None
    attendace_report = None
    if action is not None:
        print('getting subject...')
        if request.method == 'POST':
            attendace_date = request.POST.get('attendace_date')
            print('attendace_date : ', attendace_date)
            session_year_id = request.POST.get('session_year_id')
            get_session_year = Session_Year.objects.get(id=session_year_id)
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            # students = Student.objects.filter(Course_id=course_id)
            attendace = Attendace.objects.filter(date=attendace_date, subject=subject_id, session_year=session_year_id)
            print('attendace : ', attendace)
            for i in attendace:
                attendace_id = i.id
                attendace_report = Attendance_Report.objects.filter(attendace=attendace_id)
                print(attendace_report)
    context = {
    'subjects' : subjects,
    'session_years' : session_years,
    'action' : action,
    'get_date' : attendace_date,
    'get_session_year' : get_session_year,
    'get_subject' : get_subject,
    'attendace_report' : attendace_report
    }
    return render (request,'staffApp/view_attendance.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['STAFF'])
def add_result(request):
    staff = Staff.objects.get(admin=request.user)
    subjects = Subject.objects.filter(staff=staff)
    session_years = Session_Year.objects.all()
    action = request.GET.get('action')
    if action is not None:
        if request.method=='POST':
            session_year_id = request.POST.get('session_year_id')
            subject_id = request.POST.get('subject_id')
            get_session_year = Session_Year.objects.get(id=session_year_id)
            get_subject = Subject.objects.get(id=subject_id)

    context = {
    'subjects' : subjects,
    'session_years' : session_years,
    'action' : action,
    }
    return render (request, 'staffApp/add_result.html', context)
