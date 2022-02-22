from django.urls import path

from MyBody.catalog.views import catalog_view, delete_article, edit_article, create_article, details_article, \
    like_article

urlpatterns = [
    path('', catalog_view, name='catalog'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    path('create/', create_article, name='create article'),
    path('details/<int:pk>', details_article, name='details article'),
    path('like/<int:pk>', like_article, name='like'),
]
