from django.db import models
from apps.ntemplates.models import NotificationTemplate
from apps.users.models import User


class Notification(models.Model):
    class STATUS(models.TextChoices):
        PENDING = "PENDING"
        SENT = "SENT"
        FAILED = "FAILED"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    template = models.ForeignKey(
        NotificationTemplate, on_delete=models.CASCADE, related_name="notifications"
    )
    payload = models.JSONField(default=dict)
    status = models.CharField(
        max_length=20, choices=STATUS.choices, default=STATUS.PENDING
    )
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.payload["title"]
