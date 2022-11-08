from re import U
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
    return render(request, 'users/login.html')