from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testober, name='cadastrar_testober'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testober, name='valida_testober'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testober, name='home_testober'),
]