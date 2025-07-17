from rest_framework.routers import SimpleRouter

from products.views import CategoryViewSet, ProductImagesViewSet, ProductViewSet

product_router = SimpleRouter()
product_router.register("products", ProductViewSet, basename="products")
product_router.register("images", ProductImagesViewSet, basename="images")
product_router.register("categories", CategoryViewSet, basename="categories")

