from django.contrib import admin
from .models import Desvam, DesempenhoDesvam



@admin.register(Desvam)
class DesvamAdmin(admin.ModelAdmin):
    fields = ('c2km', 'c3km', 'vam', 'teste')
    

@admin.register(DesempenhoDesvam)
class DesempenhoDesvamAdmin(admin.ModelAdmin):
    list_display = ['teste', 'vam_2km', 'vam_3km']
