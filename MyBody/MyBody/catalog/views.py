import os
from os.path import join

from django.shortcuts import render, redirect

from MyBody import settings
from MyBody.catalog.forms import CreateForm, EditForm, DeleteArticleForm
from MyBody.catalog.models import Article, LikeArticle


def catalog_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'catalog.html', context)


def create_article(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            return redirect('catalog')
    else:
        form = CreateForm()

    context = {
        'form': form,
    }

    return render(request, 'create_catalog.html', context)


def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            return redirect('catalog')

    else:
        form = EditForm(initial=article.__dict__)

    context = {
        'form': form,
    }
    return render(request, 'edit_catalog.html', context)


def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('catalog')
    else:
        context = {
            'article': article
        }

    return render(request, 'delete_catalog.html', context)


def details_article(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user
    likes = len(LikeArticle.objects.filter(article_id=pk))

    context = {
        'article': article,
        'likes_count': likes,
    }

    if not user.is_anonymous:
        is_liked = len(list(LikeArticle.objects.filter(article=article, user=user))) > 0
        is_owner = article.owner == user
        context['is_liked'] = is_liked
        context['is_owner'] = is_owner

    return render(request, 'details_article.html', context)


def like_article(request, pk):
    article = Article.objects.get(pk=pk)
    user = request.user
    like = LikeArticle.objects.filter(article=article, user=user)

    if not like:
        like = LikeArticle(article_id=article.id, user=user)
        like.save()

    else:
        like.delete()

    return redirect('details article', pk)
