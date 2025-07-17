from rest_framework import viewsets

from products.models import Category, Product, ProductImage
from products.serializers import CategorySerializer, ProductImageSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
