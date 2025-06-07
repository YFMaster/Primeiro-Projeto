from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)
    deadline = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    education_level = models.CharField(max_length=255, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.title
