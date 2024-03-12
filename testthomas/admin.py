from django.contrib import admin
from .models import Testthomas



@admin.register(Testthomas)
class TestthomasAdmin(admin.ModelAdmin):
    list_display = ['teste', 'iliopsoasdir', 'iliopsoasesq', 'retofemoraldir', 'retofemuralesq']
    
