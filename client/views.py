from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import UpdateUserForm
from django.utils import timezone
from client.models import Article
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
def regular_articles(request):
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
    return render(request, 'client/regular-articles.html', context)


@login_required(login_url='my-login')
def manage_account(request):
    try:
       
        # Updating our account details
        form = UpdateUserForm(instance=request.user)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('client-dashboard')
        
        memberDetails = Membership.objects.get(user=request.user)
        context = {'UpdateUserForm': form, 'Membership': memberDetails}
        return render(request, 'client/manage-account.html', context)
    except:
   
        # Update our account details
        form = UpdateUserForm(instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('client-dashboard')
        
        # Pass through data to our template
        context = {'UpdateUserForm': form}
        return render(request, 'client/manage-account.html', context)


