from . import views
from django.urls import path

urlpatterns = [
    path('get/', views.BooksListView.as_view(), name='books'),
    path('create/', views.CreateBookView.as_view(), name='create-book'),
    path('test_create/', views.test_create_book, name='test-create-book'),
]
