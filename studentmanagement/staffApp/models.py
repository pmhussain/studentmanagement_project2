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
