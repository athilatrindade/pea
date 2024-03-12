from django.db import models
from teste.models import Teste

class Desvam(models.Model):
    c2km = models.CharField(max_length=5)
    c3km = models.CharField(max_length=5)
    vam = models.CharField(max_length=5)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Desvam' 
    
        
class DesempenhoDesvam(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    vam_2km = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    vam_3km = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'DesempenhoDesvam'