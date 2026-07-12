from rest_framework.throttling import UserRateThrottle


class SendNotificationThrottle(UserRateThrottle):
    scope = "send"


class BulkSendThrottle(UserRateThrottle):
    scope = "bulk_send"