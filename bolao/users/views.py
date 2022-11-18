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
        first_name = request.POST.get('primeiro_nome')
        last_name = request.POST.get('sobrenome')

        user = User.objects.filter(username = username).first()
        if user:
            return render(request, 'users/register.html',
        context= {"fl_erro":1,
                "email":email,
                "username":username,
                "nome": first_name,
                "sobrenome": last_name})
        if first_name == "" or last_name == "":
            return render(request, 'users/register.html',
            context = {
                "email":email,
                "username":username,
                "fl_erro_nome":1,
                "nome": first_name,
                "sobrenome": last_name})

        
        else:
            user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name,
            last_name = last_name)

        return render(request, 'users/login.html',
        context= {"fl_register":1})



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
            return render(request, 'users/login.html',
        context= {"fl_erro":1})

    
@login_required(login_url="/auth/login/")
def games(request):
     return  HttpResponseRedirect('/games/jogos/')