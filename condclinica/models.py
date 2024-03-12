from django.db import models
from teste.models import Teste

class Condclinica(models.Model):
    descricao = models.TextField(max_length=300)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Condclinica' 
        
