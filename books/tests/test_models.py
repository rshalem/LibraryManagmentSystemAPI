from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase

from authors.models import Authors
from books.models import Books
from categories.models import Categories

class BooksModelTestCases(APITestCase):
    def setUp(self):
        register_url = reverse('users:register')
        user_data = {
            'username':'ben',
            'email':'test@email.com',
            'password1':'testpass1',
            'password2':'testpass1'
        }
        response = self.client.post(register_url, user_data, format='json')
        user = User.objects.get(username='ben')
        self.client.force_authenticate(user=user)

        return super().setUp()
    
    def test_book_model_create(self):
        author1 = Authors.objects.create(
            author_name='testauthor',
            author_registered = timezone.now(),
            bio = 'Writer & Traveller'
            )
        
        author2 = Authors.objects.create(
            author_name='testauthor2',
            author_registered = timezone.now(),
            bio = 'Writers & Travellers'
            )
        
        cat1 = Categories.objects.create(
            category_name='testcategory1',
            )
        
        cat2 = Categories.objects.create(
            category_name='testcategory2',
            )

        data = {
            "book_name": "TestBook",
            "published_date": timezone.now(),
        }
        book = Books.objects.create(
            book_name=data['book_name'],
            published_date=data['published_date'],
        )
        book.authors.add(author1.id,author2.id)
        book.categories.add(cat1.id,cat2.id)
        book.save()
        self.assertEqual(book.book_name, 'TestBook')
        self.assertEqual(cat1.category_name, 'testcategory1')
        self.assertIsNot(cat2.category_name, 'testcategory1')
        print('TEST BOOK MODEL CREATED')