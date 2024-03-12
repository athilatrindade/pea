from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testey, name='cadastrar_testey'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testey, name='valida_testey'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testey, name='home_testey'),
]