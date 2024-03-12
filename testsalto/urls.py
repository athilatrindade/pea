from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testsalto, name='cadastrar_testsalto'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testsalto, name='valida_testsalto'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testsalto, name='home_testsalto'),
]