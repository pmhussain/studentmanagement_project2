from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect((request.user.user_type).lower()+'_home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.user_type in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page!!!!')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.user_type=='STAFF':
            return redirect('staff_home')
        elif request.user.user_type=='STUDENT':
            return redirect('student_home')
        elif request.user.user_type=='HOD':
            return view_func(request, *args, **kwargs)
        else:
            # if user is not part of any group (STUDENT or STAFF or HOD) then not allowed to view any page
            return HttpResponse('You are not authorized to view this page.....')
    return wrapper_func
