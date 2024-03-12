from django.db import models
from teste.models import Teste

class Runmatic(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    tcontatoesq = models.CharField(max_length=15)
    tcontatodir = models.CharField(max_length=15)
    tvooesq = models.CharField(max_length=15)
    tvoodir = models.CharField(max_length=15)
    freqpassadaesq = models.CharField(max_length=15)
    freqpassadadir = models.CharField(max_length=15)
    osverticalesq = models.CharField(max_length=15)
    osverticaldir = models.CharField(max_length=15)
    stifnessesq = models.CharField(max_length=15)
    stifnessdir = models.CharField(max_length=15)
    fmaximaesq = models.CharField(max_length=15)
    fmaximadir = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Runmatic'
        



class AssimetriaRunmatic(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    tcontato = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'AssimetriaRunmatic' #este comando server para eu escolher o nome que aparece na parte administrativa
    
    