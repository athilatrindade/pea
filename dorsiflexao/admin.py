from django.contrib import admin
from .models import Dorsiflexao


@admin.register(Dorsiflexao)
class DorsiflexaoAdmin(admin.ModelAdmin):
    fields = ('ec', 'dg', 'eg', 'dc', 'teste')
    


