import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
app = Celery("mydjangoapp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
app.conf.beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"
app.autodiscover_tasks()
