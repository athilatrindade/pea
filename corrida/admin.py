from django.contrib import admin
from .models import Corrida



@admin.register(Corrida)
class CorridaAdmin(admin.ModelAdmin):
    fields = ('tr', 'c20m', 'muddirecao', 'c10m', 'c30m', 'vift', 'teste')
    


