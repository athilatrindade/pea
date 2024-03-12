from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testquedapelvica, name='cadastrar_testquedapelvica'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testquedapelvica, name='valida_testquedapelvica'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testquedapelvica, name='home_testquedapelvica'),
]