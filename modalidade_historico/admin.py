from django.contrib import admin
from .models import Modalidades_atleta 



@admin.register(Modalidades_atleta)
class Modalidades_atletaAdmin(admin.ModelAdmin):
    list_display = ['modalidade', 'ativo', 'atleta', 'usuario', 'criado']


