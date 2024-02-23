# Enhancer/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    interest = models.CharField(max_length=100)  # Example field definition

    def __str__(self):
        return self.username
    # Provide unique related names for groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'  # Unique related name for groups field
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'  # Unique related name for user_permissions field
    )
