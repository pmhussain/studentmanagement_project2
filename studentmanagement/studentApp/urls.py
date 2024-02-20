from django.urls import path
from . import views
urlpatterns = [
    path('home', views.student_home, name="student_home"),
    path('student_view_attendance', views.student_view_attendance, name="student_view_attendance"),
    ]
