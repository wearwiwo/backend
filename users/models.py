import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user."""
        if not email:
            raise ValueError('Please provide an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and stores a new superuser."""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deactivated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    ACTIVITY_LOG_OBJECT_NAME_FIELD = 'email'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def default_address(self):
        queryset = self.addresses.all().values_list('owner__id', flat=True)
        return queryset

    class Meta:
        verbose_name = 'User'
        app_label = 'users'

    def __str__(self):
        return self.full_name


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.state}, {self.country}'

    def set_default_address(self):
        """Set this address as the default for the user."""

        # Unset any existing default address for the user
        Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        # Set this address as the default
        self.is_default = True
        self.save()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
