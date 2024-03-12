from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_atleta, name='cadastrar_atleta'),
    path('editar/<int:id>', views.editar_atleta, name='editar_atleta'),
    path('lista/', views.ver_atletas, name='ver_atletas'),
    path('visualizar_atleta/<int:id>', views.visualizar_atleta, name='visualizar_atleta'),
    path('valida_cadastro_atleta/', views.valida_cadastro_atleta, name='valida_cadastro_atleta'),
    path('valida_edicao_atleta/<int:id>', views.valida_edicao_atleta, name='valida_edicao_atleta'),   
]