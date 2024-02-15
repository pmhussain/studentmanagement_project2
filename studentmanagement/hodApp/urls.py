from django.urls import path
from . import views
urlpatterns = [
    path('home', views.hod_home, name="hod_home"),
    path('add_student', views.add_student, name="add_student"),
    path('view_student', views.view_student, name="view_student"),
    path('edit_student/<int:id>', views.edit_student, name="edit_student"),
    path('delete_student/<str:admin>', views.delete_student, name="delete_student"), #instead of deleting the student we are deleting student admin so that student alsong with admin deleted
    #course urls
    path('add_course', views.add_course, name="add_course"),
    path('view_course', views.view_course, name="view_course"),
    path('edit_course/<int:id>', views.edit_course, name="edit_course"),
    path('delete_course/<int:id>', views.delete_course, name="delete_course"),
    #staff urls
    path('add_staff', views.add_staff, name="add_staff"),
    path('view_staff', views.view_staff, name="view_staff"),
    path('edit_staff/<int:id>', views.edit_staff, name="edit_staff"),
    path('delete_staff/<str:admin>', views.delete_staff, name="delete_staff"),

    #session urls
    path('add_session', views.add_session, name="add_session"),
    path('view_session', views.view_session, name="view_session"),
    path('edit_session/<int:id>', views.edit_session, name="edit_session"),
    path('delete_session/<int:id>', views.delete_session, name="delete_session"),

    #session urls
    path('add_subject', views.add_subject, name="add_subject"),
    path('view_subject', views.view_subject, name="view_subject"),
    path('edit_subject/<int:id>', views.edit_subject, name="edit_subject"),
    path('delete_subject//<int:id>', views.delete_subject, name="delete_subject"),

    #session urls
    path('staff_notification', views.staff_notification, name="staff_notification"),
    path('student_notification', views.student_notification, name="student_notification"),

    path('view_staff_leaves', views.view_staff_leaves, name="view_staff_leaves"),
    path('view_staff_feedbacks', views.view_staff_feedbacks, name="view_staff_feedbacks"),
    path('view_student_leaves', views.view_student_leaves, name="view_student_leaves"),
    ]
