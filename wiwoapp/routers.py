from rest_framework.routers import SimpleRouter

from users.urls import user_router

v1_router = SimpleRouter()
v1_router.registry.extend(user_router.registry)
