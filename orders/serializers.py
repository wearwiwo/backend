from rest_framework import serializers

from orders.models import Order, OrderItem
from products.serializers import ProductSerializer
from users.serializers import AddressSerializer, UserSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for order items.
    """

    product = ProductSerializer(many=False)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'product_image',
            'product_description',
            'confirmed_price',
            'quantity',
            'status',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for order details.
    """

    user = UserSerializer(many=False, read_only=True)
    address = AddressSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        """
        Calculate the total amount for the order.
        """
        if obj.status != Order.Status.PAID:
            # Return current product prices if not paid
            return sum(item.product.price * item.quantity for item in obj.items.all())

        # Return confirmed prices if the order is paid
        return sum(item.confirmed_price * item.quantity for item in obj.items.all())

    class Meta:
        model = Order
        fields = [
            'id',
            'order_id',
            'user',
            'address',
            'status',
            'payment_status',
            'payment_intent_id',
            'total_amount',
            'items',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'order_id']
