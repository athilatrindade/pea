from django.contrib import admin
from .models import Compmembinf



@admin.register(Compmembinf)
class CompmembinfAdmin(admin.ModelAdmin):
    fields = ('direito', 'esquerdo', 'teste')
    


