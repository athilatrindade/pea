from django.contrib import admin
from .models import Runmatic, AssimetriaRunmatic



@admin.register(Runmatic)
class RunmaticAdmin(admin.ModelAdmin):
    list_display = ['teste', 'tcontatoesq', 'tcontatodir','tvooesq','tvoodir', 'freqpassadaesq',
                    'freqpassadadir', 'osverticalesq', 'osverticaldir', 'stifnessesq', 'stifnessdir',
                    'fmaximaesq', 'fmaximadir']

@admin.register(AssimetriaRunmatic)
class AssimetriaRunmaticAdmin(admin.ModelAdmin):
    list_display = ['teste', 'tcontato']