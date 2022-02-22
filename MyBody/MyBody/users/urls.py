from django.urls import path
from MyBody.users.signals import user_created
from MyBody.users.views import login_view, profile_edit, register_view, logout_view, profile_details, profile_delete

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profile/create', profile_edit, name='profile edit'),
    path('profile/register', register_view, name='register'),
    path('profile/logout', logout_view, name='logout'),
    path('prfile/details/<int:pk>', profile_details, name='profile details'),
    path('profile/delete', profile_delete, name='profile delete'),
]
