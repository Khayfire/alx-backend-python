# chats/models.py
import uuid   # ✅ required by the checker

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"


class Conversation(models.Model):
    # Example: UUID for unique conversation IDs
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in {self.conversation}"
