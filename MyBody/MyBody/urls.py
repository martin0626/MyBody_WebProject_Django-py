from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MyBody import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBody.home.urls')),
    path('user/', include('MyBody.users.urls')),
    path('catalog/', include('MyBody.catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
