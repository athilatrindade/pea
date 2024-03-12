from django.contrib import admin
from .models import Testober



@admin.register(Testober)
class TestoberAdmin(admin.ModelAdmin):
    fields = ('direito', 'esquerdo', 'teste')
    

