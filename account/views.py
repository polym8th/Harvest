from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            is_creator = form.cleaned_data.get('is_creator')
            user.is_creator = is_creator
            user.save()

            # Prepare messages based on user selections
            messages = ["Well done, your account has been created successfully!"]
            if is_creator:
                messages.append("You are now a content creator!")

            return render(request, 'account/registration_success.html', {'messages': messages})
    else:
        form = CreateUserForm()

    return render(request, 'account/register.html', {'RegisterForm': form})

def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None and hasattr(user, 'is_creator'):
                login(request, user)
                if user.is_creator:
                    return redirect('creator-dashboard')
                else:
                    return redirect('client-dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'account/my-login.html', {'LoginForm': form})


def user_logout(request):
    logout(request)
    return redirect('my-login')
