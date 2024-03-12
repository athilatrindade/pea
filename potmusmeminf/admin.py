from django.contrib import admin
from .models import Postmusmeminf, CalculosPotmusmeminf



@admin.register(Postmusmeminf)
class PostmusmeminfAdmin(admin.ModelAdmin):
    fields = ('dj_1', 'dj_2', 'dj_3', 'sj_1', 'sj_2', 'sj_3', 'cmj_1', 'cmj_2', 'cmj_3', 'teste')


@admin.register(CalculosPotmusmeminf)
class CalculosPotmusmeminfAdmin(admin.ModelAdmin):
    list_display = ['teste', 'cmj_maior', 'sj_maior', 'dj_maior', 'indice_fr']