from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Default user model extending ``AbstractUser``."""

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.username

