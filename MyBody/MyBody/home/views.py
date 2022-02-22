from django.shortcuts import render

from MyBody.home.models import ArticleTypes


def home_view(request):
    article_types = ArticleTypes.objects.all()
    context = {
        'article_types': article_types,
    }
    return render(request, 'index.html', context)


def details_article_type(request, pk):
    type_article = ArticleTypes.objects.get(pk=pk)
    context = {
        'type_article': type_article,

    }

    return render(request, 'home_views/article_type_details.html', context)
