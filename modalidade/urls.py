from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_modalidade, name='cadastrar_modalidade'),
    path('editar/<int:id>', views.editar_modalidade, name='editar_modalidade'),
    path('excluir/<int:id>', views.excluir_modalidade, name='excluir_modalidade'),
    path('valida_cadastro_modalidade/', views.valida_cadastro_modalidade, name='valida_cadastro_modalidade'),
    path('valida_edicao_modalidade/<int:id>', views.valida_edicao_modalidade, name='valida_edicao_modalidade'),
    path('lista/', views.lista_modalidade, name='lista_modalidade'),
    path('lista/membros/<int:id>', views.lista_membros, name='lista_membros'),
    path('lista/atletas/<int:id>', views.lista_atletas, name='lista_atletas'),
    path('adicionar/<int:modalidade_id>/<int:atleta_id>', views.adicionar_modalidade, name='adicionar_modalidade'),
    path('valida/<int:modalidade_id>/<int:atleta_id>', views.valida_adicionar_modalidade, name='valida_adicionar_modalidade'),
    
    
]