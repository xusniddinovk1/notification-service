from django.conf import settings
from django.core.mail import send_mail

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
            print(f"Sending email to: {notification.user.email}")
            print(f"Subject: {notification.template.subject}")
            print(f"Content: {rendered}")
            send_mail(
                subject=notification.template.subject,
                message=rendered,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[notification.user.email],
                fail_silently=False,
            )
            print("Email sent successfully!")
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
