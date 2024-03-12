from django.contrib import admin
from .models import Testprogmaximo



@admin.register(Testprogmaximo)
class TestprogmaximoAdmin(admin.ModelAdmin):
    fields = ('ultestatingido', 'teste')



