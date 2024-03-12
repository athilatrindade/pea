from django.db import models
from teste.models import Teste

class Postmusmeminf(models.Model):
    dj_1 = models.CharField(max_length=15)
    dj_2 = models.CharField(max_length=15)
    dj_3 = models.CharField(max_length=15)
    sj_1 = models.CharField(max_length=15)
    sj_2 = models.CharField(max_length=15)
    sj_3 = models.CharField(max_length=15)
    cmj_1 = models.CharField(max_length=15)
    cmj_2 = models.CharField(max_length=15)
    cmj_3 = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Postmusmeminf'


class CalculosPotmusmeminf(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    cmj_maior = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    sj_maior = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    dj_maior = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    indice_fr = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'CalculosPotmusmeminf'