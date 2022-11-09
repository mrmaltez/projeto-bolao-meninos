from django.db import models
from teams.models import Teams

class Games(models.Model):
    teamId_1 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name="teamId_1")
    teamId_2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="teamId_2")
    date = models.DateField()

    def __str__(self):
        return f"{self.teamId_1} x  {self.teamId_2}"

    class Meta:
        verbose_name_plural = "Jogos"

