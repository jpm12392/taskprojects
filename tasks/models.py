from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from .managers import CustomUserManager


## User Custom Models
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()


## Task Model.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    due_date = models.DateField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
