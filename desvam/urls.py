from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_desvam, name='cadastrar_desvam'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_desvam, name='valida_desvam'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_desvam, name='home_desvam'),
]