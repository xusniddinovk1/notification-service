from django.urls import path

from apps.notifications.views import NotificationListView, NotificationSendView, NotificationDetailView, \
    NotificationStatsView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notification-list"),
    path("<int:notification_id>/", NotificationDetailView.as_view(), name="notification-detail"),
    path("send/", NotificationSendView.as_view(), name="notification-send"),
    path("stats/", NotificationStatsView.as_view(), name="notification-stats"),
]
