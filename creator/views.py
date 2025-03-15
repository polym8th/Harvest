from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from creator.forms import ArticleForm, UpdateUserForm
from .models import Article
from django.utils import timezone 
from django_ckeditor_5.widgets import CKEditor5Widget


def index(request):
    teaser_articles = Article.objects.filter(article_teaser=True, is_published=True)
    return render(request, 'accounts/index.html', {'teaser_articles': teaser_articles})

@login_required(login_url='my-login')
def creator_dashboard(request):
    user_articles = Article.objects.filter(user=request.user)
    return render(request, 'creator/creator-dashboard.html', {'articles': user_articles})

@login_required(login_url='my-login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.article_teaser = request.POST.get('article_teaser', "0") == "1"
            
            # Handle event-related fields
            article.is_event_related = request.POST.get('is_event_related') == 'on'
            if article.is_event_related:
                article.event_date = request.POST.get('event_date')
                article.event_name = request.POST.get('event_name')
                article.event_venue = request.POST.get('event_venue')
                article.event_location = request.POST.get('event_location')
                article.event_postcode = request.POST.get('event_postcode')
            # Debug: Print image upload info
            if 'image' in request.FILES:
                uploaded_image = request.FILES['image']
                print(f"✅ Image Uploaded: {uploaded_image.name} | Size: {uploaded_image.size} bytes | Type: {uploaded_image.content_type}")
    
            
            article.save()
            return redirect('create-article-success')  # Redirect to the new success page
    else:
        form = ArticleForm()

    return render(request, 'creator/create-article.html', {'CreateArticleForm': form})

@login_required(login_url='my-login')
def create_article_success(request):
    return render(request, 'creator/create-article-success.html')

def article_guest(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'account/article-guest.html', {'article': article})

@login_required(login_url='my-login')
def published(request):
    articles = Article.objects.filter(is_published=True) | Article.objects.filter(article_teaser=True)
    events = Article.objects.filter(is_event_related=True, is_published=True)
    return render(request, 'creator/published.html', {
        'AllArticles': articles,
        'Events': events
    })

@login_required(login_url='my-login')
def update_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)

            article.updated_by = request.user  # Store the user who updated it
            article.updated_at = timezone.now()  # Store the update time

            article.save()
            messages.success(request, '✅ Your article has been updated successfully!', extra_tags='update')
            return redirect('update-article-success')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'creator/update-article.html', {
        'UpdateArticleForm': form,
        'article': article
    })
    
@login_required(login_url='my-login')
def update_article_success(request):
    return render(request, 'creator/update-article-success.html')

@login_required(login_url='my-login')
def delete_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    # Allow only superusers to delete any article, while creators can delete their own
    if not (request.user.is_superuser or (request.user.is_creator and article.user == request.user)):
        messages.error(request, "❌ You cannot delete this article as you are not the creator of it.")
        return redirect(request.META.get('HTTP_REFERER', 'creator-dashboard'))  # Redirect to the previous page

    if request.method == 'POST':
        article.delete()
        messages.success(request, '✅ The article has been deleted successfully.')
        return redirect('delete-success')

    return render(request, 'creator/delete-success.html', {'article': article})

@login_required(login_url='my-login')
def manage_account(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('creator-dashboard')

    return render(request, 'account/manage-account.html', {'UpdateUserForm': form})

@login_required(login_url='my-login')
def delete_success(request):
    return render(request, 'creator/delete-success.html')

@login_required(login_url='my-login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  
        return redirect("delete-account-success")  

    return render(request, 'account/delete-account.html')

def delete_account_success(request):
    return render(request, 'account/delete-account-success.html')
