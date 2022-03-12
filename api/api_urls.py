from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('account/', include('account.urls')),
    path('token/', include('djoser.urls.jwt')),
    path('reg/', include('djoser.urls')),
]