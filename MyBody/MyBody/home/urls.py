from django.urls import path
from MyBody.home.views import home_view, details_article_type

urlpatterns = [
   path('', home_view, name='home'),
   path('info/type/<int:pk>', details_article_type, name='article info'),
]
