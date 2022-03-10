from django.urls import path
from MyBody.users.signals import user_created
from MyBody.users.views import profile_edit, profile_details, profile_delete, \
    UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/create', profile_edit, name='profile edit'),
    path('profile/register', UserRegistrationView.as_view(), name='register'),
    path('profile/logout', UserLogoutView.as_view(), name='logout'),
    path('prfile/details/<int:pk>', profile_details, name='profile details'),
    path('profile/delete', profile_delete, name='profile delete'),
]
