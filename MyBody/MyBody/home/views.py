from django.shortcuts import render
from django.views.generic import ListView, DetailView

from MyBody.home.models import ArticleTypes


class HomeView(ListView):
    template_name = 'index.html'
    model = ArticleTypes
    context_object_name = 'article_types'
    ordering = ('title',)


class DetailsArticleType(DetailView):
    model = ArticleTypes
    template_name = 'home_views/article_type_details.html'
    context_object_name = 'type_article'

