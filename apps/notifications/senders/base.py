from abc import ABC, abstractmethod

from apps.notifications.models import Notification


class BaseSender(ABC):
    @abstractmethod
    def send(self, notification: Notification) -> None:
        pass
