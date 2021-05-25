from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class UserTokenGenerationTestCases(APITestCase):
    url = reverse('author_app:authors')

    def setUp(self):
        self.user = User.objects.create(
            username='test', 
            email='test@gmail.com',
            password='testpass1'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        """ authenticating with Token credentials"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_token_creation(self):
        self.assertIsNot(self.token.key, '')
        print('TOKEN GENERATED TEST PASSED')

    def test_author_list_with_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('TEST AUTHOR LIST WITH AUTHENTICATION WORKED')

    def test_author_list_with_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print('TEST AUTHOR LIST WITH UN AUTHENTICATION WORKED')
    