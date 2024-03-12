from django.contrib import admin
from .models import Testmuscular



@admin.register(Testmuscular)
class TestmuscularAdmin(admin.ModelAdmin):
    list_display = ['teste', 'abduquadrildir', 'abduquadrilesq', 'rotquadrildir', 'rotquadrilesq',
                    'flexplantardir', 'flexplantaresq', 'flexjoelhodir', 'flexjoelhoesq',
                    'exjoelhodir', 'exjoelhoesq']
    
