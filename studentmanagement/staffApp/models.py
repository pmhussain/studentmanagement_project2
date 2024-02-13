from django.db import models
from hodApp.models import *
# Create your models here.
class Staff_Notification(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0, null=True)


    def __str__(self):
        return self.message

class Staff_Leave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_from_date = models.CharField(max_length=20)
    leave_to_date = models.CharField(max_length=20)
    leave_days = models.IntegerField()
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.staff.admin.first_name +" "+ self.staff.admin.last_name
