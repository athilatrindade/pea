from django.db import models
from datetime import date
from modalidade.models import Modalidade
from atleta.models import Atleta
from usuario.models import Usuario

class Modalidades_atleta (models.Model):

    ativo = models.BooleanField(default=False)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.DO_NOTHING)
    atleta = models.ForeignKey(Atleta, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Modalidades do Atleta' 
