from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from atleta.models import Atleta
from instrutor.models import Instrutor
from usuario.models import Usuario
from modalidade.models import Modalidade
from teste.models import Teste
from antropometria.models import Antropometria, CalculoAntropometria
from decimal import Decimal, getcontext

def cadastrar_antropometria(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'cadastrar_antropometria.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_antropometria(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atletas = Atleta.objects.get(id=atleta_id)

    massacorporal = request.POST.get('massacorporal')
    dctriceps = request.POST.get('dctriceps')
    dcabdominal = request.POST.get('dcabdominal')
    dcpanturrilha = request.POST.get('dcpanturrilha')
    dcsubescapular = request.POST.get('dcsubescapular')
    circcoxamedial = request.POST.get('circcoxamedial')
    circpanturmedial = request.POST.get('circpanturmedial')
    dcbiceps = request.POST.get('dcbiceps')
    dcpeitoral = request.POST.get('dcpeitoral')
    dccoxamedial = request.POST.get('dccoxamedial')
    dcsuprailiaca = request.POST.get('dcsuprailiaca')
    dccoxaproximal = request.POST.get('dccoxaproximal')
    dcmedioaxilar = request.POST.get('dcmedioaxilar')
    altura = request.POST.get('altura')
    teste = request.POST.get('teste')
    

    try:
        # Convertendo os valores para Decimal
        massacorporal = Decimal(massacorporal)
        dctriceps = Decimal(dctriceps)
        dcabdominal = Decimal(dcabdominal)
        dcpanturrilha = Decimal(dcpanturrilha)
        dcsubescapular = Decimal(dcsubescapular)
        circcoxamedial = Decimal(circcoxamedial)
        circpanturmedial = Decimal(circpanturmedial)
        dcbiceps = Decimal(dcbiceps)
        dcpeitoral = Decimal(dcpeitoral)
        dccoxamedial = Decimal(dccoxamedial)
        dcsuprailiaca = Decimal(dcsuprailiaca)
        dccoxaproximal = Decimal(dccoxaproximal)
        dcmedioaxilar = Decimal(dcmedioaxilar)
        altura = Decimal(altura)
        
        
        
    except (ValueError) as e:
        
        massacorporal = Decimal(0)
        dctriceps = Decimal(0)
        dcabdominal = Decimal(0)
        dcpanturrilha = Decimal(0)
        dcsubescapular = Decimal(0)
        circcoxamedial = Decimal(0)
        circpanturmedial = Decimal(0)
        dcbiceps = Decimal(0)
        dcpeitoral = Decimal(0)
        dccoxamedial = Decimal(0)
        dcsuprailiaca = Decimal(0)
        dccoxaproximal = Decimal(0)
        dcmedioaxilar = Decimal(0)
        

    # Calcula a idade com base na data de nascimento
    hoje = date.today()
    idade = hoje.year - atletas.data_nasc.year - ((hoje.month, hoje.day) < (atletas.data_nasc.month, atletas.data_nasc.day))

    # Converta a idade para Decimal
    idade_decimal = Decimal(idade)
    idade_float = float(idade)

    somanovedobras = (dctriceps + dcbiceps + dcpeitoral + dcabdominal + dcpanturrilha +
                      dcsubescapular + dcmedioaxilar + dcsuprailiaca + dccoxamedial)
    
    somasetedobras = (dctriceps + dcpeitoral + dcabdominal + dcsubescapular + dcmedioaxilar +
                      dcsuprailiaca + dccoxamedial)
    

    somasetedobras_float = float(somasetedobras)
    
    densicorphomem = ((1.112 - (0.00043499 * somasetedobras_float))) + ((0.00000055 * (somasetedobras_float*somasetedobras_float))-(0.0002882*idade_float))

    densicorpmulher = ((1.097 - (0.00046971 * somasetedobras_float))) + ((0.00000056 * (somasetedobras_float*somasetedobras_float))-(0.00012828*idade_float))

    percgordhomem = (((4.95/densicorphomem)-4.50)*100)

    percgordmulher = (((5.01/densicorphomem)-4.57)*100)

    imc = (massacorporal/((altura/100)*(altura/100)))

    massacorporalfloat = float(massacorporal)

    gordcorporalhomem = ((massacorporalfloat*percgordhomem)/100)
    gordcorporalmulher = ((massacorporalfloat*percgordmulher)/100)

    massamagrahomem = (massacorporalfloat - gordcorporalhomem)
    massamagramulher = (massacorporalfloat - gordcorporalmulher)

    getcontext().prec = 10

    if atletas.sexo == "Masculino":

        somanovedobras = Decimal(f'{somanovedobras:.2f}')
        somasetedobras = Decimal(f'{somasetedobras:.2f}')
        densicorporal = Decimal(f'{densicorphomem:.2f}')
        percgordura = Decimal(f'{percgordhomem:.2f}')
        gordcorporal = Decimal(f'{gordcorporalhomem:.2f}')
        massamagra = Decimal(f'{massamagrahomem:.2f}')
    else:
        somanovedobras = Decimal(f'{somanovedobras:.2f}')
        somasetedobras = Decimal(f'{somasetedobras:.2f}')
        densicorporal = Decimal(f'{densicorpmulher:.2f}')
        percgordura = Decimal(f'{percgordmulher:.2f}')
        gordcorporal = Decimal(f'{gordcorporalmulher:.2f}')
        massamagra = Decimal(f'{massamagramulher:.2f}')



    try:
        teste = get_object_or_404(Teste, id=int(teste))

        antropometria = Antropometria(massacorporal = massacorporal, dctriceps = dctriceps,
                                       dcabdominal = dcabdominal, dcpanturrilha = dcpanturrilha,
                                       dcsubescapular = dcsubescapular, circcoxamedial = circcoxamedial,
                                       circpanturmedial = circpanturmedial, dcbiceps = dcbiceps,
                                       dcpeitoral = dcpeitoral, dccoxamedial = dccoxamedial,
                                       dcsuprailiaca = dcsuprailiaca, dccoxaproximal = dccoxaproximal,
                                       dcmedioaxilar = dcmedioaxilar, altura = altura, teste = teste)
        antropometria.save()

        calculoantropometria = CalculoAntropometria(teste = teste, somanovedobras = somanovedobras, somasetedobras = somasetedobras,
                                                    densicorporal = densicorporal, percgordura = percgordura, imc = imc,
                                                      gordcorporal = gordcorporal, massamagra = massamagra)
        calculoantropometria.save()        
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}, massacorporal {massacorporal}, dctriceps {dctriceps}, dcabdominal {dcabdominal}, dcpanturrilha {dcpanturrilha},dcsubescapular {dcsubescapular}, circcoxamedial {circcoxamedial},circpanturmedial {circpanturmedial}, dcbiceps {dcbiceps},dcpeitoral {dcpeitoral}, dccoxamedial {dccoxamedial},dcsuprailiaca {dcsuprailiaca}, dccoxaproximal {dccoxaproximal},dcmedioaxilar {dcmedioaxilar}, altura {altura}")


def home_antropometria(request, modalidade_id, atleta_id, teste_id):

    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}

    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_antropometria.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
