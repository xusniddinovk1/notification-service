from .base import BaseSender
from ..models import Notification


class SMSSender(BaseSender):
    def send(self, notification: Notification) -> None:
        pass
