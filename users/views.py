from django.contrib.auth import get_user_model
from rest_framework import viewsets

from users.serializers import AddressSerializer, UserSerializer

from .models import Address


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    User = get_user_model()
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
