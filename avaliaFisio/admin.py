from django.contrib import admin
from .models import AvaliaFisio



@admin.register(AvaliaFisio)
class AvaliaFisioAdmin(admin.ModelAdmin):
    list_display = ['data', 'data_nasc', 'relato', 'atleta', 'avaliador', 'modalidade', 'criado', 'alterado']
   