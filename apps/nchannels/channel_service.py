from django.db.models import QuerySet
from django.http import Http404
from django.core.cache import cache
from .channel_repository import NotificationChannelRepository
from apps.nchannels.models import NotificationChannel


class NotificationChannelService:
    def __init__(
        self,
        repo: NotificationChannelRepository,
    ) -> None:
        self.repo = repo

    def list_channels(self) -> QuerySet[NotificationChannel]:
        cached = cache.get("channels_list")
        if cached:
            return cached
        channels = self.repo.get_all_channel()
        cache.set("channels_list", channels, timeout=300)
        return channels

    def get_channel(self, channel_id: int) -> NotificationChannel:
        channel = self.repo.get_channel_by_id(channel_id)
        if not channel:
            raise Http404("Channel not found")
        return channel

    def create_channel(self, channel_data: NotificationChannel) -> NotificationChannel:
        self.repo.create_channel(channel_data)
        cache.delete("channels_list")
        return channel_data

    def update_channel(
        self, channel_id: int, channel_data: NotificationChannel
    ) -> NotificationChannel:
        channel = self.repo.get_channel_by_id(channel_id)
        if not channel:
            raise Http404("Channel not found")
        self.repo.update_channel(channel_data)
        cache.delete("channels_list")
        return channel_data

    def delete_channel(self, channel_id: int) -> None:
        channel = self.repo.get_channel_by_id(channel_id)
        if not channel:
            raise Http404("Channel not found")
        self.repo.delete_channel(channel_id)
        cache.delete("channels_list")
