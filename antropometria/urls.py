from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_antropometria, name='cadastrar_antropometria'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_antropometria, name='valida_antropometria'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_antropometria, name='home_antropometria'),
]