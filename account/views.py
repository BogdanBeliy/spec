from rest_framework import status, permissions, response, viewsets
from account.models import UserModel, PersonalArea
from account.permissions import CreateAccountPermission
from account.serializers import UserSerializer, RegistrationUserSerializer, PersonalAreaSerializer
from rest_framework.decorators import action, permission_classes


class UserAPIViewset(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


user_create = UserAPIViewset.as_view({'post': 'create'})
user_detail = UserAPIViewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})
user_delete = UserAPIViewset.as_view({'delete': 'destroy'})


class PersonalAreaAPIViewset(viewsets.ModelViewSet):
    queryset = PersonalArea.objects.all()
    serializer_class = PersonalAreaSerializer
