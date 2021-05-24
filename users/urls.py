from . import views
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),

    # getting auth token upon login with correct user and pass
    path('login/', obtain_auth_token, name='login')
]