from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from creator.models import Article
from .models import Membership
from account.models import CustomUser


@login_required(login_url='my-login')
def client_dashboard(request):
    try:
        memDetails = Membership.objects.get(user=request.user)
        membership_plan = memDetails.membership_plan
        context = {'SubPlan': membership_plan}
        return render(request, 'client/client-dashboard.html', context)
    except:
        membership_plan = "None"
        context = {'SubPlan': membership_plan}
        return render(request, 'client/client-dashboard.html', context)


@login_required(login_url='my-login')
def browse_articles(request):
    user = request.user
    articles = Article.objects.filter(pub_date__lte=timezone.now())

    # Filter articles based on user access
    if user.is_staff or user.is_creator:
        # Staff and creators see all is_unlimited articles
        articles = articles.filter(is_unlimited=True) | articles
    elif hasattr(user, 'membership') and user.membership.is_unlimited:
        # Unlimited members see all articles
        pass
    else:
        # Users without unlimited access can't see is_unlimited articles
        articles = articles.filter(is_unlimited=False)

    context = {'AllClientArticles': articles}
    return render(request, 'client/browse-articles.html', context)