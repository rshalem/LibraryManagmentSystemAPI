from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from authors.models import Authors
from books.models import Books
from categories.models import Categories

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
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)  # authentication

        # dummy category, author, books instance setup
        self.author = Authors.objects.create(author_name='Raj',author_registered=timezone.now(),bio='Writer & Traveller')
        self.category = Categories.objects.create(category_name='Fiction')

        self.book = Books.objects.create(book_name='TestBookNow',published_date=date.today())  #book instance creation
        self.book.authors.add(self.author)
        self.book.categories.add(self.category)
        self.book.save()

        self.category_from_db = Categories.objects.get(category_name__iexact='Fiction')

    def test_get_authors_via_category_id_analytics_view(self):
        response = self.client.get(reverse('analytics_api:author_analytics', kwargs={'category_name':self.category_from_db.category_name}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('total_authors'), 1)
        print("AUTHOR ANALYTICS TEST PASSED")

    def test_get_books_via_category_id_analytics_view(self):
        response = self.client.get(reverse('analytics_api:book_analytics', kwargs={'category_name':self.category_from_db.category_name}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('total_books'), 1)
        self.assertEqual(self.book.book_name, 'TestBookNow')
        print("BOOK ANALYTICS TEST PASSED")