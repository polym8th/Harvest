from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article


@login_required(login_url='my-login')
def creator_dashboard(request):
    return render(request, 'creator/creator-dashboard.html')


@login_required(login_url='my-login')
def create_article(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():     
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('published')

    context = {'CreateArticleForm': form}
    return render(request, 'creator/create-article.html', context)


@login_required(login_url='my-login')
def published(request):
    current_user = request.user.id
    articles = Article.objects.filter(user=current_user)
    context = {'AllArticles': articles}
    return render(request, 'creator/published.html', context)


@login_required(login_url='my-login')
def update_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)
    except Article.DoesNotExist:
        return redirect('published')

    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('published')

    context = {'UpdateArticleForm': form}
    return render(request, 'creator/update-article.html', context)


@login_required(login_url='my-login')
def delete_article(request, pk):
    
    article = Article.objects.get(id=pk) 

    if request.method == 'POST':
        
        article.delete()
        
        return redirect('published')

    return render(request, 'creator/delete-article.html')
