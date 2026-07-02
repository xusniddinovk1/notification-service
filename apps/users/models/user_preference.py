from django.db import models
from .users import User
from apps.nchannels.models import NotificationChannel


class Preference(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="preference"
    )
    channel = models.ForeignKey(
        NotificationChannel,
        on_delete=models.CASCADE,
        related_name="preference"
    )
    is_enabled = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "channel")
