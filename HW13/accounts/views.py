from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Task.models import Tasks

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.first_name = cd['last_name']
            user.save()
            messages.success(request, 'با موفقیت ثبت نام شدید!', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password= cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید!', 'success')
                return redirect('user_page_url', user_id=user.id)
        else:
            messages.error(request, 'نام کاربری یا رمزعبور اشتباه است!!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت از سایت خارج شدید!', 'danger')
    return redirect('home')

    
    
def User_page(request, user_id):
    tasks = Tasks.objects.filter(user__id=user_id)
    return render(request, 'accounts/user_page.html', {'tasks':tasks})