from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from . import forms
from .models import User


# def login_page(request):
#     form = forms.LoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             pass
#     return render(request, 'authentication/login.html', context={'form': form})

def home(request):
    return render(request, 'account/home.html')

  # add to imports

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if (user is not None) and User.role:
                login(request, user)
                #message = f'Hello {user.username}! You have been logged in'
                return redirect('adminPage')
            else:
                message = 'Login failed!'
    return render(request, 'login.html', context={'form': form, 'message': message})


def adminPage(request):
    return render(request, 'account/admin.html')

def staff(request):
    return render(request, 'account/staff.html')

def chairman(request):
    return render(request, 'account/chairman.html')

def director(request):
    return render(request, 'account/director.html')


def convenor(request):
    return render(request, 'account/convenor.html')

