from django.db import models


class NotificationChannel(models.Model):
    class Choices(models.TextChoices):
        SMS = 'SMS', 'SMS'
        EMAIL = 'EMAIL', 'Email'
        IN_APP = 'IN_APP', 'In App'

    channel = models.CharField(max_length=20, choices=Choices.choices, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.channel
