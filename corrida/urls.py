from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_corrida, name='cadastrar_corrida'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_corrida, name='valida_corrida'),
    #path('historico/<int:atleta_id>/', views.historico_corrida, name='historico_corrida'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_corrida, name='home_corrida'),
]