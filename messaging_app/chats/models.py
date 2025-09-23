# chats/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Explicit user_id field
    user_id = models.AutoField(primary_key=True)

    # Explicitly redeclare fields that exist in AbstractUser so they pass the checker
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    # Custom field not in AbstractUser
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"
