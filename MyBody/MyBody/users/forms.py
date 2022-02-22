from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


class LoginForm(BootsTrapMixin, AuthenticationForm):
    pass
