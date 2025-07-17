from rest_framework.routers import SimpleRouter

from products.urls import product_router
from users.urls import user_router

v1_router = SimpleRouter()
v1_router.registry.extend(user_router.registry)
v1_router.registry.extend(product_router.registry)
