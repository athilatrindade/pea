from django.db import models
from teste.models import Teste

class Testmuscular(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    abduquadrildir = models.CharField(max_length=15)
    abduquadrilesq = models.CharField(max_length=15)
    rotquadrildir = models.CharField(max_length=15)
    rotquadrilesq = models.CharField(max_length=15)
    flexplantardir = models.CharField(max_length=15)
    flexplantaresq = models.CharField(max_length=15)
    flexjoelhodir = models.CharField(max_length=15)
    flexjoelhoesq = models.CharField(max_length=15)
    exjoelhodir = models.CharField(max_length=15)
    exjoelhoesq = models.CharField(max_length=15)


    class Meta:
        verbose_name = 'Teste muscular' 
        verbose_name_plural = 'Testes musculares'