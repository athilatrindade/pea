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
from teste.models import Teste
from flexibilidade.models import Flexibilidade, MaiorWellsFlexibilidade
from modalidade.models import Modalidade
from decimal import Decimal


def cadastrar_flexibilidade(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    return render(request, 'cadastrar_flexibilidade.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_flexibilidade(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atletas = Atleta.objects.get(id=atleta_id)

    wells_1 = request.POST.get('wells_1')
    wells_2 = request.POST.get('wells_2')
    wells_3 = request.POST.get('wells_3')
    teste = request.POST.get('teste')

    try:
        # Convertendo os valores para Decimal
        wells_1 = Decimal(wells_1)
        wells_2 = Decimal(wells_2)
        wells_3 = Decimal(wells_3)
    except (ValueError) as e:
        
        wells_1 = Decimal(0)
        wells_2 = Decimal(0)
        wells_3 = Decimal(0)

    maiorwells = wells_1

    if wells_2 > maiorwells:
        maiorwells = wells_2
    
    if wells_3 > maiorwells:
        maiorwells = wells_3


    try:

        teste = get_object_or_404(Teste, id=int(teste))

        flexibilidade = Flexibilidade(wells_1 = wells_1, wells_2 = wells_2, wells_3 = wells_3, teste = teste)
        flexibilidade.save()

        maiorwellsflexibilidade = MaiorWellsFlexibilidade(teste = teste, maiorwells = maiorwells)
        maiorwellsflexibilidade.save()

        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_flexibilidade(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_flexibilidade.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
