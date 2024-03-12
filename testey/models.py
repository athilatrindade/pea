from django.db import models
from teste.models import Teste


class Testey(models.Model):
    anterior_direito_1 = models.CharField(max_length=15)
    anterior_direito_2 = models.CharField(max_length=15)
    anterior_direito_3 = models.CharField(max_length=15)
    anterior_esquerdo_1 = models.CharField(max_length=15)
    anterior_esquerdo_2 = models.CharField(max_length=15)
    anterior_esquerdo_3 = models.CharField(max_length=15)
    postero_medial_dir_1 = models.CharField(max_length=15)
    postero_medial_dir_2 = models.CharField(max_length=15)
    postero_medial_dir_3 = models.CharField(max_length=15)
    postero_medial_esq_1 = models.CharField(max_length=15)
    postero_medial_esq_2 = models.CharField(max_length=15)
    postero_medial_esq_3 = models.CharField(max_length=15)
    postero_lat_esq_1 = models.CharField(max_length=15)
    postero_lat_esq_2 = models.CharField(max_length=15)
    postero_lat_esq_3 = models.CharField(max_length=15)
    postero_lat_dir_1 = models.CharField(max_length=15)
    postero_lat_dir_2 = models.CharField(max_length=15)
    postero_lat_dir_3 = models.CharField(max_length=15)
    teste = models.ForeignKey(Teste, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = 'Testey' 
        
