from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_testcadextensora, name='cadastrar_testcadextensora'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_testcadextensora, name='valida_testcadextensora'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_testcadextensora, name='home_testcadextensora'),
]