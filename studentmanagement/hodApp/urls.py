from django.urls import path
from . import views
urlpatterns = [
    path('home', views.hod_home, name="hod_home"),
    path('add_student', views.add_student, name="add_student"),
    path('view_student', views.view_student, name="view_student"),
    path('edit_student/<int:id>', views.edit_student, name="edit_student"),
    path('delete_student/<str:admin>', views.delete_student, name="delete_student"), #instead of deleting the student we are deleting student admin so that student alsong with admin deleted

    path('add_course', views.add_course, name="add_course"),
    path('view_course', views.view_course, name="view_course"),
    path('edit_course/<int:id>', views.edit_course, name="edit_course"),
    path('delete_course/<int:id>', views.delete_course, name="delete_course"),
    ]
