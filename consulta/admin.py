from django.contrib import admin
from .models import Consulta



@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'data', 'receituario', 'relato', 'atleta', 'instrutor', 'sigilo', 'criado', 'alterado']

