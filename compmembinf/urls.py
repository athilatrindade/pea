from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_compmembinf, name='cadastrar_compmembinf'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_compmembinf, name='valida_compmembinf'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_compmembinf, name='home_compmembinf'),
]