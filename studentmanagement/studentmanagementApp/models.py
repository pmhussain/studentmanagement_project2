from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
    ('HOD','HOD'),
    ('STAFF','STAFF'),
    ('STUDENT', 'STUDENT')
    )
    user_type = models.CharField(choices=USER, max_length=50, default = 'STUDENT', null =True)
    designation = models.CharField(max_length=500, blank=True, null =True)
    mobileno = models.CharField(max_length=30, blank=True, null =True)
    profile_pic = models.ImageField(default='img_avatar.png', blank=True)
