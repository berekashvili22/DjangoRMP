from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CreateUserForm
from pages.views import home

from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.user.is_authenticated:
        # return redirect('home')
        pass

    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Your account has been created, Log in now')
                return redirect('login')
        else:
            form = CreateUserForm()
    
    return render(request, 'Account/register.html', {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.username}, You are logged in')
                return redirect('home')
            else:
                messages.info(request, f'Username or Password is incorrect')

    return render(request, 'Account/login.html')

def logoutUser(request):
    logout(request)
    print('logout')
    messages.info(request, f'You\'ve been logged out')
    return redirect('login')