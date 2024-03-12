from django.db import models
from teste.models import Teste

class Fundtecnico(models.Model):
    controle_1 = models.CharField(max_length=15)
    controle_2 = models.CharField(max_length=15)
    controle_3 = models.CharField(max_length=15)
    passe_1 = models.CharField(max_length=15)
    passe_2 = models.CharField(max_length=15)
    passe_3 = models.CharField(max_length=15)
    conducao_1 = models.CharField(max_length=15)
    conducao_2 = models.CharField(max_length=15)
    conducao_3 = models.CharField(max_length=15)
    chute_1 = models.CharField(max_length=15)
    chute_2 = models.CharField(max_length=15)
    chute_3 = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Fundtecnico' 
        