from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from . forms import ArticleForm

from django.http import HttpResponse

from . models import Article


@login_required(login_url='my-login')
def creator_dashboard(request):
    
    return render(request, 'creator/creator-dashboard.html')

@login_required(login_url='login')
def create_article(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():     
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            
            return redirect ('published')

    context = {'CreateArticleForm': form}

    return render(request, 'creator/create-article.html', context)

@login_required(login_url='my-login')
def published(request):
    
    current_user = request.user.id
    
    article =  Article.objects.filter(user=current_user)
    
    context  = {'AllArticles': article}
    
    return render(request, 'creator/published.html', context)