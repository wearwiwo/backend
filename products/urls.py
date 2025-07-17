from rest_framework.routers import SimpleRouter

from products.views import CategoryViewSet, ProductImagesViewSet, ProductViewSet

products_router = SimpleRouter()
products_router.register("products", ProductViewSet, basename="products")
products_router.register("images", ProductImagesViewSet, basename="images")
products_router.register("categories", CategoryViewSet, basename="categories")

