from django.db import models
from datetime import date
from instrutor.models import Instrutor
from atleta.models import Atleta

class Teste(models.Model):
    codigo = models.CharField(max_length=10)
    data = models.DateField(default= date.today)
    instrutor = models.ForeignKey(Instrutor, on_delete = models.DO_NOTHING)
    atleta = models.ForeignKey(Atleta, on_delete = models.DO_NOTHING)
    criado = models.DateTimeField(auto_now=True)
    alterado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Teste'
        

    def __str__(self):
        return self.data.strftime('%Y-%m-%d')
