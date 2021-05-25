from datetime import date, datetime
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from authors.models import Authors
from books.models import Books
from books.serializers import BookSerializer
from categories.models import Categories

class BooksViewTestCases(APITestCase):
    def setUp(self):
        # book obj creation
        self.author1 = Authors.objects.create(author_name='James',author_registered=datetime.today(),bio='Auth')
        self.author2 = Authors.objects.create(author_name='Ron',author_registered=datetime.today(),bio='Guitarist')
        self.cat1 = Categories.objects.create(category_name='Love')
        self.cat2 = Categories.objects.create(category_name='Dark')

        book = Books.objects.create(
            book_name = "TestsBook",
            published_date = date.today()
        )
        book.authors.add(self.author1.id)
        book.categories.add(self.cat1.id)
        book.save()

        # user registration
        register_url = reverse('users:register')
        user_data = {
            'username':'ben',
            'email':'test@email.com',
            'password1':'testpass1',
            'password2':'testpass1'
        }
        res = self.client.post(register_url, user_data, format='json')
        user = User.objects.get(username='ben')
        self.client.force_authenticate(user=user)

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

    def test_book_list_view(self):
        url = reverse('books')
        books = Books.objects.all()
        # get from db
        response = self.client.get(url)
        serializer = BookSerializer(books, many=True)
        
        self.assertEqual(response.status_code, 200)
        print('TEST GET ALL AUTHORS VIEW WORKED')
        self.assertEqual(response.data, serializer.data)
        print('TEST AUTHOR SERIALIZER WORKED')
        
        