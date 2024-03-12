from django.db import models
from teste.models import Teste



class Antropometria(models.Model):
    massacorporal = models.DecimalField(max_digits=5, decimal_places=2)
    dctriceps = models.CharField(max_length=4)
    dcabdominal = models.CharField(max_length=4)
    dcpanturrilha = models.CharField(max_length=4)
    dcsubescapular = models.CharField(max_length=4)
    circcoxamedial = models.CharField(max_length=4)
    circpanturmedial = models.CharField(max_length=4)
    dcbiceps = models.CharField(max_length=4)
    dcpeitoral = models.CharField(max_length=4)
    dccoxamedial = models.CharField(max_length=4)
    dcsuprailiaca = models.CharField(max_length=4)
    dccoxaproximal = models.CharField(max_length=4)
    dcmedioaxilar = models.CharField(max_length=4)
    altura = models.CharField(max_length=3, blank=True)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Antropometria' 



class CalculoAntropometria(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    somanovedobras = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    somasetedobras = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    densicorporal = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    percgordura = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    imc = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    gordcorporal = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    massamagra = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'CalculoAntropometria'