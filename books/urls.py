from . import views
from django.urls import path

urlpatterns = [
    path('get/', views.BooksListView.as_view(), name='books'),
    path('create/', views.CreateBookView.as_view(), name='create-book'),
    path('analytics/<str:category_id>/', views.GetBooksAnalyticsView.as_view(), name='book_analytics')
]
