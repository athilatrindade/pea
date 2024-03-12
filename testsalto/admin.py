from django.contrib import admin
from .models import Testsalto



@admin.register(Testsalto)
class TestsaltoAdmin(admin.ModelAdmin):
    fields = ('direito', 'esquerdo', 'teste')



