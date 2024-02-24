from django.contrib import admin
from .models import *
# Register your models here.
class Attendance_ReportAdmin(admin.ModelAdmin):
    list_display = ['student', 'status', 'attendace', 'attendace_date']

admin.site.register(Staff_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Attendace)
admin.site.register(Attendance_Report,Attendance_ReportAdmin)
admin.site.register(Result)
