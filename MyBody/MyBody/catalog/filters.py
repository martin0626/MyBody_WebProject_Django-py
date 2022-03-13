from django import forms
from django.db import models
from django_filters import FilterSet, CharFilter
from MyBody.catalog.forms import BootsTrapMixin
from MyBody.catalog.models import Article


class ArticleTypeFilter(FilterSet):

    class Meta:
        model = Article
        fields = {
            'title': ['contains'],
        }

        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
            },
            'extra': lambda f: {
                'widget': 'class: form-control'
            }
        }
