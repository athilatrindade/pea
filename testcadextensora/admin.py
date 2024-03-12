from django.contrib import admin
from .models import Testcadextensora



@admin.register(Testcadextensora)
class TestcadextensoraAdmin(admin.ModelAdmin):
    list_display = ['teste', 'direito', 'esquerdo']
    
