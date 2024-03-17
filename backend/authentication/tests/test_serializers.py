from django.contrib.auth import get_user_model
from django.test import TestCase
from ..serializers import UserSerializer

User = get_user_model()


class UserSerializerTest(TestCase):
    def setUp(self):
        self.validated_data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_create_user(self):
        serializer = UserSerializer(data=self.validated_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, self.validated_data['username'])
        self.assertEqual(user.email, self.validated_data['email'])
        self.assertEqual(user.first_name, self.validated_data['first_name'])
        self.assertEqual(user.last_name, self.validated_data['last_name'])
