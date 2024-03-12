from django.db import models
from datetime import date, datetime
from atleta.models import Atleta
from instrutor.models import Instrutor
from modalidade.models import Modalidade

class AvaliaAtletismo(models.Model):
    
    data = models.DateField(default= date.today)
    atleta = models.ForeignKey(Atleta, on_delete= models.DO_NOTHING) 
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Avaliação Atletismo' 
        verbose_name_plural = 'Avaliações Atletismo'
        

    def __str__(self):
        return self.atleta
