from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from MyBody.users.signals import user_created
from MyBody.users.views import profile_delete, \
    UserRegistrationView, UserLoginView, UserLogoutView, ChangePasswordView, ProfileDetails, ProfileEdit

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/create/<int:pk>', ProfileEdit.as_view(), name='profile edit'),
    path('profile/register', UserRegistrationView.as_view(), name='register'),
    path('profile/logout', UserLogoutView.as_view(), name='logout'),
    path('profile/details', ProfileDetails.as_view(), name='profile details'),
    path('profile/change_password', ChangePasswordView.as_view(), name='change password'),
    path('password_chnage_done/', RedirectView.as_view(url=reverse_lazy('home')), name='password_change_done'),
    path('profile/delete', profile_delete, name='profile delete'),
]
