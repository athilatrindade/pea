from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_instrutor, name='cadastrar_instrutor'),
    path('valida_cadastro_instrutor/', views.valida_cadastro_instrutor, name='valida_cadastro_instrutor'),
    path('valida_edicao_instrutor/<int:id>', views.valida_edicao_instrutor, name='valida_edicao_instrutor'),
    path('editar/<int:id>', views.editar_instrutor, name='editar_instrutor'),
    path('visualizar/<int:id>', views.ver_instrutor, name='ver_instrutor'),
    path('cadastrar_perfil/', views.cadastrar_perfil, name='cadastrar_perfil'),
    path('editar_perfil/<int:id>', views.editar_perfil, name='editar_perfil'),
    path('validar_perfil/', views.validar_perfil, name = 'validar_perfil'),
    path('validar_perfil_2/', views.validar_perfil_2, name = 'validar_perfil_2'),
    path('excluir_perfil/', views.excluir_perfil, name='excluir_perfil'),
    path('validar_edicao_perfil/<int:id>', views.validar_edicao_perfil, name='validar_edicao_perfil'),
    path('lista/', views.lista_instrutor, name='lista_instrutor'),
    path('lista_perfis/', views.lista_perfil, name='lista_perfil'),
    path('lista_perfis/membros/<int:id>', views.lista_membros_perfil, name='lista_membros_perfil'),
]
