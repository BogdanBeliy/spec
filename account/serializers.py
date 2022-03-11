from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers, status
from account.models import UserModel, PersonalArea


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        personal_area = PersonalArea.objects.create(user=user)
        return user


class PersonalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalArea
        fields = '__all__'
