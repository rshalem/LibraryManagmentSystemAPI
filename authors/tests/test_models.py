from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import force_authenticate
from rest_framework.test import APITestCase


class AuthorTestCases(APITestCase):
    def setUp(self):
        register_url = reverse('users:register')
        user_data = {
            'username':'ben',
            'email':'test@email.com',
            'password1':'testpass1',
            'password2':'testpass1'
        }
        # author
        self.author_create_url = reverse('author_app:create_author')
        self.author_data = {
            'author_name': 'testauthor',
            'date_registered': timezone.now(),
            'bio': 'Writer & Traveller'
        }
        response = self.client.post(register_url, user_data, format='json')
        self.assertEqual(response.status_code, 200)

        self.user = User.objects.get(username='ben')
        self.client.force_authenticate(user=self.user)   # force authenticate
        return super().setUp()


    def test_author_model_create(self):
        url = self.author_create_url
        data = self.author_data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        print('AUTHOR CREATED')
    
    def test_author_model_create_failing(self):
        url = self.author_create_url
        data = {'author_name':'','date_registered': timezone.now(), 'bio': 'Writer & Traveller' }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        print('AUTHOR CREATION FAILED TEST PASSED')