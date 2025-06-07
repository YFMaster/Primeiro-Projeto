from django.db import migrations


def create_schedule(apps, schema_editor):
    CrontabSchedule = apps.get_model("django_celery_beat", "CrontabSchedule")
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")
    schedule, _ = CrontabSchedule.objects.get_or_create(minute="0", hour="*/6")
    PeriodicTask.objects.get_or_create(
        name="Fetch contests every 6 hours",
        task="apps.core.tasks.fetch_contests",
        crontab=schedule,
    )


def delete_schedule(apps, schema_editor):
    PeriodicTask = apps.get_model("django_celery_beat", "PeriodicTask")
    try:
        task = PeriodicTask.objects.get(task="apps.core.tasks.fetch_contests")
        schedule = task.crontab
        task.delete()
        if schedule and not PeriodicTask.objects.filter(crontab=schedule).exists():
            schedule.delete()
    except PeriodicTask.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("django_celery_beat", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_schedule, delete_schedule)]
