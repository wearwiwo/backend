from rest_framework.routers import SimpleRouter

from orders.urls import orders_router
from products.urls import products_router
from users.urls import user_router

v1_router = SimpleRouter()
v1_router.registry.extend(user_router.registry)
v1_router.registry.extend(products_router.registry)
v1_router.registry.extend(orders_router.registry)
