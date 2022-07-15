from sys import path_hooks
from django.urls import path
from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('adminpage', views.adminPage, name='adminPage'),
    path('staff', views.staff, name='staff'),
    path('chairman', views.chairman, name='chairman'),
    path('director', views.director, name='director'),
    path('convenor', views.convenor, name='convenor'),
]