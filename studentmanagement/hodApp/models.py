from django.db import models
from studentmanagementApp.models import CustomUser
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_start+'-'+self.session_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    rno = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    address = models.TextField()
    Course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.first_name +" "+ self.admin.last_name
