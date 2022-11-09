from django.contrib import admin
from games.models import Games, Bets, Results

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    pass


@admin.register(Bets)
class BetsAdmin(admin.ModelAdmin):
    pass


@admin.register(Results)
class BetsAdmin(admin.ModelAdmin):
    pass