from django.contrib import admin
from ranking.models import Ranking

@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    pass
