from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from user.forms import ChangePasswordForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been logged in to your account!')
            return redirect('post:home')
        else:
            messages.error(request, 'Oops! Username and Password do not match!')
            return redirect('user:login')
    else:
        context = {'title': 'Login'}
        return render(request, 'login.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out of your account!')
    return redirect('user:login')

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
                messages.error(request, 'Oops! User with this Username already exists.')
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Oops! User with this Email already exists.')
                return redirect('user:register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, f'Congratulations! {first_name}, Your account has been created successfully!')
                return redirect('post:home')
        else:
            messages.error(request, 'Oops! Password do not match.')
            return redirect('user:register')

    else:
        context = {'title': 'Register'}
        return render(request, 'signup.html', context)

@login_required
def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'profile.html', context)

def password_reset(request):
        context = {'title': 'Reset Password'}
        return render(request, 'reset-password.html', context)

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, user)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if not user.check_password(old_password):
                messages.error(request, 'Oops! Your old password was entered incorrectly.')
                return redirect('user:change-password')
            elif new_password != confirm_password:
                messages.error(request, 'Oops! Your passwords do not match.')
                return redirect('user:change-password')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Congratulations! Your password was changes successfully.')
                return redirect('post:home')

    else:
        form = ChangePasswordForm(instance=user)
    context = {'title':'Change Password', 'form':form}
    return render(request, 'change-password.html', context)
