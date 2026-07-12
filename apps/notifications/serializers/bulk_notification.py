from rest_framework import serializers


class BulkSendNotificationSerializer(serializers.Serializer):
    user_ids = serializers.ListField(child=serializers.IntegerField())
    template_id = serializers.IntegerField()
    payload = serializers.JSONField()
