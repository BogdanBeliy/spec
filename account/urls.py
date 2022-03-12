from django.urls import path, include
from account import views

urlpatterns = [
    path('register/', views.user_create),
    path('detail/<int:pk>/', views.user_detail, name='user_detail'),
    path('delete/<int:pk>/', views.user_delete, name='user_detail'),
]