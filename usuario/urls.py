from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name = 'cadastrar_usuario'),
    path('login/', views.login, name = 'login'),
    path('valida_cadastro_usuario/', views.valida_cadastro_usuario, name='valida_cadastro_usuario'),
    path('valida_edicao_usuario_qualquer/<int:id>', views.valida_edicao_usuario_qualquer, name='valida_edicao_usuario_qualquer'),
    path('valida_edicao_meuusuario/', views.valida_edicao_meuusuario, name='valida_edicao_meuusuario'),
    path('valida_login_usuario/', views.valida_login_usuario, name='valida_login_usuario'),
    path('home/', views.home, name = 'home'),
    path('sair/', views.sair, name = 'sair'),
    path('editar/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('editar_meu_cad/<int:id>', views.editar_meu_cad, name='editar_meu_cad'), 
    path('ver_meu_cad/<int:id>', views.ver_meu_cad, name='ver_meu_cad'),
    path('lista/', views.lista_usuario, name = 'lista_usuario'),
    
]
