from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def login(request):
    context = {'title': 'Login'}
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! User with this Username already exists.')
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Oops! User with this Email already exists.')
                return redirect('user:register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, f'Congratulations! {first_name}, Your account has been created successfully!')
                return redirect('post:home')
        else:
            messages.info(request, 'Oops! Password do not match.')
            return redirect('user:register')

    else:
        context = {'title': 'Register'}
        return render(request, 'signup.html', context)

def password_change(request):
    context = {'title': 'Change Password'}
    return render(request, 'change-password.html', context)
