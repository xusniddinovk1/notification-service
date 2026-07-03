from django.urls import path
from .views import ChannelListAPIView, ChannelDetailAPIView

urlpatterns = [
    path("", ChannelListAPIView.as_view(), name="channel_list"),
    path("<int:channel_id>/", ChannelDetailAPIView.as_view(), name="channel_detail"),
]