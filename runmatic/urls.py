from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_runmatic, name='cadastrar_runmatic'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_runmatic, name='valida_runmatic'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_runmatic, name='home_runmatic'),
]