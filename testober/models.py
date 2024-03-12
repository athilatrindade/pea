from django.db import models
from teste.models import Teste

class Testober(models.Model):
    direito = models.BooleanField(default=False)
    esquerdo = models.BooleanField(default=False)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Testober' 
    
