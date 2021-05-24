from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    
    def post(self, request):
        data = request.data  # from frontend JSON data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                'token': token.key,
                'user_info': serializer.data,
                'status': status.HTTP_201_CREATED
            })
        else:
            return Response(serializer.errors)