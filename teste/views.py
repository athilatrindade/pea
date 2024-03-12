from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from atleta.models import Atleta
from usuario.models import Usuario
from modalidade.models import Modalidade
from instrutor.models import Instrutor
from teste.models import Teste
from datetime import date
from angpopliteo.models import Angpopliteo
from antropometria.models import Antropometria, CalculoAntropometria
from compmembinf.models import Compmembinf
from condclinica.models import Condclinica
from corrida.models import Corrida
from desvam.models import Desvam, DesempenhoDesvam
from dorsiflexao.models import Dorsiflexao
from flexibilidade.models import Flexibilidade, MaiorWellsFlexibilidade
from fundtecnico.models import Fundtecnico
from potmusmeminf.models import Postmusmeminf, CalculosPotmusmeminf
from rast.models import Rast, CalculoRast
from runmatic.models import Runmatic, AssimetriaRunmatic
from testcadextensora.models import Testcadextensora
from testey.models import Testey
from testmuscular.models import Testmuscular
from testober.models import Testober
from testprogmaximo.models import Testprogmaximo
from testquedapelvica.models import Testquedapelvica
from testsalto.models import Testsalto
from testthomas.models import Testthomas
from modalidade_historico.models import Modalidades_atleta
from django.db.models import Max


def home_teste(request):
    
    status = request.GET.get('status')
    atleta = Atleta.objects.all()
    
    
    modalidades_atleta = Modalidades_atleta.objects.values('modalidade__id', 'modalidade__nome').distinct()
    
    
    modalidades = [{'id': ma['modalidade__id'], 'nome': ma['modalidade__nome']} for ma in modalidades_atleta]
    
    
    modalidades_nao_associadas = Modalidade.objects.exclude(id__in=[ma['modalidade__id'] for ma in modalidades_atleta])
    
    
    for modalidade in modalidades_nao_associadas:
        modalidades.append({'id': modalidade.id, 'nome': modalidade.nome})
    
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        usuario_id = request.session.get('usuario')
        imagens = {
            'atleta_url': '/media/img/atletismo.png',
            'fisioterapia_url': '/media/img/fisioterapia.png',
            'futebol_url': '/media/img/futebol.png',
            'usuario_admin': usuario.administrador,
            'usuario_id': usuario_id,
            'usuario_instrutor': usuario.instrutor,
            'atleta' : atleta,
            'modalidades' : modalidades,
        }

        if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            imagens['usuario_id'] = usuario_id
            
            return render(request, 'home_teste.html', imagens)
        else:
            return redirect('/usuario/login/?status=2')
    else:
        return redirect('/usuario/login/')

def cadastrar_teste(request,modalidade_id, atleta_id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        modalidades = Modalidade.objects.get(id=modalidade_id)
        instrutores = Instrutor.objects.all()
        status = request.GET.get('status')

        usuario = Usuario.objects.get(id=request.session['usuario'])
        instrutor_relacionado = usuario.instrutor

        atletas = Modalidades_atleta.objects.filter(modalidade = modalidades.id).order_by('atleta')

        atleta = Atleta.objects.get(id = atleta_id)

        last_teste = Teste.objects.aggregate(Max('id'))
        next_id = last_teste['id__max'] + 1 if last_teste['id__max'] else 1

        codigo = f'{next_id:03}'

        return render(request, 'cadastrar_teste.html', {'instrutor_relacionado': instrutor_relacionado,'status':status, 'atleta':atleta, 'modalidades':modalidades, 'atletas':atletas, 'codigo':codigo})
    return redirect('/usuario/login/')

def editar_teste(request, id):
    pass
  

def ver_avaliacao(request, atleta_id, teste_id):
    
    status = request.GET.get('status')
    modalidade_id = request.GET.get('modalidade_id')
    testes = Teste.objects.get(id=teste_id)
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atleta = Atleta.objects.get(id = atleta_id)


    angpopliteo_avaliacoes = Angpopliteo.objects.filter(teste=testes)
    antropometria_avaliacoes = Antropometria.objects.filter(teste=testes)
    compmembinf_avaliacoes = Compmembinf.objects.filter(teste=testes)
    condclinica_avaliacoes = Condclinica.objects.filter(teste=testes)
    corrida_avaliacoes = Corrida.objects.filter(teste=testes)
    desvam_avaliacoes = Desvam.objects.filter(teste=testes)
    dorsiflexao_avaliacoes = Dorsiflexao.objects.filter(teste=testes)
    flexibilidade_avaliacoes = Flexibilidade.objects.filter(teste=testes)
    fundtecnico_avaliacoes = Fundtecnico.objects.filter(teste=testes)
    potmusmeinf_avaliacoes = Postmusmeminf.objects.filter(teste=testes)
    rast_avaliacoes = Rast.objects.filter(teste=testes)
    runmatic_avaliacoes = Runmatic.objects.filter(teste=testes)
    testcadextensora_avaliacoes = Testcadextensora.objects.filter(teste=testes)
    testey_avaliacoes = Testey.objects.filter(teste=testes)
    testmuscular_avaliacoes = Testmuscular.objects.filter(teste=testes)
    testober_avaliacoes = Testober.objects.filter(teste=testes)
    testprogmaximo_avaliacoes = Testprogmaximo.objects.filter(teste=testes)
    testquedapelvica_avaliacoes = Testquedapelvica.objects.filter(teste=testes)
    testsalto_avaliacoes = Testsalto.objects.filter(teste=testes)
    testthomas_avaliacoes = Testthomas.objects.filter(teste=testes)

    #adicionando abaixo os calculos
    calculoantropometria_avaliacoes = CalculoAntropometria.objects.filter(teste=testes)
    assimetriarunmatic_avaliacoes = AssimetriaRunmatic.objects.filter(teste=testes)
    maiorwellsflexibilidade_avaliacoes = MaiorWellsFlexibilidade.objects.filter(teste=testes)
    calculospotmusmeminf_avaliacoes = CalculosPotmusmeminf.objects.filter(teste=testes)
    desempenhodesvam_avaliacoes = DesempenhoDesvam.objects.filter(teste=testes)
    calculorast_avaliacoes = CalculoRast.objects.filter(teste=testes)


    return render(request, 'ver_teste.html', {'instrutor_relacionado': instrutor_relacionado,
                                              'status':status, 'atleta':atleta, 'testes':testes,
                                              'angpopliteo_avaliacoes':angpopliteo_avaliacoes,
                                              'antropometria_avaliacoes':antropometria_avaliacoes,
                                              'compmembinf_avaliacoes':compmembinf_avaliacoes,
                                              'condclinica_avaliacoes':condclinica_avaliacoes,
                                              'corrida_avaliacoes':corrida_avaliacoes,
                                              'desvam_avaliacoes':desvam_avaliacoes,
                                              'dorsiflexao_avaliacoes':dorsiflexao_avaliacoes,
                                              'flexibilidade_avaliacoes':flexibilidade_avaliacoes,
                                              'fundtecnico_avaliacoes':fundtecnico_avaliacoes,
                                              'potmusmeinf_avaliacoes':potmusmeinf_avaliacoes,
                                              'rast_avaliacoes':rast_avaliacoes,
                                              'runmatic_avaliacoes':runmatic_avaliacoes,
                                              'testcadextensora_avaliacoes':testcadextensora_avaliacoes,
                                              'testey_avaliacoes':testey_avaliacoes,
                                              'testmuscular_avaliacoes':testmuscular_avaliacoes,
                                              'testober_avaliacoes':testober_avaliacoes,
                                              'testprogmaximo_avaliacoes':testprogmaximo_avaliacoes,
                                              'testquedapelvica_avaliacoes':testquedapelvica_avaliacoes,
                                              'testsalto_avaliacoes':testsalto_avaliacoes,
                                              'testthomas_avaliacoes':testthomas_avaliacoes,
                                              'modalidade_id':modalidade_id,
                                              'calculoantropometria_avaliacoes':calculoantropometria_avaliacoes,
                                              'assimetriarunmatic_avaliacoes':assimetriarunmatic_avaliacoes,
                                              'maiorwellsflexibilidade_avaliacoes':maiorwellsflexibilidade_avaliacoes,
                                              'calculospotmusmeminf_avaliacoes':calculospotmusmeminf_avaliacoes,
                                              'desempenhodesvam_avaliacoes':desempenhodesvam_avaliacoes,
                                              'calculorast_avaliacoes':calculorast_avaliacoes})

def valida_teste(request, modalidade_id, atleta_id):

    status = request.GET.get('status')
    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    

    atletas = Atleta.objects.get(id=atleta_id)

    codigo = request.POST.get('codigo')
    data = request.POST.get('data')
    instrutor = request.POST.get('instrutor')
    atleta = request.POST.get('atleta') 

    try:
        atletas = get_object_or_404(Atleta, id=int(atleta))
        instrutores = get_object_or_404(Instrutor, id=int(instrutor))

        teste = Teste(codigo = codigo, data = data, instrutor = instrutores, 
                     atleta = atletas)
        teste.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste.id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora codigo {codigo}, data {data}, instrutor {instrutor}, atleta {atleta}, modalidade_id {modalidade_id} atleta_id {atleta_id}")



def busca_modalidade(request, modalidade_id):
    
    status = request.GET.get('status')
    modalidades = Modalidade.objects.get(id=modalidade_id)
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    atletas = Modalidades_atleta.objects.filter(modalidade=modalidades.id, ativo = True).order_by('atleta__nome')

    return render(request, 'atletas_modalidade.html', {'instrutor_relacionado': instrutor_relacionado, 'modalidades': modalidades, 'atletas': atletas, 'status':status})



def home_avaliacoes(request, modalidade_id, atleta_id):
    status = request.GET.get('status')
    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    modalidade_atleta = Modalidades_atleta.objects.get(atleta_id=atleta_id, modalidade=modalidade)

    modalidades = request.POST.get('modalidade_id')

    atleta = Atleta.objects.get(id=atleta_id)

    imagens = {
        'cadastro_teste_url': '/media/img/novo_teste.png',
        'historico_avaliacao_url': '/media/img/historico_avaliacao.png',
        'instrutor_relacionado': instrutor_relacionado,
        'modalidade': modalidade,
        'modalidades':modalidades,
        'atleta': atleta,
        'status': status,
        'modalidade_atleta':modalidade_atleta,
    }

    return render(request, 'home_avaliacoes.html', imagens)


def lista_avaliacoes(request,modalidade_id, atleta_id):
    
    avaliacao_url = {'avaliacao_url': '/media/img/avaliacao.png'}
    
    
    status = request.GET.get('status')
    modalidades = Modalidade.objects.get(id=modalidade_id)
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    teste_id = request.GET.get('teste_id')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    atletas = Modalidades_atleta.objects.filter(modalidade = modalidades.id).order_by('atleta')

    atleta = Atleta.objects.get(id=atleta_id)
    return render(request, 'avaliacoes_lista.html', {'instrutor_relacionado': instrutor_relacionado, 'modalidades': modalidades, 'atletas': atletas, 'status':status, 'atleta':atleta, 'teste_id':teste_id, 'avaliacao_url':avaliacao_url})


def historico_avaliacoes(request, atleta_id):
    status = request.GET.get('status')
    modalidade_id = request.GET.get('modalidade_id')
    modalidade = request.GET.get('modalidade')
    modalidade = request.POST.get('modalidade')
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    teste_id = request.GET.get('teste_id')

    testes = Teste.objects.filter(atleta = atleta_id).order_by('criado')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    

    atleta = Atleta.objects.get(id=atleta_id)

    try:
        
        modalidade_id = modalidade_id
    except Modalidades_atleta.DoesNotExist:
        modalidade_id = None
    
    
    return render(request, 'historico_avaliacoes.html', {'instrutor_relacionado': instrutor_relacionado,'status':status, 'atleta':atleta, 'teste_id':teste_id, 'testes':testes, 'modalidade_id':modalidade_id, 'modalidade':modalidade})
    