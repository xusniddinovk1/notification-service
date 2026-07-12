from django.urls import path

from apps.notifications.views.notification import (
    NotificationListView,
    NotificationSendView,
    NotificationDetailView,
    NotificationStatsView,
)
from apps.notifications.views.bulk_notification import BulkSendNotificationView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification-list"),
    path(
        "<int:notification_id>/",
        NotificationDetailView.as_view(),
        name="notification-detail",
    ),
    path("send/", NotificationSendView.as_view(), name="notification-send"),
    path("bulk-send/", BulkSendNotificationView.as_view(), name="notification-bulk-send"),
    path("stats/", NotificationStatsView.as_view(), name="notification-stats"),
]
