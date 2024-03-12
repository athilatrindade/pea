from django.db import models
from teste.models import Teste

class Compmembinf(models.Model):
    direito = models.CharField(max_length=15)
    esquerdo = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Compmembinf' 
        