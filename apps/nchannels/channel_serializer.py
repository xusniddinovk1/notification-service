from rest_framework import serializers
from .models import NotificationChannel


class NotificationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationChannel
        fields = ["id", "channel", "is_active", "created_at"]
        read_only_fields = ["id", "created_at"]
