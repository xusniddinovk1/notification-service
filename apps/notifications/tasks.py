from config.celery import app
from apps.notifications.models import Notification
from jinja2 import Template
from django.utils import timezone


@app.task(bind=True, max_retries=3)
def send_notification_task(self, notification_id: int):
    try:
        notification = Notification.objects.get(id=notification_id)
        content = notification.template.content
        rendered = Template(content).render(**notification.payload)

        channel_type = notification.template.channel.channel
        if channel_type == "EMAIL":
            print(f"EMAIL {rendered}")
        elif channel_type == "SMS":
            print(f"SMS {rendered}")
        elif channel_type == "IN_APP":
            print(f"IN_APP {rendered}")

        notification.status = Notification.STATUS.SENT
        notification.sent_at = timezone.now()
        notification.save()

    except Exception as exc:
        notification.status = Notification.STATUS.FAILED
        notification.save()
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)
