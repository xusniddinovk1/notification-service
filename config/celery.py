import os
from celery import Celery

# Django settings ni Celery ga aytish
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    f'config.settings.{os.getenv("DJANGO_ENV")}'
)

app = Celery('notification_service')

# Celery konfiguratsiyasini Django settings dan olish (CELERY_ prefix bilan)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Barcha applardan task larni avtomatik topish
app.autodiscover_tasks()
