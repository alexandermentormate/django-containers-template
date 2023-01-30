from rest_framework import viewsets

from apps.core.serializers import UserSerializer
from apps.core.services import get_all_users


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_all_users()
