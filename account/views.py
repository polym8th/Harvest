from django.shortcuts import render, redirect  # ✅ Added redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'account/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')

    context = {'RegisterForm': form}
    return render(request, 'account/register.html', context)

def my_login(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None and hasattr(user, 'is_creator'):  # ✅ Prevents AttributeError if is_creator is missing
                login(request, user)
                
                if user.is_creator:
                    return redirect('creator-dashboard')
                else:
                    return redirect('client-dashboard')
    
    context = {'LoginForm': form}        
    return render(request, 'account/my-login.html', context)

def user_logout(request):
    
    logout(request)
    
    return redirect('my-login')