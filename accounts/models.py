from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    username = None
    
    email = models.EmailField(
        unique=True
    )
    
    display_name = models.CharField(
        max_length=50,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.display_name
    
    
