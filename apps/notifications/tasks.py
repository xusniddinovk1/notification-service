from django.utils import timezone
from celery import Task

from apps.notifications.senders.base import BaseSender
from apps.notifications.senders.email import EmailSender
from apps.notifications.senders.in_app import InAPPSender
from apps.notifications.senders.sms import SMSSender
from config.celery import app
from apps.notifications.models import Notification

SENDER: dict[str, type[BaseSender]] = {
    "EMAIL": EmailSender,
    "SMS": SMSSender,
    "IN_APP": InAPPSender,
}

@app.task(bind=True, max_retries=3)
def send_notification_task(self: Task, notification_id: int) -> None:
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        print(f"Notification with ID {notification_id} does not exist.")
        return

    try:
        channel_type = notification.template.channel.channel

        sender = SENDER.get(channel_type)
        if not sender:
            raise ValueError(f"Unknown channel: {channel_type}")

        sender().send(notification)

        notification.status = Notification.STATUS.SENT
        notification.sent_at = timezone.now()
        notification.save()

    except Exception as exc:
        notification.status = Notification.STATUS.FAILED
        notification.save()

        raise self.retry(exc=exc, countdown=2**self.request.retries)
