from django.contrib import admin
from .models import Fundtecnico



@admin.register(Fundtecnico)
class FundtecnicoAdmin(admin.ModelAdmin):
    fields = ('controle_1', 'controle_2', 'controle_3', 'passe_1', 'passe_2',
               'passe_3', 'conducao_1', 'conducao_2', 'conducao_3', 'chute_1', 'chute_2', 'chute_3', 'teste')
    
