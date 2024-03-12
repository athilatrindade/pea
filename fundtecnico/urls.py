from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_fundtecnico, name='cadastrar_fundtecnico'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_fundtecnico, name='valida_fundtecnico'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_fundtecnico, name='home_fundtecnico'),
]