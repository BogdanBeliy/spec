from django.urls import path, include
from rest_framework.authtoken import views

from account.views import UserAPIViewset

urlpatterns = [
    path('auth/', views.obtain_auth_token),
    path('create/', UserAPIViewset.as_view({'post': 'create'}))
    # path('detail/')
    # path('delete/')
]