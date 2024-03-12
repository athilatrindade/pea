from django.contrib import admin
from .models import Instrutor, PerfilInstrutor



@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'identificador', 'telefone', 'email', 'curso', 'endereco']
    

@admin.register(PerfilInstrutor)
class PerfilInstrutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    

