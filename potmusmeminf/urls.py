from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_potmusmeminf, name='cadastrar_potmusmeminf'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_potmusmeminf, name='valida_potmusmeminf'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_potmusmeminf, name='home_potmusmeminf'),
]