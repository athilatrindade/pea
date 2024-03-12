from django.contrib import admin
from .models import AvaliaFut



@admin.register(AvaliaFut)
class AvaliaFutAdmin(admin.ModelAdmin):
    
    list_display = ['data', 'atleta','modalidade', 'criado', 'alterado']
    