from django.db import models
from teste.models import Teste

class Dorsiflexao(models.Model):
    ec = models.CharField(max_length=15)
    dg = models.CharField(max_length=15)
    eg = models.CharField(max_length=15)
    dc = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Dorsiflexao'
        verbose_name_plural = 'Dorsiflexões'
        
