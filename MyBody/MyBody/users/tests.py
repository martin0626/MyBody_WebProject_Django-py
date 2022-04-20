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

    def __register_user(self, credentials=None):
        if not credentials:
            credentials = self.VALID_USER_DATA

        self.client.post(
            reverse('register'),
            data=credentials,
        )
        return MyBodyUser.objects.first()

    def __create_user(self, user_data=None):
        self.USER_DATA = {
            'username': 'martin123',
            'email': 'emailTest@abv.bg',
            'password': '123asdQWE@#$%*&^%%$',
        }
        if not user_data:
            return MyBodyUser.objects.create_user(**self.USER_DATA)
        return MyBodyUser.objects.create_user(**user_data)

    def test_register_user_with_valid_data(self):
        user = self.__register_user()
        self.assertIsNotNone(user)
        self.assertEqual('martin123', user.username)
        self.assertEqual('emailTest@abv.bg', user.email)

    def test_register_user_with_invalid_data(self):
        user = self.__register_user(self.INVALID_USER_DATA)
        self.assertEqual(None, user)

    def test_creating_profile_on_register(self):
        user = self.__register_user()
        profile = Profile.objects.first()
        self.assertIsNotNone(user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, user)

    def test_profile_details_is_owner(self):
        user = self.__register_user()
        profile = Profile.objects.first()
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

        self.assertEqual(int(self.client.session['_auth_user_id']), profile.pk)

    def test_edit_profile_correctly(self):
        user = self.__register_user()
        profile = Profile.objects.first()
        profile.description = 'Test description'
        profile.save()
        self.assertEqual('Test description', profile.description)

    def test_login_user_on__login_view(self):
        user = self.__create_user()
        response = self.client.post(
            reverse('login'),
            data={'username': 'martin123', 'password': "123asdQWE@#$%*&^%%$"}
        )
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_edit_profile_with_owner_user(self):
        user = self.__register_user()
        response = self.client.post(
            reverse('profile edit', kwargs={'pk': user.pk}),
            data={'description': 'Test Test'}
        )
        profile = Profile.objects.first()
        self.assertEqual('Test Test', profile.description)

    def test_login_template(self):
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'profile_views/login.html')

    def test_register_template(self):
        response = self.client.get(reverse('register'))

        self.assertTemplateUsed(response, 'profile_views/register_user.html')

    def test_logout_template(self):
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.url, '/')

    def test_profile_details_template(self):
        user = self.__register_user()
        response = self.client.get(reverse('profile details', kwargs={'pk': user.pk}))
        self.assertTemplateUsed(response, 'profile_views/profile_details.html')

    def test_delete_profile_view(self):
        user = self.__register_user()
        response = self.client.post(reverse('profile delete'))
        self.assertEqual(None, Profile.objects.first())

    def test_change_password(self):
        user = self.__register_user()
        response = self.client.post(
            reverse('change password'),
            data={'old_password': '123asdQWE@#$%*&^%%$', 'new_password1': '123asdQWE@#', 'new_password2': '123asdQWE@#'}
        )
        self.client.logout()
        self.client.login(**{'username': 'martin123', 'password': '123asdQWE@#'})
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)
