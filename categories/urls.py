from . import views
from django.urls import path

urlpatterns = [
    path('get/', views.CategoryListView.as_view(), name='categories'),
    path('create/', views.CreateCategoryView.as_view(), name='create-category'),
]
