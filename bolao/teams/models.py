from django.db import models

class Teams(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name_plural = "Times"
