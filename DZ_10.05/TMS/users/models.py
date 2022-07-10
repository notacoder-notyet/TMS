from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email