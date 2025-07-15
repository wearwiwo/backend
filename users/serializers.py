from rest_framework import serializers

from .models import Address, User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for a User model.
    """
    # address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id',  'email', 'first_name', 'last_name', 'phone_number', 'default_address']
        read_only_fields = ['id']


class AddressSerializer(serializers.Serializer):
    """
    Serializer for adding an address to a user.
    """
    class Meta:
        model = Address
        fields = [
            'street_address',
            'city',
            'is_default',
            'state',
            'country'
        ]
        read_only_fields = ['id']
