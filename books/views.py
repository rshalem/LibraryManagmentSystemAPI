from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authors.models import Authors
from .models import Books
from .serializers import BookSerializer
from categories.models import Categories

class BooksListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = Books.objects.all()
            serializer = BookSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)

class CreateBookView(APIView):
    def post(self, request):
        data = request.data
        authors_associated = data['authors']
        categories_associated = data['categories']
        try:
            book_name = data.get('book_name','')
            authors_queryset = Authors.objects.filter(author_name__in=authors_associated)
            categories_queryset = Categories.objects.filter(category_name__in=categories_associated)

            if len(authors_associated) != len(authors_queryset):
                message = {
                    'authors': 'Invalid author name to be associated with'
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
            if len(categories_associated) != len(categories_queryset):
                message = {
                    'category': 'Invalid category name to be associated with'
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
            if not book_name:
                message = {
                    'book_name': 'Cannot be empty'
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            
            book = Books.objects.create(
                book_name = book_name
            )
            # adding m2m
            for author in authors_queryset:
                book.authors.add(author)
            for category in categories_queryset:
                book.categories.add(category)
            
            book.save()
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def test_create_book(request):
    """test fnc"""
    data = request.data
    authors_associated = data['authors']
    categories_associated = data['categories']

    book_name = data.get('book_name','')
    authors_queryset = Authors.objects.filter(author_name__in=authors_associated)
    categories_queryset = Categories.objects.filter(category_name__in=categories_associated)  

    book = Books.objects.create(
        book_name = book_name
    )
    # adding m2m
    for author in authors_queryset:
        book.authors.add(author)
    for category in categories_queryset:
        book.categories.add(category)
    
    book.save()
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

