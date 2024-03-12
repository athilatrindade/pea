from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_rast, name='cadastrar_rast'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_rast, name='valida_rast'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_rast, name='home_rast'),
]