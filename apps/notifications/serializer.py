from rest_framework import serializers

from apps.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "user", "template", "payload", "status", "created_at", "sent_at"]
        read_only_fields = ["id", "user", "status", "created_at", "sent_at"]


class SendNotificationSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()
    payload = serializers.JSONField()