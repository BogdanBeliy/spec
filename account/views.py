from rest_framework import status, permissions, response, viewsets
from account.models import UserModel, PersonalArea
from account.serializers import UserSerializer, RegistrationUserSerializer


class UserAPIViewset(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = RegistrationUserSerializer


class PersonalAreaAPIViewset(viewsets.ModelViewSet):
    queryset = PersonalArea.objects.all()
    serializer_class = PersonalAreaSerializer
