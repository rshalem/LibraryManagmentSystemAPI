from categories.models import Categories
from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Authors
from .serializers import AuthorSerializer

class AuthorsListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = Authors.objects.all()
            serializer = AuthorSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            message = {
                'detail':'Authors objects not found'
            }
            return Response(message, status=status.HTTP_204_NO_CONTENT)

class GetAuthorsAnalyticsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, category_id):
        try:
            category = Categories.objects.get(id=category_id)
            author_ids = category.books_set.values_list('authors', flat=True).distinct().count()
            return Response({'total_authors': author_ids})
        except Exception:
            message = {
                'detail':'Category id doesn\'t exist'
            }
            return Response(message, status=status.HTTP_404_NOT_FOUND)

class CreateAuthorView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)