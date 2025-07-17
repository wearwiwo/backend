
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2) #Price in Kobo
    stock = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    default_image = models.CharField(max_length=1024, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete method to set is_active to False instead of deleting."""
        self.is_active = False
        self.is_deleted = False
        self.name = f"{self.name} (deleted)"
        self.save(update_fields=['is_active','is_deleted', 'name', 'updated_at'])

    def unpublish(self):
        """Set the product as inactive without deleting it."""
        self.is_active = False
        self.name = f"{self.name} (unpublished)"
        self.save(update_fields=['is_active', 'updated_at'])

    def publish(self):
        """Set the product as active."""
        self.is_active = True
        self.name = self.name.replace(" (unpublished)", "").replace(" (deleted)", "")
        self.save(update_fields=['is_active', 'updated_at'])

    @property
    def in_stock(self):
        """Check if the product is in stock."""
        return self.stock > 0

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(Product)


    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductImage(models.Model):
    url = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"Image for {self.product.name}" if self.product else "Image without product"


