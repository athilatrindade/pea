from django.contrib import admin
from .models import Modalidade



@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    fields = ('codigo', 'nome')


