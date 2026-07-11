from django.conf import settings
from django.core.mail import send_mail
from .base import BaseSender
from ..models import Notification
from jinja2 import Template


class EmailSender(BaseSender):

    def send(self, notification: Notification) -> None:
        rendered = Template(notification.template.content).render(**notification.payload)
        send_mail(
            subject=notification.template.subject or "No subject",
            message=rendered,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[notification.user.email],
            fail_silently=False,
        )
