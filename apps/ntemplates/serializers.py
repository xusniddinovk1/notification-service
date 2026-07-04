from rest_framework import serializers

from apps.ntemplates.models import NotificationTemplate


class TemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ["id", "title", "subject", "content", "channel", "is_active", "created_at"]
        read_only_fields = ["id", "created_at"]
