from .base import BaseSender
from ..models import Notification


class InAPPSender(BaseSender):
    def send(self, notification: Notification) -> None:
        pass
