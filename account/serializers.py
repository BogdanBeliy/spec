from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers, status
from account.models import UserModel, PersonalArea


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions']


class RegistrationUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ('email', 'password')


class PersonalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalArea
        fields = '__all__'
