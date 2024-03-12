from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/<int:id>', views.home_consulta, name='home_consulta'),
    path('cadastrar/<int:id>', views.cadastrar_consulta, name='cadastrar_consulta'),
    path('editar_consulta/<int:atleta_id>/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('valida_cad_consulta/', views.valida_cad_consulta, name='valida_cad_consulta'),
    path('valida_edit_consulta/<int:atleta_id>/<int:consulta_id>/', views.valida_edit_consulta, name='valida_edit_consulta'),
    path('ver_consulta/<int:atleta_id>/<int:consulta_id>/', views.ver_consulta, name='ver_consulta'),
    path('historico/<int:id>', views.historico_consulta, name='historico_consulta'),
    path('busca/', views.busca_atleta_consulta, name='busca_atleta_consulta'),
]