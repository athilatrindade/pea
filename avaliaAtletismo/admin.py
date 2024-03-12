from django.contrib import admin
from .models import AvaliaAtletismo



@admin.register(AvaliaAtletismo)
class AvaliaAtletismo(admin.ModelAdmin): 
    list_display = ['data', 'atleta','criado', 'alterado']
    