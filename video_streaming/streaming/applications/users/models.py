from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField("Nombre completo", max_length=50, blank=True)
    age = models.PositiveIntegerField(verbose_name="Edad", blank=True, null=True)
    code_register = models.CharField(max_length=6, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"


    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def __str__(self):
        return f"{self.email} {self.full_name}"
