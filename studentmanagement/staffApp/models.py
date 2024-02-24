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

class Staff_Feedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff.admin.first_name +" "+ self.staff.admin.last_name

class Attendace(models.Model):
    date = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_year = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject.name

class Attendance_Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendace = models.ForeignKey(Attendace, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=(('Present','Present'),('Absent','Absent')), max_length=10, default = 'Absent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.admin.first_name +" "+ self.student.admin.last_name

    from django.contrib import admin
    @admin.display(description="Date")
    def attendace_date(self):
        return self.attendace.date

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    quiz_marks = models.FloatField()
    exam_marks = models.FloatField()
    # total_marks = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.admin.first_name +" "+ self.student.admin.last_name
