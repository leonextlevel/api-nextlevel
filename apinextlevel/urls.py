from django.contrib import admin
from django.urls import path, include

from apinextlevel.personagem.views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),

    path('helloworld/', hello_world, name='helloworld'),

    path('personagem/', include('apinextlevel.personagem.urls')),
]
