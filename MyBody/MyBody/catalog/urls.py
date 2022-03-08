from django.urls import path

from MyBody.catalog.views import delete_article, edit_article, details_article, \
    like_article, CreateArticle, CatalogView, UnauthorizedView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    path('create/', CreateArticle.as_view(), name='create article'),
    path('details/<int:pk>', details_article, name='details article'),
    path('like/<int:pk>', like_article, name='like'),
    path('unauthorized/', UnauthorizedView.as_view(), name='unauthorized view'),
]
