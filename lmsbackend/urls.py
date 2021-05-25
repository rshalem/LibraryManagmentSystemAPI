from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authors/', include('authors.urls')),
    path('api/books/', include('books.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/users/', include('users.urls')),
    path('api/analytics/', include('analytics.urls')),
]
