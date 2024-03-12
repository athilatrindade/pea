from django.contrib import admin
from .models import Atleta



@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin): 
    list_display = ['nome', 'celular', 'data_nasc', 'cel_resp', 'grau_instrucao', 'origem_escolar', 'cpf', 'sexo']
