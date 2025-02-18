from django.shortcuts import render

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

            article.user = request.users
            
            article.save()
            
            return HttpResponse ('Article created!')

    context = {'CreateArtcleForm': form}

    return render(request, 'creator/create-article.html', context)

@login_required(login_url='my-login')
def my_article(request):
    
    current_user = request.user.id
    
    article =  Article.objects.filter(user=current_user)
    
    context  = {'AllArticle': article}
    
    return render(request, 'creator/my-article.html', context)