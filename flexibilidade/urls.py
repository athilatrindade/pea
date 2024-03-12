from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_flexibilidade, name='cadastrar_flexibilidade'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_flexibilidade, name='valida_flexibilidade'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_flexibilidade, name='home_flexibilidade'),
]