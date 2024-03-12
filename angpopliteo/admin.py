from django.contrib import admin
from .models import Angpopliteo



@admin.register(Angpopliteo)
class AngpopliteoAdmin(admin.ModelAdmin):
    list_display = ['direito', 'esquerdo', 'teste']