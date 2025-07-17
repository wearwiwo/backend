from rest_framework import serializers

from products.models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serializer for product images.
    """

    class Meta:
        model = ProductImage
        fields = ['id', 'url']
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for product categories.
    """

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for adding an address to a user.
    """

    images = ProductImageSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    default_image = ProductImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'images',
            'categories',
            'name',
            'slug',
            'description',
            'price',
            'stock',
            'default_image',
            'is_active',
            'categories',
        ]
        read_only_fields = ['id', 'slug', 'is_active', 'created_at', 'updated_at', 'is_deleted']
