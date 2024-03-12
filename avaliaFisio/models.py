from django.db import models
from datetime import date, datetime
from atleta.models import Atleta
from instrutor.models import Instrutor
from modalidade.models import Modalidade

class AvaliaFisio(models.Model):
    
    data = models.DateField(default= date.today)
    data_nasc = models.DateField(default= date.today)
    relato = models.TextField(max_length=1000)
    modalidade = models.ForeignKey(Modalidade, on_delete= models.DO_NOTHING)
    atleta = models.ForeignKey(Atleta, on_delete= models.DO_NOTHING)
    avaliador = models.CharField(max_length=150)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Avaliação Fisioterapia' 
        verbose_name_plural = 'Avaliações Fisioterapia'
        
