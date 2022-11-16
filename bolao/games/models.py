from django.db import models
from teams.models import Teams
from django.contrib.auth.models import User

class Games(models.Model):
    teamId_1 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name="teamId_1")
    teamId_2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="teamId_2")
    date = models.DateField()

    def __str__(self):
        return f"ID: {self.id} - {self.teamId_1} x  {self.teamId_2}"

    class Meta:
        verbose_name_plural = "Jogos"

class Bets(models.Model):
    fk_userId = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_gameId = models.ForeignKey(Games, on_delete=models.CASCADE)
    team1_score = models.PositiveSmallIntegerField()
    team2_score = models.PositiveSmallIntegerField()  

    def __str__(self):
        return f"{self.fk_userId} - {self.fk_gameId} - {self.team1_score} x  {self.team2_score}"

    class Meta:
        verbose_name_plural = "Apostas"


class Results(models.Model):
    fk_gameId = models.ForeignKey(Games, on_delete=models.CASCADE)
    team1_score = models.PositiveSmallIntegerField()
    team2_score = models.PositiveSmallIntegerField()  

    def __str__(self):
        return f"{self.fk_gameId} - {self.team1_score} x  {self.team2_score}"

    class Meta:
        verbose_name_plural = "Resultados"

