import uuid

from django.db import models

from products.models import Product
from users.models import Address, User
from wiwoapp.utils import generate_order_id


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING_PAYMENT = 'pending_payment', 'Pending Payment'
        PAID = 'paid', 'Paid'
        PENDING = 'pending', 'Pending'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
        RETURNED = 'returned', 'Returned'

    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        FAILED = 'failed', 'Failed'
        COMPLETED = 'completed', 'Completed'
        REVERSED = 'reversed', 'Reversed'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField(max_length=250, unique=True, default=generate_order_id)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='orders', null=True,  blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='orders')
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING_PAYMENT)
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )
    payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.order_id} by User {self.user.id}" if self.user else f"Order {self.order_id}"


class OrderItem(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SHIPPED = 'shipped', 'Shipped'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'
        RETURNED = 'returned', 'Returned'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='items')
    product_name = models.CharField(max_length=255,null=True, blank=True)
    product_image = models.URLField(max_length=255, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    confirmed_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.quantity} order for {self.product.name}" if self.product else f"{self.quantity} order for {self.product_name}"
