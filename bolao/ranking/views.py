from django.shortcuts import render

from games.models import Bets, Results
from .models import Ranking
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def ranking(request):
    if request.POST.get('ranking') == 'ranking':
        return HttpResponseRedirect('/games/jogos/')
    ranking_score = {}
    results = Results.objects.all()
    for result in results:
        gameId = result.fk_gameId
        result_team1 = result.team1_score
        result_team2 = result.team2_score
        if result_team1 > result_team2:
            winner = 'team1'
        elif result_team1 == result_team2:
            winner = 'draw'
        else:
            winner = 'team2'

        bets_game = Bets.objects.filter(fk_gameId = gameId)
        for bet in bets_game:
            userId = bet.fk_userId
            if userId not in ranking_score.keys():
                ranking_score[userId] = {'pontuacao':0,'correct_results':0,'correct_winner':0}
            bet_result_team1 = bet.team1_score
            bet_result_team2 = bet.team2_score
            if bet_result_team1 == result_team1 and bet_result_team2 == result_team2:
                ranking_score[userId]['pontuacao'] += 20
                ranking_score[userId]['correct_results'] += 1
            elif bet_result_team1 == bet_result_team2 and winner == 'draw':
                ranking_score[userId]['pontuacao'] += 10
                ranking_score[userId]['correct_winner'] += 1
            elif bet_result_team1 > bet_result_team2 and winner == 'team1':
                ranking_score[userId]['pontuacao'] += 10
                ranking_score[userId]['correct_winner'] += 1
            elif bet_result_team1 < bet_result_team2 and winner == 'team2': 
                ranking_score[userId]['pontuacao'] += 10
                ranking_score[userId]['correct_winner'] += 1
    
    for key in ranking_score.keys():
        correct_results = ranking_score[key]['correct_results']
        correct_winner = ranking_score[key]['correct_winner']
        pontuacao = ranking_score[key]['pontuacao']
        if Ranking.objects.filter(fk_userId = key).exists():
            update_saved = Ranking.objects.get(fk_userId = key)
            update_saved.pontuacao = pontuacao
            update_saved.correct_winner = correct_winner
            update_saved.correct_results = correct_results
            update_saved.save()
        else:
            ranking = Ranking(fk_userId = key,
                    pontuacao = pontuacao,
                    correct_results = correct_results,
                    correct_winner = correct_winner)
            ranking.save()


    # order ranking 
    all_entries = Ranking.objects.order_by('-pontuacao','-correct_results','-correct_winner')
    return render(request, 'ranking/ranking.html',
        context= {"ranking":all_entries})
    
    
            
