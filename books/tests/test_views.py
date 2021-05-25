import json
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

class BooksViewTestCases(APITestCase):
    def setUp(self):
        register_url = reverse('users:register')
        user_data = {
            'username':'ben',
            'email':'test@email.com',
            'password1':'testpass1',
            'password2':'testpass1'
        }
        reversed_url = reverse('create-category')
        response = self.client.post(reversed_url, data={'category_name':'Thriller'})
        self.category = json.loads(response.content.decode('utf-8'))

        res = self.client.post(register_url, user_data, format='json')
        user = User.objects.get(username='ben')
        self.client.force_authenticate(user=user)

        return super().setUp()

    def test_book_create_view(self):
        data = {
            "book_name": "TestBook",
            "published_date": date.today(),
            "authors": ["Chetan Bhagat","Edward"],
            "categories": ["Fiction","Romantic"]
        }
        url = reverse('test-create-book')
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 201)

        print('TEST BOOK MODEL CREATED VIA VIEW')