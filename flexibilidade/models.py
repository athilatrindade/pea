from django.db import models
from teste.models import Teste

class Flexibilidade(models.Model):
    wells_1 = models.CharField(max_length=15)
    wells_2 = models.CharField(max_length=15)
    wells_3 = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Flexibilidade' 
        

class MaiorWellsFlexibilidade(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    maiorwells = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'MaiorWells'