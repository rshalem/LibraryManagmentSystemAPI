from rest_framework import serializers

from .models import Books
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Books
        fields = ('id', 'book_name', 'published_date', 'authors', 'categories')