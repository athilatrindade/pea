from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_angpopliteo, name='cadastrar_angpopliteo'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_angpopliteo, name='valida_angpopliteo'),
    path('historico/<int:modalidade_id>/<int:atleta_id>/', views.historico_angpopliteo, name='historico_angpopliteo'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_angpopliteo, name='home_angpopliteo'),
]