from django.contrib import admin
from .models import Testey



@admin.register(Testey)
class TesteyAdmin(admin.ModelAdmin):
    fields = ('anterior_direito_1', 'anterior_direito_2', 'anterior_direito_3',
               'anterior_esquerdo_1', 'anterior_esquerdo_2', 'anterior_esquerdo_3',
               'postero_medial_dir_1', 'postero_medial_dir_2', 'postero_medial_dir_3',
                 'postero_medial_esq_1', 'postero_medial_esq_2', 'postero_medial_esq_3',
                 'postero_lat_esq_1', 'postero_lat_esq_2', 'postero_lat_esq_3',
                 'postero_lat_dir_1', 'postero_lat_dir_2', 'postero_lat_dir_3', 'teste')
    