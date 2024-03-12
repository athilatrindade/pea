from django.contrib import admin
from .models import Teste



@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'data', 'instrutor', 'atleta', 'criado', 'alterado']

