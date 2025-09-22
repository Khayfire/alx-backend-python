from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    # Example of explicit CharField
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bio"]


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ["id", "sender", "sender_username", "content", "timestamp", "conversation"]

    def get_sender_username(self, obj):
        return obj.sender.username


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    title = serializers.CharField(required=True)

    class Meta:
        model = Conversation
        fields = ["id", "title", "participants", "messages"]

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Conversation title must be at least 3 characters long.")
        return value
