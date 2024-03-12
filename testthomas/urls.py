from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testthomas, name='cadastrar_testthomas'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testthomas, name='valida_testthomas'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testthomas, name='home_testthomas'),
]