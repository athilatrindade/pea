from django.db import models
from teste.models import Teste

class Corrida(models.Model):
    tr = models.CharField(max_length=5)
    c20m = models.CharField(max_length=5)
    muddirecao = models.CharField(max_length=5)
    c10m = models.CharField(max_length=5)
    c30m = models.CharField(max_length=5)
    vift = models.DecimalField(max_digits= 5, decimal_places=2)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)


    class Meta:
        verbose_name = 'Corrida' 



