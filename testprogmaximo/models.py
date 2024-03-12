from django.db import models
from teste.models import Teste

class Testprogmaximo(models.Model):
    ultestatingido = models.CharField(max_length=10)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
            verbose_name = 'Testprogmaximo' 
            

    