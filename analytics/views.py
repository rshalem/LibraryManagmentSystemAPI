from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Categories

# Create your views here.
class GetAuthorsAnalyticsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category_name):
        try:
            category = Categories.objects.get(category_name__iexact=category_name)
            author_ids = category.books_set.values_list('authors', flat=True).distinct().count()
            return Response({'total_authors': author_ids}, status=status.HTTP_200_OK)
        except Exception:
            message = {
                'detail':'Category id doesn\'t exist'
            }
            return Response(message, status=status.HTTP_404_NOT_FOUND)

class GetBooksAnalyticsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category_name):
        try:
            category = Categories.objects.get(category_name__iexact=category_name)
            books_count = category.books_set.all().count()
            return Response({'total_books': books_count}, status=status.HTTP_200_OK)
        except Exception:
            message = {
                'detail':'Category id doesn\'t exist'
            }
            return Response(message, status=status.HTTP_404_NOT_FOUND)