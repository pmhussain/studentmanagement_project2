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
