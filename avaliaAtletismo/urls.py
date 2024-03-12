from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar_avaliacao/', views.cadastrar_avaliacao, name='cadastrar_avaliacao'),
    path('valida_cad_avaliacao/', views.valida_cad_avaliacao, name='valida_cad_avaliacao'),
    path('editar_avaliacao/<int:id>', views.editar_avaliacao, name='editar_avaliacao'),
    path('ver_avaliacao/<int:id>', views.ver_avaliacao, name='ver_avaliacao'),
]