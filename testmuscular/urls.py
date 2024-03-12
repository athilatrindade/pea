from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testmuscular, name='cadastrar_testmuscular'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testmuscular, name='valida_testmuscular'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testmuscular, name='home_testmuscular'),
]