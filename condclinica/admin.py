from django.contrib import admin
from .models import Condclinica



@admin.register(Condclinica)
class CondclinicaAdmin(admin.ModelAdmin):
    fields = ('descricao', 'teste')
   


