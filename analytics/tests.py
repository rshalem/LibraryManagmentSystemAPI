from categories.models import Categories
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate
from rest_framework.test import APITestCase

class AnalyticsViewTestCases(APITestCase):
    def setUp(self):
        url = reverse('users:register')
        data = {
            'username':'test',
            'email':'test@gmail.com', 
            'password1':'test@123',
            'password2':'test@123'
        }
        self.client = APIClient()
        response = self.client.post(url, data, format='json')
        self.category = Categories.objects.create(category_name='Fiction')

    def test_get_authors_via_category_id_analytics_view(self):
        print(self.category.category_name)
        url_path = reverse('author_analytics')
        response = self.client.get(url_path, args=self.category.category_name)
        self.assertEqual(response.status_code, 200)

    def test_get_books_via_category_id_analytics_view(self):
        pass