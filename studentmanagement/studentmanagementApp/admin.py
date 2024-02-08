from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username','user_type','first_name', 'last_name','email','designation', 'mobileno', 'profile_pic']
admin.site.register(CustomUser,)
