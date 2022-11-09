from django.db import models

class Teams(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Times"
