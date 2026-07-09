from typing import ClassVar

from rest_framework import serializers
from .models import NotificationChannel


class NotificationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationChannel
        fields: ClassVar[list[str]] = ["id", "channel", "is_active", "created_at"]
        read_only_fields: ClassVar[list[str]] = ["id", "created_at"]
