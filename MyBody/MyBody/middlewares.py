from MyBody.catalog.models import Article


def last_viewed_articles_middleware(get_response):
    def middleware(request):
        viewed_articles_ids = request.session.get('viewed_articles_ids', [])
        articles = Article.objects.filter(id__in=viewed_articles_ids)
        request.viewed_articles_ids = articles
        return get_response(request)
    return middleware
