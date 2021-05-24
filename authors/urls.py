from . import views
from django.urls import path

app_name = 'author_app'

urlpatterns = [
    path('get/', views.AuthorsListView.as_view(), name='authors'),
    path('create/', views.CreateAuthorView.as_view(), name='create_author'),
    path('analytics/<str:category_id>/', views.GetAuthorsAnalyticsView.as_view(), name='author_analytics'),
]