from sys import path_hooks
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', views.login_page, name='login'),
    path('adminpage', views.adminPage, name='adminPage'),
    path('staff', views.staff, name='staff'),
    path('chairman', views.chairman, name='chairman'),
    path('director', views.director, name='director'),
    path('convenor', views.convenor, name='convenor'),
]