from django.db import models
from apps.nchannels.models import NotificationChannel

class NotificationTemplate(models.Model):
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    channel = models.ForeignKey(
        NotificationChannel,
        on_delete=models.CASCADE,
        related_name="notification_templates"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
