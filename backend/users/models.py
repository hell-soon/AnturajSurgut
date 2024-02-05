from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The Phone number must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')

    USERNAME_FIELD = 'phone'
    objects = CustomUserManager()

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.phone
