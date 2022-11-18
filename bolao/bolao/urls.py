from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('/auth/login/')),
    path('auth/', include('users.urls')),
    path('games/', include('games.urls')),
    path('ranking/', include('ranking.urls'))
]
