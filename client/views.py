from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from creator.models import Article
from account.models import CustomUser

@login_required(login_url='my-login')
def client_dashboard(request):
    # Filter articles created by the logged-in user
    user_articles = Article.objects.filter(user=request.user)
    
    # Pass the articles to the template
    return render(request, 'client/client-dashboard.html', {'articles': user_articles})



@login_required(login_url='my-login')
def regular_articles(request):
    user = request.user
    articles = Article.objects.filter(pub_date__lte=timezone.now(), is_unlimited=False)
    
    context = {'AllClientArticles': articles}
    return render(request, 'client/regular-articles.html', context)


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