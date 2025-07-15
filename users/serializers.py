from rest_framework import serializers

from .models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for adding an address to a user.
    """

    class Meta:
        model = Address
        fields = ['id', 'user', 'street_address', 'city', 'is_default', 'state', 'country']
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for a User model.
    """

    default_address = AddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'default_address', 'full_name']
        read_only_fields = ['id', 'full_name']
