from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #fields = "__all__"
        fields = ['username', 'email', 'password1', 'password2']
