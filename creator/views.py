from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import ArticleForm, UpdateUserForm
from .models import Article

"""
The above functions are Django views that handle creating, updating, publishing, and deleting
articles, managing user accounts, and displaying dashboard for creators with appropriate permissions
and error handling.
"""

@login_required(login_url='my-login')
def creator_dashboard(request):
    # FIX: Ensured function body is properly indented (4 spaces)
    user_articles = Article.objects.filter(user=request.user)
    
    # Pass the articles to the template
    return render(request, 'creator/creator-dashboard.html', {'articles': user_articles})


@login_required(login_url='my-login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'Your article has been created successfully!')
            return redirect('published')
    else:
        form = ArticleForm()
    # FIX: Maintained consistent indentation in the return statement
    return render(request, 'creator/create-article.html', {'CreateArticleForm': form})


@login_required(login_url='my-login')
def published(request):
    if getattr(request.user, 'has_unlimited_access', False):
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(is_unlimited=False)
    # FIX: Ensured proper indentation for the return statement
    return render(request, 'creator/published.html', {'AllArticles': articles})


@login_required(login_url='my-login')
def update_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    
    # Allow superusers or article owners/creators to update
    if not (request.user.is_superuser or article.user == request.user or getattr(request.user, 'is_creator', False)):
        raise PermissionDenied("You do not have permission to update this article.")

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been updated successfully!', extra_tags='update')
            return redirect('update-success')
    else:
        form = ArticleForm(instance=article)

    # FIX: Return statement indented consistently
    return render(request, 'creator/update-article.html', {'UpdateArticleForm': form})


@login_required(login_url='my-login')
def delete_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    # Allow superusers or article owners/creators to delete
    if not (request.user.is_superuser or article.user == request.user or getattr(request.user, 'is_creator', False)):
        raise PermissionDenied("You do not have permission to delete this article.")

    if request.method == 'POST':
        article.delete()
        messages.success(request, 'The article has been deleted successfully.', extra_tags='delete')
        return redirect('delete-success')

    return render(request, 'creator/delete-article.html', {'article': article})


@login_required(login_url='my-login')
def manage_account(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('creator-dashboard')

    context = {'UpdateUserForm': form}
    return render(request, 'creator/manage-account.html', context)


@login_required(login_url='my-login')
def delete_success(request):
    return render(request, 'creator/delete-success.html')


@login_required(login_url='my-login')
def update_success(request):
    return render(request, 'creator/update-success.html')
