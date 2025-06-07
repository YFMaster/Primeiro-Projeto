from django.conf import settings
from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    deadline = models.DateField(null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "contest")

    def __str__(self) -> str:  # pragma: no cover - simple
        return f"{self.user} -> {self.contest}"
