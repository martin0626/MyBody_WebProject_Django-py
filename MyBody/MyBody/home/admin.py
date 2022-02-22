from django.contrib import admin

from MyBody.home.models import ArticleTypes


@admin.register(ArticleTypes)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
