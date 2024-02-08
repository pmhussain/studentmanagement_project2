from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import CustomUser
from .forms import *
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render (request, 'studentmanagementApp/home.html')

@unauthenticated_user
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username,password)
        if CustomUser.objects.filter(username=username).exists():
            #user exist in User's authenticate password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                if user.user_type == 'HOD':
                    return redirect('hod_home')
                elif user.user_type == 'STAFF':
                    return redirect('staff_home')
                elif user.user_type == 'STUDENT':
                    return redirect('student_home')
            else:
                messages.info(request, "Password is not Valid")
        else:
            ##user NOT exist in users print username not exist.
            print("No user")
            messages.info(request, "Username does not exist")
            #return render(request, 'loginApp/login.html')
    return render(request, 'studentmanagementApp/login.html')

def userlogout(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # throw message when any fields are wrong while registering
            username = form.cleaned_data.get('username')
            # below commented code is for adding registered user to STUDENT group automatically, smae can do with signals.py
            # user = form.save()
            # username = form.cleaned_data.get('username')
            # group = Group.objects.get(name='STUDENT')
            # user.groups.add(group)
            messages.success(request,"Account created for "+ username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'studentmanagementApp/register.html', context)


@login_required(login_url='login')
def profile(request):
    user =request.user
    # print('custom user',CustomUser.objects.all().values() )
    context = {'user':user}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        profile_pic = request.FILES.get('profile_pic')
        if not profile_pic: # means if profile_pic not attached then use profile_pic as default profile_pic
            profile_pic = user.profile_pic
        try:
            # user = CustomUser.objects.get(id=pk)
            user=request.user
            user.first_name = first_name
            user.last_name = last_name
            user.designation = designation
            user.email = email
            user.mobileno = mobileno
            #  if profile_pic is attached, then check profile pic exist in direcorty or not if exist use the same.
            import os
            from django.conf import settings
            imageslist = os.listdir(settings.MEDIA_ROOT) # list of all images
            if  str(profile_pic) in imageslist:
                index = imageslist.index(str(profile_pic))
                print('same profile pic is present at index', index)
                user.profile_pic = imageslist[index]
            else:
                print('new profile pic')
                user.profile_pic = profile_pic
            user.save()
            print('Profile updated sucessfully')
            return redirect('profile',pk)
        except Exception as e:
            print(e)
            print('Profile not updated')
    return render(request, 'studentmanagementApp/profile.html', context)


@login_required(login_url='login')
def change_password(request):
    # user = CustomUser.objects.get(id=pk)
    user=request.user
    context = {'user':user}
    # print('old_password', user.password)
    if request.method == 'POST':
        username = user.username
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        if user.check_password(old_password):
            if new_password1 == new_password2:
                user.set_password(new_password2)
                user.save()
                messages.success(request, "Password changed Sucessfully, \n login again with new password!")
                return redirect('login')
            else:
                messages.warning(request, "two new passwords didnot matched")
        else:
            messages.warning(request, "You Entered wrong old password")
    return render(request, 'studentmanagementApp/change_password.html', context)
