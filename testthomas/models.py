from django.db import models
from teste.models import Teste

class Testthomas(models.Model):
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)
    iliopsoasdir = models.BooleanField(default=False)
    iliopsoasesq = models.BooleanField(default=False)
    retofemoraldir = models.BooleanField(default=False)
    retofemuralesq = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Testthomas'
            

