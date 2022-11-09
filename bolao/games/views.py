from django.shortcuts import render
from .models import Games
import datetime

def games(request):
    if request.method == "GET":
        all_entries = Games.objects.all()
        instance = Games.objects.values()
        #print(instance)
        return render(request, 'games/games.html',
        context= {"jogos":all_entries})
