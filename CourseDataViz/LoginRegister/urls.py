from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('secret/', views.secret, name="secret"),
    path('upload_data/', views.upload_data, name="upload"),
]