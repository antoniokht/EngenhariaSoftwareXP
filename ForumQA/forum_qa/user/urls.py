from django.urls import path
from . import views
from .views import UserDetailView, UserDeleteView


urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
