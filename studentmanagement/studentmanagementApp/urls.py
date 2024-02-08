from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('register/', views.register, name="register"),
    path('home', views.home, name='home'),

    path('profile', views.profile, name="profile"),
    path('change_password', views.change_password, name="change_password"),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
