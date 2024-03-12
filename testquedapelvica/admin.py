from django.contrib import admin
from .models import Testquedapelvica



@admin.register(Testquedapelvica)
class TestquedapelvicaAdmin(admin.ModelAdmin):
    fields = ('direito', 'esquerdo', 'teste')
    


