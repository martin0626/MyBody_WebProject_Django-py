from django.urls import path
from MyBody.home.views import HomeView, DetailsArticleType

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('info/type/<int:pk>', DetailsArticleType.as_view(), name='article info'),
]
