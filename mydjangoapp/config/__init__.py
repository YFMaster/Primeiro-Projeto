# Permite que Celery descubra as configurações padrão
from .celery import app as celery_app  # noqa

__all__ = ("celery_app",)
