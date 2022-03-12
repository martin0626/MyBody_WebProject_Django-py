from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.views.generic import FormView

from MyBody.catalog.forms import BootsTrapMixin
from MyBody.users.models import Profile, MyBodyUser

UserModel = get_user_model()


class ProfileForm(BootsTrapMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                }),
        }


class RegisterForm(BootsTrapMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )


class LoginForm(BootsTrapMixin, AuthenticationForm):
    pass


class ChangePassword(BootsTrapMixin, PasswordChangeForm):
    pass
