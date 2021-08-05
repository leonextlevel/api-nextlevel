from django.contrib import admin
from apinextlevel.personagem.models import (
    Personagem,
    Equipamento,
    Pericia,
    Magia,
    PersonagemEquipamento,
    PersonagemPericia,
    PersonagemMagia
)


admin.site.register(Personagem)
admin.site.register(Equipamento)
admin.site.register(Pericia)
admin.site.register(Magia)
admin.site.register(PersonagemEquipamento)
admin.site.register(PersonagemPericia)
admin.site.register(PersonagemMagia)
