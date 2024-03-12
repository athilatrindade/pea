from django.contrib import admin
from .models import Antropometria, CalculoAntropometria



@admin.register(Antropometria)
class AntropometriaAdmin(admin.ModelAdmin):
    fields = ('massacorporal', 'dctriceps', 'dcabdominal', 'dcpanturrilha',
              'dcsubescapular','circcoxamedial','circpanturmedial','dcbiceps',
               'dcpeitoral','dccoxamedial','dcsuprailiaca','dccoxaproximal','dcmedioaxilar', 'altura', 'teste')
    

@admin.register(CalculoAntropometria)
class CalculoAntropometriaAdmin(admin.ModelAdmin):
    list_display = ['teste', 'somanovedobras', 'somasetedobras', 'densicorporal',
                     'percgordura']