from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from MyBody.catalog.models import Article, LikeArticle
from MyBody.users.forms import ProfileForm, RegisterForm, LoginForm
from MyBody.users.helpers import send_email_message
from MyBody.users.models import MyBodyUser, Profile


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'profile_views/login.html', context)


def profile_edit(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', profile.pk)
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
    }
    return render(request, 'profile_views/profile_create.html', context)


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            send_email_message(email, username)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'profile_views/register_user.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_details(request, pk):

    profile = Profile.objects.get(pk=pk)
    is_owner = request.user and request.user.id == profile.user_id
    user = MyBodyUser.objects.get(pk=pk)
    articles = Article.objects.filter(owner__profile=profile)
    likes = len(list(LikeArticle.objects.filter(article_id__in=articles)))
    context = {
        'user': user,
        'profile': profile,
        'articles': articles,
        'likes': likes,
        'is_owner': is_owner,
    }

    return render(request, 'profile_views/profile_details.html', context)


def profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'profile_views/delete_profile.html')
