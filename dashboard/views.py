from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect
from atleta.models import Atleta
from usuario.models import Usuario
from modalidade.models import Modalidade
from instrutor.models import Instrutor
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
from consulta.models import Consulta
from teste.models import Teste
from django.db.models import Count


def home(request):
    return render(request, 'home_minha_dashboard.html')

def periodo_painel(request):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        
        if request.method == 'POST':
            atleta_id = request.POST.get('atleta_id')
            data_inicio = request.POST.get('data_inicio')
            data_fim = request.POST.get('data_fim')

            request.session['atleta_id'] = atleta_id
            request.session['data_inicio'] = data_inicio
            request.session['data_fim'] = data_fim
            
            
            if atleta_id and data_inicio and data_fim:
                return redirect('painel_atleta', atleta_id=atleta_id)

        atletas = Atleta.objects.all().order_by('nome')
        status = request.GET.get('status')

        return render(request, 'periodo_painel.html', {'atletas':atletas, 'status': status})
    else:
        return redirect('/usuario/login/') 
    
def valida_periodo_painel(request):
    pass

def retorna_total_consultas(request): 
    total = Consulta.objects.count()
    
    if request.method == "GET":
        return JsonResponse({'total': total})
    
def retorna_total_consultas_atleta(request, atleta_id):

    total = Consulta.objects.filter(atleta_id=atleta_id).count()
    
    if request.method == "GET":
        return JsonResponse({'total': total})



def retorna_total_testes(request): 
    total = Teste.objects.count()
    if request.method == "GET":
        return JsonResponse({'total': total})
    
def retorna_total_testes_atleta(request, atleta_id): 
    total = Teste.objects.filter(atleta_id=atleta_id).count()
    if request.method == "GET":
        return JsonResponse({'total': total})

def painel_atleta(request, atleta_id):

    status = request.GET.get('status')

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        atleta_id = request.session.get('atleta_id')
        data_inicio = request.session.get('data_inicio')
        data_fim = request.session.get('data_fim')

        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        
        atleta = get_object_or_404(Atleta, id=atleta_id)
                
        
        tem_avaliacao_angpopliteo = Angpopliteo.objects.filter(
            teste__atleta=atleta,  
            teste__data__gte=data_inicio,  
            teste__data__lte=data_fim     
        )
        
        tem_avaliacao_antropometria = Antropometria.objects.filter(
            teste__atleta=atleta,  
            teste__data__gte=data_inicio,  
            teste__data__lte=data_fim     
        )

        tem_avaliacao_calculoantropometria = CalculoAntropometria.objects.filter(
            teste__atleta=atleta,  
            teste__data__gte=data_inicio,  
            teste__data__lte=data_fim     
        )

        tem_avaliacao_compmembinf = Compmembinf.objects.filter(
            teste__atleta=atleta,  
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim  
        )

        tem_avaliacao_condclinica = Condclinica.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim  
        )

        tem_avaliacao_corrida = Corrida.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_desvam = Desvam.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,  
            teste__data__lte=data_fim  
        )

        tem_avaliacao_desempenhodesvam = DesempenhoDesvam.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim  
        )

        tem_avaliacao_dorsiflexao = Dorsiflexao.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_flexibilidade = Flexibilidade.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_maiorwellsflexibilidade = MaiorWellsFlexibilidade.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_fundtecnico = Fundtecnico.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_potmusmeminf = Postmusmeminf.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_calculospotmusmeminf = CalculosPotmusmeminf.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_rast = Rast.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_calculorast = CalculoRast.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_runmatic = Runmatic.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_assimetriarunmatic = AssimetriaRunmatic.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testcadextensora = Testcadextensora.objects.filter(
            teste__atleta=atleta,
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testey = Testey.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testmuscular = Testmuscular.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testober = Testober.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testprogmaximo = Testprogmaximo.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testquedapelvica = Testquedapelvica.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        tem_avaliacao_testsalto = Testsalto.objects.filter(
            teste__atleta=atleta, 
            teste__data__gte=data_inicio,
            teste__data__lte=data_fim  
        )

        tem_avaliacao_testthomas = Testthomas.objects.filter(
            teste__atleta=atleta,  
            teste__data__gte=data_inicio, 
            teste__data__lte=data_fim 
        )

        context = {
            "tem_avaliacao_angpopliteo": tem_avaliacao_angpopliteo,
            "tem_avaliacao_antropometria": tem_avaliacao_antropometria,
            "tem_avaliacao_calculoantropometria":tem_avaliacao_calculoantropometria,
            "tem_avaliacao_compmembinf": tem_avaliacao_compmembinf,
            "tem_avaliacao_condclinica": tem_avaliacao_condclinica,
            "tem_avaliacao_corrida": tem_avaliacao_corrida,
            "tem_avaliacao_desvam": tem_avaliacao_desvam,
            "tem_avaliacao_desempenhodesvam":tem_avaliacao_desempenhodesvam,
            "tem_avaliacao_dorsiflexao": tem_avaliacao_dorsiflexao,
            "tem_avaliacao_flexibilidade": tem_avaliacao_flexibilidade,
            "tem_avaliacao_maiorwellsflexibilidade":tem_avaliacao_maiorwellsflexibilidade,
            "tem_avaliacao_fundtecnico": tem_avaliacao_fundtecnico,
            "tem_avaliacao_potmusmeminf": tem_avaliacao_potmusmeminf,
            "tem_avaliacao_calculospotmusmeminf":tem_avaliacao_calculospotmusmeminf,
            "tem_avaliacao_rast": tem_avaliacao_rast,
            "tem_avaliacao_calculorast":tem_avaliacao_calculorast,
            "tem_avaliacao_runmatic": tem_avaliacao_runmatic,
            "tem_avaliacao_assimetriarunmatic":tem_avaliacao_assimetriarunmatic,
            "tem_avaliacao_testcadextensora": tem_avaliacao_testcadextensora,
            "tem_avaliacao_testey": tem_avaliacao_testey,
            "tem_avaliacao_testmuscular": tem_avaliacao_testmuscular,
            "tem_avaliacao_testober": tem_avaliacao_testober,
            "tem_avaliacao_testprogmaximo": tem_avaliacao_testprogmaximo,
            "tem_avaliacao_testquedapelvica": tem_avaliacao_testquedapelvica,
            "tem_avaliacao_testsalto": tem_avaliacao_testsalto,
            "tem_avaliacao_testthomas": tem_avaliacao_testthomas,

            'atleta_id':atleta_id,
            'atleta':atleta,          
        }
        return render(request, 'dashboard_atleta.html', context)
    else:
        return redirect('/usuario/login/') 

def relatorio_testes(request): 
    # Obtém a data atual
    hoje = datetime.now()
    
    # Calcula o primeiro dia do mês atual
    primeiro_dia_mes_atual = hoje.replace(day=1)
    
    # Calcula a data de início para um ano atrás a partir do mês atual
    um_ano_atras = primeiro_dia_mes_atual.replace(year=hoje.year - 1)
    
    # Consulta o banco de dados para obter o total de testes feitos por mês
    dados = Teste.objects.filter(data__range=[um_ano_atras, hoje]).values('data__month', 'data__year').annotate(total=Count('id'))
    
    # Organiza os dados em listas separadas para rótulos e valores
    labels = []
    data = []
    for item in dados:
        labels.append(item['data__month'])
        data.append(item['total'])
    
    # Retorna os dados como uma resposta JSON
    data_json = {'data': data, 'labels': labels}
    return JsonResponse(data_json)

def relatorio_atletas_modalidade(request): 
    
    modalidades_ativas = Modalidades_atleta.objects.filter(ativo=True)
    
    
    modalidades_com_total_atletas = (
        modalidades_ativas
        .values('modalidade__nome')  
        .annotate(total_atletas=Count('atleta', distinct=True)) 
    )
    
    # Criar listas de rótulos (nomes de modalidades) e dados (total de atletas)
    labels = [modalidade['modalidade__nome'] for modalidade in modalidades_com_total_atletas]
    data = [modalidade['total_atletas'] for modalidade in modalidades_com_total_atletas]

    return JsonResponse({'labels': labels, 'data': data})


def relatorio_angpopliteo_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')

    avaliacoes = Angpopliteo.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)
     

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        angpopliteo = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(angpopliteo)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_antropometria_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Antropometria.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        antropometria = {
            "data_avaliacao": data_avaliacao,
            "massacorporal": avaliacao.massacorporal,
            "dctriceps": avaliacao.dctriceps,
            "dcabdominal": avaliacao.dcabdominal,
            "dcpanturrilha": avaliacao.dcpanturrilha,
            "dcsubescapular": avaliacao.dcsubescapular,
            "circcoxamedial": avaliacao.circcoxamedial,
            "circpanturmedial": avaliacao.circpanturmedial,
            "dcbiceps": avaliacao.dcbiceps,
            "dcpeitoral": avaliacao.dcpeitoral,
            "dccoxamedial": avaliacao.dccoxamedial,
            "dcsuprailiaca": avaliacao.dcsuprailiaca,
            "dccoxaproximal": avaliacao.dccoxaproximal,
            "dcmedioaxilar": avaliacao.dcmedioaxilar,
        }
        avaliacoes_formatadas.append(antropometria)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)


def relatorio_calculoantropometria_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = CalculoAntropometria.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        calculoantropometria = {
            "data_avaliacao": data_avaliacao,
            "somanovedobras": avaliacao.somanovedobras,
            "somasetedobras": avaliacao.somasetedobras,
            "densicorporal": avaliacao.densicorporal,
            "percgordura": avaliacao.percgordura,
            "imc": avaliacao.imc,
            "gordcorporal": avaliacao.gordcorporal,
            "massamagra": avaliacao.massamagra,

            
        }
        avaliacoes_formatadas.append(calculoantropometria)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_compmembinf_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Compmembinf.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)
    

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        compmembinf = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(compmembinf)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_condclinica_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Condclinica.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        condclinica = {
            "data_avaliacao": data_avaliacao,
            "descricao": avaliacao.descricao,
        }
        avaliacoes_formatadas.append(condclinica)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_corrida_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Corrida.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        corrida = {
            "data_avaliacao": data_avaliacao,
            "tr": avaliacao.tr,
            "c20m": avaliacao.c20m,
            "muddirecao": avaliacao.muddirecao,
            "c10m": avaliacao.c10m,
            "c30m": avaliacao.c30m,
            "vift": avaliacao.vift,
        }
        avaliacoes_formatadas.append(corrida)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_desvam_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Desvam.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        desvam = {
            "data_avaliacao": data_avaliacao,
            "c2km": avaliacao.c2km,
            "c3km": avaliacao.c3km,
            "vam": avaliacao.vam,
        }
        avaliacoes_formatadas.append(desvam)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_desempenhodesvam_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = DesempenhoDesvam.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        desempenhodesvam = {
            "data_avaliacao": data_avaliacao,
            "vam_2km": avaliacao.vam_2km,
            "vam_3km": avaliacao.vam_3km,
        }
        avaliacoes_formatadas.append(desempenhodesvam)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_dorsiflexao_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Dorsiflexao.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        dorsiflexao = {
            "data_avaliacao": data_avaliacao,
            "ec": avaliacao.ec,
            "dg": avaliacao.dg,
            "eg": avaliacao.eg,
            "dc": avaliacao.dc,
        }
        avaliacoes_formatadas.append(dorsiflexao)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_flexibilidade_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Flexibilidade.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        flexibilidade = {
            "data_avaliacao": data_avaliacao,
            "wells_1": avaliacao.wells_1,
            "wells_2": avaliacao.wells_2,
            "wells_3": avaliacao.wells_3,
        }
        avaliacoes_formatadas.append(flexibilidade)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_maiorwellsflexibilidade_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = MaiorWellsFlexibilidade.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        maiorwellsflexibilidade = {
            "data_avaliacao": data_avaliacao,
            "maiorwells": avaliacao.maiorwells,
        }
        avaliacoes_formatadas.append(maiorwellsflexibilidade)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_fundtecnico_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Fundtecnico.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        fundtecnico = {
            "data_avaliacao": data_avaliacao,
            "controle_1": avaliacao.controle_1,
            "controle_2": avaliacao.controle_2,
            "controle_3": avaliacao.controle_3,
            "passe_1": avaliacao.passe_1,
            "passe_2": avaliacao.passe_2,
            "passe_3": avaliacao.passe_3,
            "conducao_1": avaliacao.conducao_1,
            "conducao_2": avaliacao.conducao_2,
            "conducao_3": avaliacao.conducao_3,
            "chute_1": avaliacao.chute_1,
            "chute_2": avaliacao.chute_2,
            "chute_3": avaliacao.chute_3,
        }
        avaliacoes_formatadas.append(fundtecnico)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_potmusmeminf_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Postmusmeminf.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        potmusmeminf = {
            "data_avaliacao": data_avaliacao,
            "dj_1": avaliacao.dj_1,
            "dj_2": avaliacao.dj_2,
            "dj_3": avaliacao.dj_3,
            "sj_1": avaliacao.sj_1,
            "sj_2": avaliacao.sj_2,
            "sj_3": avaliacao.sj_3,
            "cmj_1": avaliacao.cmj_1,
            "cmj_2": avaliacao.cmj_2,
            "cmj_3": avaliacao.cmj_3,
        }
        avaliacoes_formatadas.append(potmusmeminf)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_calculospotmusmeminf_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = CalculosPotmusmeminf.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        calculospotmusmeminf = {
            "data_avaliacao": data_avaliacao,
            "cmj_maior": avaliacao.cmj_maior,
            "sj_maior": avaliacao.sj_maior,
            "dj_maior": avaliacao.dj_maior,
            "indice_fr": avaliacao.indice_fr,
        }
        avaliacoes_formatadas.append(calculospotmusmeminf)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)


def relatorio_rast_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Rast.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        rast = {
            "data_avaliacao": data_avaliacao,
            "estimulo_1": avaliacao.estimulo_1,
            "estimulo_2": avaliacao.estimulo_2,
            "estimulo_3": avaliacao.estimulo_3,
            "estimulo_4": avaliacao.estimulo_4,
            "estimulo_5": avaliacao.estimulo_5,
            "estimulo_6": avaliacao.estimulo_6,
        }
        avaliacoes_formatadas.append(rast)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_calculorast_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = CalculoRast.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        calculorast = {
            "data_avaliacao": data_avaliacao,
            "potanaerobia": avaliacao.potanaerobia,
            "capanaerobia": avaliacao.capanaerobia,
            "indfadiga": avaliacao.indfadiga,
        }
        avaliacoes_formatadas.append(calculorast)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_runmatic_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Runmatic.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        runmatic = {
            "data_avaliacao": data_avaliacao,
            "tcontatoesq": avaliacao.tcontatoesq,
            "tcontatodir": avaliacao.tcontatodir,
            "tvooesq": avaliacao.tvooesq,
            "tvoodir": avaliacao.tvoodir,
            "freqpassadaesq": avaliacao.freqpassadaesq,
            "freqpassadadir": avaliacao.freqpassadadir,
            "osverticalesq": avaliacao.osverticalesq,
            "osverticaldir": avaliacao.osverticaldir,
            "stifnessesq": avaliacao.stifnessesq,
            "stifnessdir": avaliacao.stifnessdir,
            "fmaximaesq": avaliacao.fmaximaesq,
            "fmaximadir": avaliacao.fmaximadir,
        }
        avaliacoes_formatadas.append(runmatic)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_assimetriarunmatic_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = AssimetriaRunmatic.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        assimetriarunmatic = {
            "data_avaliacao": data_avaliacao,
            "tcontato": avaliacao.tcontato,
        }
        avaliacoes_formatadas.append(assimetriarunmatic)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testcadextensora_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testcadextensora.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testcadextensora = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(testcadextensora)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testey_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testey.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testey = {
            "data_avaliacao": data_avaliacao,
            "anterior_direito_1": avaliacao.anterior_direito_1,
            "anterior_direito_2": avaliacao.anterior_direito_2,
            "anterior_direito_3": avaliacao.anterior_direito_3,
            "anterior_esquerdo_1": avaliacao.anterior_esquerdo_1,
            "anterior_esquerdo_2": avaliacao.anterior_esquerdo_2,
            "anterior_esquerdo_3": avaliacao.anterior_esquerdo_3,
            "postero_medial_dir_1": avaliacao.postero_medial_dir_1,
            "postero_medial_dir_2": avaliacao.postero_medial_dir_2,
            "postero_medial_dir_3": avaliacao.postero_medial_dir_3,
            "postero_medial_esq_1": avaliacao.postero_medial_esq_1,
            "postero_medial_esq_2": avaliacao.postero_medial_esq_2,
            "postero_medial_esq_3": avaliacao.postero_medial_esq_3,
            "postero_lat_esq_1": avaliacao.postero_lat_esq_1,
            "postero_lat_esq_2": avaliacao.postero_lat_esq_2,
            "postero_lat_esq_3": avaliacao.postero_lat_esq_3,
            "postero_lat_dir_1": avaliacao.postero_lat_dir_1,
            "postero_lat_dir_2": avaliacao.postero_lat_dir_2,
            "postero_lat_dir_3": avaliacao.postero_lat_dir_3,
        }
        avaliacoes_formatadas.append(testey)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)


def relatorio_testmuscular_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testmuscular.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testmuscular = {
            "data_avaliacao": data_avaliacao,
            "abduquadrildir": avaliacao.abduquadrildir,
            "abduquadrilesq": avaliacao.abduquadrilesq,
            "rotquadrildir": avaliacao.rotquadrildir,
            "rotquadrilesq": avaliacao.rotquadrilesq,
            "flexplantardir": avaliacao.flexplantardir,
            "flexplantaresq": avaliacao.flexplantaresq,
            "flexjoelhodir": avaliacao.flexjoelhodir,
            "flexjoelhoesq": avaliacao.flexjoelhoesq,
            "exjoelhodir": avaliacao.exjoelhodir,
            "exjoelhoesq": avaliacao.exjoelhoesq,
        }
        avaliacoes_formatadas.append(testmuscular)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testober_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testober.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testober = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(testober)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testprogmaximo_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testprogmaximo.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testprogmaximo = {
            "data_avaliacao": data_avaliacao,
            "ultestatingido": avaliacao.ultestatingido,
        }
        avaliacoes_formatadas.append(testprogmaximo)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testquedapelvica_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testquedapelvica.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testquedapelvica = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(testquedapelvica)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testsalto_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testsalto.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testsalto = {
            "data_avaliacao": data_avaliacao,
            "direito": avaliacao.direito,
            "esquerdo": avaliacao.esquerdo,
        }
        avaliacoes_formatadas.append(testsalto)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)

def relatorio_testthomas_atleta(request, atleta_id):

    data_inicio = request.session.get('data_inicio')
    data_fim = request.session.get('data_fim')
    
    avaliacoes = Testthomas.objects.filter(teste__atleta_id=atleta_id,
                                             teste__data__gte=data_inicio,
                                             teste__data__lte=data_fim)

    # Crie uma lista de avaliações no formato desejado
    avaliacoes_formatadas = []

    for avaliacao in avaliacoes:
        data_avaliacao = avaliacao.teste.data.strftime("%Y-%m-%d")
        testthomas = {
            "data_avaliacao": data_avaliacao,
            "iliopsoasdir": avaliacao.iliopsoasdir,
            "iliopsoasesq": avaliacao.iliopsoasesq,
            "retofemoraldir": avaliacao.retofemoraldir,
            "retofemuralesq": avaliacao.retofemuralesq,
        }
        avaliacoes_formatadas.append(testthomas)

    # Prepare os dados para resposta JSON
    data = {
        "avaliacoes": avaliacoes_formatadas,
    }

    return JsonResponse(data)