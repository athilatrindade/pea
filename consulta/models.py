from django.db import models
from datetime import date, datetime
from atleta.models import Atleta
from instrutor.models import Instrutor

class Consulta(models.Model):
    numero = models.CharField(max_length=10)
    data = models.DateField(default= date.today)
    receituario = models.TextField(max_length=600)
    relato = models.TextField(max_length=1000)
    atleta = models.ForeignKey(Atleta, on_delete= models.DO_NOTHING)
    instrutor = models.ForeignKey(Instrutor, on_delete= models.DO_NOTHING)
    sigilo = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Consulta' 
        

    def __str__(self):
        return self.numero