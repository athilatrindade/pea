from django.db import models
from datetime import date


class PerfilInstrutor(models.Model):
    nome = models.CharField(max_length=50)


    verbose_name = 'PerfilInstrutor' 
    verbose_name_plural = 'PerfilInstrutores'

    def __str__(self):
        return self.nome

class Instrutor(models.Model):
    nome = models.CharField(max_length=150)
    identificador = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=110)
    curso = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    perfil = models.ForeignKey(PerfilInstrutor, null=True, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Instrutor' 
        verbose_name_plural = 'Instrutores'

    def __str__(self):
        return self.nome
    

