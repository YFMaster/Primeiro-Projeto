from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Contest
from .tasks import send_update_email


@receiver(post_save, sender=Contest)
def notify_favorite_update(sender, instance, created, **kwargs):
    if not created:
        send_update_email.delay(instance.id)
