from django.contrib import admin
from .models import Flexibilidade, MaiorWellsFlexibilidade



@admin.register(Flexibilidade)
class FlexibilidadeAdmin(admin.ModelAdmin):   
    fields = ('wells_1', 'wells_2', 'wells_3', 'teste')


@admin.register(MaiorWellsFlexibilidade)
class MaiorWellsFlexibilidadeAdmin(admin.ModelAdmin):
    fields = ('teste', 'maiorwells')