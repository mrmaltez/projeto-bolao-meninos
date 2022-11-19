from django.shortcuts import render

from .models import Games, Bets
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib.auth import logout

@login_required(login_url="/auth/login/")
def games(request):
    # query user bets
    current_user = request.user 
    bets = Bets.objects.filter(fk_userId = current_user)
    all_entries_games = Games.objects.all()
    all_entries_game_values = Games.objects.values()
    if request.method == "GET":
        
        return render(request, 'games/games.html',
        context= {"jogos":all_entries_games,
        "bets":bets})
    else:
        if request.POST.get('logout') == 'logout':
            logout(request)
            return HttpResponseRedirect('/auth/login/')
        if request.POST.get('ranking') == 'ranking':
            return HttpResponseRedirect('/ranking')
        elif request.POST.get('submit'):
            # user
             
            for i in all_entries_game_values:
                try:
                    i = i["id"]
                    name_1 = f'jogo_{i}_time_1'
                    name_2 = f'jogo_{i}_time_2'
                    if Bets.objects.filter(fk_userId = current_user,
                        fk_gameId = Games(id=i)).exists():
                        update_saved = Bets.objects.get(fk_userId = current_user,
                        fk_gameId = Games(id=i))
                        update_saved.team1_score = request.POST.get(name_1)
                        update_saved.team2_score = request.POST.get(name_2)
                        update_saved.save()
                    else:
                        bet = Bets(fk_userId = current_user,
                        fk_gameId = Games(id=i),
                        team1_score = request.POST.get(name_1),
                        team2_score = request.POST.get(name_2))
                        bet.save()
                except:
                    print(f"Não foi possível salvar o jogo de id {i} na base")

            # # email = request.POST.get('email')
            # # password = request.POST.get('password')
            # print(results)
            bets = Bets.objects.filter(fk_userId = current_user)
            return render(request, 'games/games.html',
        context= {"fl_games":1,
        "bets":bets,
        "jogos":all_entries_games})
