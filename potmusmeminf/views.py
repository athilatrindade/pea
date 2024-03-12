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
from django import forms
from instrutor.models import Instrutor
from usuario.models import Usuario
from modalidade.models import Modalidade
from teste.models import Teste
from potmusmeminf.models import Postmusmeminf, CalculosPotmusmeminf
from decimal import Decimal


def cadastrar_potmusmeminf(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    
    return render(request, 'cadastrar_potmusmeminf.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_potmusmeminf(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    atletas = Atleta.objects.get(id=atleta_id)

    dj_1 = request.POST.get('dj_1')
    dj_2 = request.POST.get('dj_2')
    dj_3 = request.POST.get('dj_3')
    sj_1 = request.POST.get('sj_1')
    sj_2 = request.POST.get('sj_2')
    sj_3 = request.POST.get('sj_3')
    cmj_1 = request.POST.get('cmj_1')
    cmj_2 = request.POST.get('cmj_2')
    cmj_3 = request.POST.get('cmj_3')
    teste = request.POST.get('teste')


    try:
        # Convertendo os valores para Decimal
        cmj_1 = Decimal(cmj_1)
        cmj_2 = Decimal(cmj_2)
        cmj_3 = Decimal(cmj_3)
        sj_1 = Decimal(sj_1)
        sj_2 = Decimal(sj_2)
        sj_3 = Decimal(sj_3)
        dj_1 = Decimal(dj_1)
        dj_2 = Decimal(dj_2)
        dj_3 = Decimal(dj_3)
    
    except (ValueError) as e:
        
        cmj_1 = Decimal(0)
        cmj_2 = Decimal(0)
        cmj_3 = Decimal(0)
        sj_1 = Decimal(0)
        sj_2 = Decimal(0)
        sj_3 = Decimal(0)
        dj_1 = Decimal(0)
        dj_2 = Decimal(0)
        dj_3 = Decimal(0)
        


    cmj_maior = cmj_1
    
    if cmj_2 > cmj_maior:
        cmj_maior = cmj_2

    if cmj_3 > cmj_maior:
        cmj_maior = cmj_3

    sj_maior = sj_1

    if sj_2 > sj_maior:
        sj_maior = sj_2

    if sj_3 > sj_maior:
        sj_maior = sj_3

    dj_maior = dj_1

    if dj_2 > sj_maior:
        dj_maior = dj_2

    if dj_3 > dj_maior:
        dj_maior = dj_3

    indice_fr = (((cmj_maior - sj_maior)/sj_maior)*100)


    try:
       

        teste = get_object_or_404(Teste, id=int(teste))

        potmusmeminf = Postmusmeminf(dj_1 = dj_1, dj_2 = dj_2, dj_3 = dj_3,
                                  sj_1 = sj_1, sj_2 = sj_2, sj_3 = sj_3,
                                  cmj_1 = cmj_1, cmj_2 = cmj_2, cmj_3 = cmj_3, teste = teste)
        potmusmeminf.save()
        
        calculopotmusmeminf = CalculosPotmusmeminf(teste = teste, cmj_maior = cmj_maior, sj_maior = sj_maior,
                                                   dj_maior = dj_maior, indice_fr = indice_fr)
        calculopotmusmeminf.save()

        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_potmusmeminf(request, modalidade_id, atleta_id, teste_id):

    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_potmusmeminf.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
