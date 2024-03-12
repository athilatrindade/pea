from django.contrib import admin
from .models import Rast, CalculoRast



@admin.register(Rast)
class RastAdmin(admin.ModelAdmin):
    fields = ('estimulo_1', 'estimulo_2', 'estimulo_3', 'estimulo_4', 'estimulo_5', 'estimulo_6', 'teste')



@admin.register(CalculoRast)
class CalculoRastAdmin(admin.ModelAdmin):
    list_display = ['teste', 'potanaerobia', 'capanaerobia', 'indfadiga']