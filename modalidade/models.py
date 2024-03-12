from django.db import models
from datetime import date

class Modalidade (models.Model):
    codigo = models.CharField(max_length=3)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Modalidade'

    def __str__(self):
        return self.nome