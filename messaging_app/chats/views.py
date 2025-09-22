from rest_framework import viewsets, filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # Add filtering & searching
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "participants__username"]
    ordering_fields = ["id", "title"]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # Add filtering & searching
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["content", "sender__username"]
    ordering_fields = ["timestamp"]
