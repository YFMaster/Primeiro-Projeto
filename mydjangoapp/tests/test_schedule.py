from django.conf import settings
from django.test import TestCase
from celery.schedules import crontab


class BeatConfigTest(TestCase):
    def test_fetch_contests_task_is_scheduled(self):
        schedule = settings.CELERY_BEAT_SCHEDULE['fetch-contests-every-6-hours']
        assert schedule['task'] == 'apps.core.tasks.fetch_contests'
        assert schedule['schedule'] == crontab(minute=0, hour='*/6')
