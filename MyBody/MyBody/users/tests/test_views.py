from django.test import TestCase
from django.urls import reverse


class UserViewsTests(TestCase):
    VALID_USER_DATA = {
        'email': 'emailTest@abv.bg',
        'username': 'martin',
        'password': '123asdQWE@#$%*&^%%$'
    }

    def test_login__view(self):
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'profile_views/login.html')

    def test_register__view(self):
        response = self.client.get(reverse('register'))

        self.assertTemplateUsed(response, 'profile_views/register_user.html')

    def test_logout__view(self):
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.url, '/')



    # def test_register_user_with_correct_data(self):
    #     response = self.client.post(reverse('register'), data={
    #         'email': self.VALID_USER_DATA['email'],
    #         'username': self.VALID_USER_DATA['username'],
    #         'password1': self.VALID_USER_DATA['password'],
    #         'password2': self.VALID_USER_DATA['password']
    #     })
    #
    #     self.assertEqual(response.status_code, 200)

