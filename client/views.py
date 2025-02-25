from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from creator.models import Article
from account.models import CustomUser

@login_required(login_url='my-login')
def client_dashboard(request):
    user_articles = Article.objects.filter(user=request.user)
    return render(request, 'client/client-dashboard.html', {'articles': user_articles})
    return render(request, 'client/client-dashboard.html', context)

@login_required(login_url='my-login')
def regular_articles(request):
    user = request.user
    # Removed is_unlimited filter
    articles = Article.objects.filter(pub_date__lte=timezone.now())

    context = {'AllClientArticles': articles}
    return render(request, 'client/regular-articles.html', context)

@login_required(login_url='my-login')
def manage_account(request):
    try:
        # Updating account details
        form = UpdateUserForm(instance=request.user)

        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('client-dashboard')

        memberDetails = Membership.objects.get(user=request.user)
        context = {'UpdateUserForm': form, 'Membership': memberDetails}
        return render(request, 'client/manage-account.html', context)

    except Membership.DoesNotExist:
        # Fallback if no membership exists
        form = UpdateUserForm(instance=request.user)

        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('client-dashboard')

        context = {'UpdateUserForm': form}
        return render(request, 'client/manage-account.html', context)
