from analytics import views
from django.urls import path

app_name = 'analytics_api'
urlpatterns = [
    path('authors/<str:category_name>/', views.GetAuthorsAnalyticsView.as_view(), name='author_analytics'),
    path('books/<str:category_name>/', views.GetBooksAnalyticsView.as_view(), name='book_analytics'),
]