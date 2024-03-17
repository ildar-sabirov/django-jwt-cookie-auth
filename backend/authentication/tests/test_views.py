from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/signup/'
        self.login_url = '/auth/login/'
        self.logout_url = '/auth/logout/'
        self.user_data = {
            'username': 'test_user',
            'password': 'test_password'
        }

    def test_register_view(self):
        response = self.client.post(
            self.register_url, self.user_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_login_view(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(
            self.login_url, self.user_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('jwt' in response.cookies)

    def test_logout_view(self):
        self.client.post(self.register_url, self.user_data, format='json')
        self.client.post(self.login_url, self.user_data, format='json')
        response = self.client.post(self.logout_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookies_dict = {}
        for key, morsel in response.cookies.items():
            cookies_dict[key] = morsel.value
        self.assertEqual(cookies_dict.get('jwt'), '')
