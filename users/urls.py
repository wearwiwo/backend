from rest_framework.routers import SimpleRouter

from .views import AddressViewSet, UserViewSet

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename="users")
user_router.register("address", AddressViewSet, basename="address")
