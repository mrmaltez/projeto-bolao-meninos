from django.shortcuts import render

from .models import Games, Bets
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

@login_required(login_url="/auth/login/")
def games(request):
    if request.method == "GET":
        all_entries = Games.objects.all()
        return render(request, 'games/games.html',
        context= {"jogos":all_entries})
    else:
        if request.POST.get('logout') == 'logout':
            logout(request)
            return HttpResponseRedirect('/auth/login/')
        if request.POST.get('ranking') == 'ranking':
            return HttpResponseRedirect('/ranking')
        elif request.POST.get('submit'):
            # user
            current_user = request.user
            results = {}
            all_entries = Games.objects.values()
            # 
            for i in all_entries:
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
            return render(request, 'games/games.html',
        context= {"fl_games":1})
