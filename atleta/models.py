from django.db import models
from datetime import date
from modalidade.models import Modalidade

class Atleta (models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=11)
    data_nasc = models.DateField(default= date.today)
    cel_resp = models.CharField(max_length=11)
    grau_instrucao = models.CharField(max_length= 100)
    origem_escolar = models.CharField(max_length= 200)
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Atleta' 

    def __str__(self):
        return self.nome
