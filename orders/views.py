from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
