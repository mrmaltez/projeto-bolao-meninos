from re import U
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "GET":
        return render(request, 'users/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse("Usuário já existe")
        
        else:
            user = User.objects.create_user(username, email, password)

        return HttpResponse("Usuário cadastrado com sucesso!")



def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            login_django(request, user)
            return games(request)
        else:
            return HttpResponse("Email ou senha inválidos")

    
@login_required(login_url="/auth/login/")
def games(request):
     return  HttpResponseRedirect('/games/jogos/')