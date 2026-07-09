from apps.nchannels.channel_repository import NotificationChannelRepository
from apps.nchannels.channel_service import NotificationChannelService


def get_channel_repository() -> NotificationChannelRepository:
    return NotificationChannelRepository()


def get_channel_service() -> NotificationChannelService:
    return NotificationChannelService(repo=get_channel_repository())
