from django.urls import path
from . import views
urlpatterns = [
    path('home', views.staff_home, name="staff_home"),
    path('notifications', views.notifications, name="notifications"),
    path('staff_leave_aaply', views.staff_leave_aaply, name="staff_leave_aaply"),
    path('staff_leave_view', views.staff_leave_view, name="staff_leave_view"),
    ]
