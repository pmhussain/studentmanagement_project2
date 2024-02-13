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
