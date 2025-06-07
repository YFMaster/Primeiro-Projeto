from django.test import TestCase
from django_celery_beat.models import PeriodicTask


class BeatScheduleTest(TestCase):
    def test_fetch_contests_task_scheduled(self):
        assert PeriodicTask.objects.filter(
            task="apps.core.tasks.fetch_contests"
        ).exists()
