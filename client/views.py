
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from client.forms import ArticleForm, UpdateUserForm
from creator.models import Article
from django.contrib.auth.models import User  

@login_required(login_url='my-login')
def client_dashboard(request):
    user_articles = Article.objects.filter(user=request.user)
    return render(request, 'client/client-dashboard.html', {'articles': user_articles})
  

@login_required(login_url='my-login')
def regular_articles(request):
    # Fetch only published articles
    articles = Article.objects.filter(is_published=True)

    return render(request, 'client/regular-articles.html', {'AllArticles': articles})

@login_required(login_url='my-login')
def manage_account(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('client-dashboard')

    return render(request, 'client/manage-account.html', {'UpdateUserForm': form})

@login_required(login_url='my-login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  
        return redirect("delete-account-success")  

    return render(request, 'client/delete-account.html')

def delete_account_success(request):
    return render(request, 'client/delete-account-success.html')

@login_required(login_url='my-login')
def delete_success(request):
    return render(request, 'creator/delete-success.html')

@login_required(login_url='my-login')
def update_success(request):
    return render(request, 'creator/update-success.html')