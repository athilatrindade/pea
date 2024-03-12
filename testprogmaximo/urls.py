from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testprogmaximo, name='cadastrar_testprogmaximo'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testprogmaximo, name='valida_testprogmaximo'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testprogmaximo, name='home_testprogmaximo'),
]