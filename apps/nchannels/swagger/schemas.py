from ..channel_serializer import NotificationChannelSerializer
from drf_spectacular.utils import extend_schema

list_channel_schema = extend_schema(
    summary='List of all channels',
    description='List of all channels',
    responses={
        200: NotificationChannelSerializer(many=True),
    },
    tags=['channels']
)

get_channel_schema = extend_schema(
    summary='Get a channel',
    description='Get a channel by its id',
    responses={200: NotificationChannelSerializer()},
    tags=['channels']

)
create_channel_schema = extend_schema(
    summary='Create a new channel',
    description='Create a new channel',
    request=NotificationChannelSerializer,
    responses={201: NotificationChannelSerializer()},
    tags=['channels']
)

update_channel_by_id_schema = extend_schema(
    summary='Update a channel',
    description='Update a channel by its id',
    request=NotificationChannelSerializer,
    responses={200: NotificationChannelSerializer()},
    tags=['channels']
)

delete_channel_by_id_schema = extend_schema(
    summary='Delete a channel',
    description='Delete a channel by its id',
    responses={204: None},
    tags=['channels']
)
