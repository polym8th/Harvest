from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .forms import ArticleForm, UpdateUserForm
from .models import Article  # Import Article model
from django.contrib import messages



@login_required(login_url='my-login')  # Ensure only logged-in users can access
def creator_dashboard(request):
    return render(request, 'creator/creator-dashboard.html')  # Render dashboard template


@login_required(login_url='my-login')

@login_required(login_url='my-login')
def create_article(request):
    if request.method == 'POST':  # Check if form is submitted
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  
            article.user = request.user
            article.save()
            messages.success(request, 'Well done, your article has been created successfully!') 
            return redirect('published')
    else:
        form = ArticleForm() 

    return render(request, 'creator/create-article.html', {'CreateArticleForm': form})  # Render form template


@login_required(login_url='my-login')
def published(request):
    if getattr(request.user, 'has_unlimited_access', False):
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(is_unlimited=False)
    return render(request, 'creator/published.html', {'AllArticles': articles})


@login_required(login_url='my-login')
def update_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)  # Fetch article by ID and user
    except Article.DoesNotExist:
        return redirect('published')  # Redirect if article doesn't exist

    if request.method == 'POST': 
        form = ArticleForm(request.POST, instance=article)  # Bind form with POST data and existing article
        if form.is_valid():  # Validate form
            form.save()  
            return redirect('published')  
    else:
        form = ArticleForm(instance=article)  

    return render(request, 'creator/update-article.html', {'UpdateArticleForm': form}) 


@login_required(login_url='my-login')
def delete_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    # Check if user has permission to delete the article
    if article.user == request.user or getattr(request.user, 'is_unlimited', False) or request.user.is_superuser or getattr(request.user, 'is_creator', False):
        if request.method == 'POST':
            article.delete()
            return redirect('published')
    else:
        return redirect('published')  # Redirect if user lacks permission

    return render(request, 'creator/delete-article.html', {'article': article})


@login_required(login_url='my-login')
def manage_account(request):
    form = UpdateUserForm(instance=request.user)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('creator-dashboard')
    
    context = {'UpdateUserForm': form}
    return render(request, 'creator/manage-account.html', context)
