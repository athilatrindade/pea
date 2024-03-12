from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.cadastrar_dorsiflexao, name='cadastrar_dorsiflexao'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.valida_dorsiflexao, name='valida_dorsiflexao'),
    path('home/<int:modalidade_id>/<int:atleta_id>/<int:teste_id>/', views.home_dorsiflexao, name='home_dorsiflexao'),
]