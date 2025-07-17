from rest_framework.routers import SimpleRouter

from orders.views import OrdersViewSet

orders_router = SimpleRouter()
orders_router.register("orders", OrdersViewSet, basename="orders")
