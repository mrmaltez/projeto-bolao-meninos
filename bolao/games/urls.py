from django.urls import path
from . import views

urlpatterns = [
    path('jogos/', views.games, name='jogos'),
]