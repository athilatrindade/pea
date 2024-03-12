from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home_teste, name='home_teste'),
    path('modalidade/<int:modalidade_id>/', views.busca_modalidade, name='busca_modalidade'),
    path('avaliacao/home/<int:modalidade_id>/<int:atleta_id>/', views.home_avaliacoes, name='home_avaliacoes'),
    path('avaliacao/lista/<int:modalidade_id>/<int:atleta_id>/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('cadastrar/<int:modalidade_id>/<int:atleta_id>/', views.cadastrar_teste, name='cadastrar_teste'),
    path('editar/<int:id>', views.editar_teste, name='editar_teste'),
    path('validar/<int:modalidade_id>/<int:atleta_id>/', views.valida_teste, name='valida_teste'),
    path('visualizar/<int:atleta_id>/<int:teste_id>/', views.ver_avaliacao, name='ver_avaliacao'),
    path('historico/<int:atleta_id>/', views.historico_avaliacoes, name='historico_avaliacoes'),
    path('angpopliteo/', include('angpopliteo.urls')),
    path('antropometria/', include('antropometria.urls')),
    path('compmembinf/', include('compmembinf.urls')),
    path('condclinica/', include('condclinica.urls')),
    path('corrida/', include('corrida.urls')),
    path('desvam/', include('desvam.urls')),
    path('dorsiflexao/', include('dorsiflexao.urls')),
    path('flexibilidade/', include('flexibilidade.urls')),
    path('fundtecnico/', include('fundtecnico.urls')),
    path('potmusmeminf/', include('potmusmeminf.urls')),
    path('rast/', include('rast.urls')),
    path('runmatic/', include('runmatic.urls')),
    path('testcadextensora/', include('testcadextensora.urls')),
    path('testey/', include('testey.urls')),
    path('testmuscular/', include('testmuscular.urls')),
    path('testober/', include('testober.urls')),
    path('testprogmaximo/', include('testprogmaximo.urls')),
    path('testquedapelvica/', include('testquedapelvica.urls')),
    path('testsalto/', include('testsalto.urls')),
    path('testthomas/', include('testthomas.urls')),
]