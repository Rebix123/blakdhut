from django.shortcuts import redirect, render
from user.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')  
            messages.success(request, f'Account created for {username} successfully!')
            new_user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            if new_user:
                login(request, new_user)
            return redirect('user:dashboard')
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user:dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Welcome back {user.username}!')
            return redirect('user:dashboard')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'user/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('user:login')

@login_required
def dashboard_view(request):
    user = request.user
    return render(request, 'user/dashboard.html', {'user': user})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})

@login_required
def update_profile_view(request):
    user  = request.user
    return render(request, 'user/update.html', {'user': user})

@login_required
def buy_view(request):
    user = request.user
    return render(request, 'user/buy.html', {'user': user})

def comingsoon_view(request):
    user = request.user
    return render(request, 'user/comingsoon.html', {'user': user})

@login_required
def history_view(request):
    user = request.user
    return render(request, 'user/history.html', {'user':user} )