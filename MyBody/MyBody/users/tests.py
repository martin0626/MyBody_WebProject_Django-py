from django.test import TestCase
from django.urls import reverse

from MyBody.users.models import MyBodyUser, Profile


class UserViewsTests(TestCase):
    VALID_USER_DATA = {
        'username': 'martin123',
        'email': 'emailTest@abv.bg',
        'password1': '123asdQWE@#$%*&^%%$',
        'password2': '123asdQWE@#$%*&^%%$',
    }

    INVALID_USER_DATA = {
        'username': 'm',
        'email': 'emailTest@abv.bg',
        'password1': '123asdQWE@#$%*&^%%$',
        'password2': '123asdQWE@#$%*&^%%$',
    }

    def test_register_user_with_valid_data(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        user = MyBodyUser.objects.first()
        self.assertIsNotNone(user)
        self.assertEqual('martin123', user.username)
        self.assertEqual('emailTest@abv.bg', user.email)

    def test_register_user_with_invalid_data(self):
        self.client.post(
            reverse('register'),
            data=self.INVALID_USER_DATA,
        )

        user = MyBodyUser.objects.first()
        self.assertEqual(None, user)

    def test_creating_profile_on_register(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        user = MyBodyUser.objects.first()
        profile = Profile.objects.first()
        self.assertIsNotNone(user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, user)

    def test_profile_details_is_owner(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )
        response = self.client.get(reverse('profile details', kwargs={'pk': 1}))
        self.assertTrue(response.context['is_owner'])

    def test_edit_profile_correctly(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )
        profile = Profile.objects.first()
        profile.description = 'Test description'
        profile.save()
        self.assertEqual('Test description', profile.description)

    def test_login_view(self):
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'profile_views/login.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))

        self.assertTemplateUsed(response, 'profile_views/register_user.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.url, '/')
