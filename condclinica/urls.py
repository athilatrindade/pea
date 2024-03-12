from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_condclinica, name='cadastrar_condclinica'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_condclinica, name='valida_condclinica'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_condclinica, name='home_condclinica'),
]