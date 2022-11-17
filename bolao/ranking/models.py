from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ranking(models.Model):
    fk_userId = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.PositiveSmallIntegerField()
    correct_results = models.PositiveSmallIntegerField()
    correct_winner =  models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.fk_userId} - {self.pontuacao}"

    class Meta:
        verbose_name_plural = "Ranking"
