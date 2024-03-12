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
from rast.models import Rast, CalculoRast
from teste.models import Teste
from modalidade.models import Modalidade
from decimal import Decimal


def cadastrar_rast(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    
    return render(request, 'cadastrar_rast.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_rast(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    

    atletas = Atleta.objects.get(id=atleta_id)

    estimulo_1 = request.POST.get('estimulo_1')
    estimulo_2 = request.POST.get('estimulo_2')
    estimulo_3 = request.POST.get('estimulo_3')
    estimulo_4 = request.POST.get('estimulo_4')
    estimulo_5 = request.POST.get('estimulo_5')
    estimulo_6 = request.POST.get('estimulo_6')
    teste = request.POST.get('teste')


    try:
        # Convertendo os valores para Decimal
        estimulo_1 = Decimal(estimulo_1)
        estimulo_2 = Decimal(estimulo_2)
        estimulo_3 = Decimal(estimulo_3)
        estimulo_4 = Decimal(estimulo_4)
        estimulo_5 = Decimal(estimulo_5)
        estimulo_6 = Decimal(estimulo_6)
    except (ValueError) as e:
        
        estimulo_1 = Decimal(0)
        estimulo_2 = Decimal(0)
        estimulo_3 = Decimal(0)
        estimulo_4 = Decimal(0)
        estimulo_5 = Decimal(0)
        estimulo_6 = Decimal(0)

    capanaerobia = ((estimulo_1 + estimulo_2 + estimulo_3 + estimulo_4 + estimulo_5 + estimulo_6)/6)

    potanaerobia = estimulo_1

    if estimulo_2 > potanaerobia:
        potanaerobia = estimulo_2

    if estimulo_3 > potanaerobia:
        potanaerobia = estimulo_3

    if estimulo_4 > potanaerobia:
        potanaerobia = estimulo_4

    if estimulo_5 > potanaerobia:
        potanaerobia = estimulo_5

    if estimulo_6 > potanaerobia:
        potanaerobia = estimulo_6

    menorsprint = estimulo_1

    if estimulo_2 < menorsprint:
        menorsprint = estimulo_2

    if estimulo_3 < menorsprint:
        menorsprint = estimulo_3
    
    if estimulo_4 < menorsprint:
        menorsprint = estimulo_4
    
    if estimulo_5 < menorsprint:
        menorsprint = estimulo_5

    if estimulo_6 < menorsprint:
        menorsprint = estimulo_6

    indfadiga = (((potanaerobia/menorsprint)*100)/menorsprint)

    try:
        

        teste = get_object_or_404(Teste, id=int(teste))

        rast = Rast(estimulo_1 = estimulo_1, estimulo_2 = estimulo_2, estimulo_3 = estimulo_3,
                                  estimulo_4 = estimulo_4, estimulo_5 = estimulo_5, estimulo_6 = estimulo_6, teste = teste)
        rast.save()
        

        calculorast = CalculoRast(teste = teste, potanaerobia = potanaerobia, capanaerobia = capanaerobia,
                                  indfadiga = indfadiga)
        calculorast.save()

        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_rast(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_rast.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
