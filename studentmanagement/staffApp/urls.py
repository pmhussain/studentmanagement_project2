from django.urls import path
from . import views
urlpatterns = [
    path('home', views.staff_home, name="staff_home"),
    path('notifications', views.notifications, name="notifications"),
    ]
