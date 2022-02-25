from django.contrib import admin

from MyBody.catalog.models import Article, LikeArticle, CommentModel


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']


@admin.register(LikeArticle)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    pass
