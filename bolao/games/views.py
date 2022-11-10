from django.shortcuts import render
from .models import Games
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url="/auth/login/")
def games(request):
    if request.method == "GET":
        all_entries = Games.objects.all()
        return render(request, 'games/games.html',
        context= {"jogos":all_entries})
    else:
        results = {}
        all_entries = Games.objects.values()
        for i in all_entries:
            i = i["id"]
            name_1 = f'{i}_time_1'
            name_2 = f'{i}_time_2'
            results[i] = {'time_1':request.POST.get(name_1),
            'time_2':request.POST.get(name_2)} 

        # email = request.POST.get('email')
        # password = request.POST.get('password')
        print(results)
        return HttpResponse("Dados Salvos")
