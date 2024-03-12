from django.db import models
from teste.models import Teste

class Rast(models.Model):
    estimulo_1 = models.CharField(max_length=15)
    estimulo_2 = models.CharField(max_length=15)
    estimulo_3 = models.CharField(max_length=15)
    estimulo_4 = models.CharField(max_length=15)
    estimulo_5 = models.CharField(max_length=15)
    estimulo_6 = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Rast'
        
class CalculoRast(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    potanaerobia = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    capanaerobia = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    indfadiga = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'CalculoRast'