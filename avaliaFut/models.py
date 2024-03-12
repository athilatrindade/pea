from django.db import models
from datetime import date, datetime
from atleta.models import Atleta
from instrutor.models import Instrutor
from modalidade.models import Modalidade

class AvaliaFut(models.Model):
    
    data = models.DateField(default= date.today)
    modalidade = models.ForeignKey(Modalidade, on_delete= models.DO_NOTHING)
    atleta = models.ForeignKey(Atleta, on_delete= models.DO_NOTHING)
  
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Avaliação Futebol' 
        verbose_name_plural = 'Avaliações Futebol'
        

    def __str__(self):
        return self.atleta
