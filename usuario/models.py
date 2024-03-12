
from django.db import models
from datetime import date
from instrutor.models import Instrutor


class Usuario(models.Model):
    cpf = models.CharField(max_length= 11)
    nome = models.CharField(max_length= 155)
    email = models.EmailField(max_length= 105)
    telefone = models.CharField(max_length= 11)
    ativado = models.BooleanField(default=True)
    senha = models.CharField(max_length= 64)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    instrutor = models.ForeignKey(Instrutor, on_delete = models.DO_NOTHING)
    administrador = models.BooleanField(default=False)

    

    class Meta:
        verbose_name = 'Usuário' #este comando server para eu escolher o nome que aparece na parte administrativa
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome