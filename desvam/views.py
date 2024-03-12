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
from desvam.models import Desvam, DesempenhoDesvam
from decimal import Decimal


def cadastrar_desvam(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    
    return render(request, 'cadastrar_desvam.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_desvam(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    atletas = Atleta.objects.get(id=atleta_id)

    
    c2km = request.POST.get('c2km')
    c3km = request.POST.get('c3km')
    vam = request.POST.get('vam')
    teste = request.POST.get('teste')


    try:
        # Convertendo os valores para Decimal
        c2km = Decimal(c2km)
        c3km = Decimal(c3km)
        # Convertendo os valores para float
        #c2km = float(c2km)
        #c3km = float(c3km)

    except (ValueError) as e:
        
        c2km = Decimal('0')
        c3km = Decimal('0')

    vam_2km = (c2km * Decimal(3.6))
    vam_3km = (c3km * Decimal(3.6))
    

    try:
        teste = get_object_or_404(Teste, id=int(teste))

        desvam = Desvam(c2km = c2km, c3km = c3km, vam = vam, teste = teste)
        desvam.save()


        desempenhodesvam = DesempenhoDesvam(teste = teste, vam_2km = vam_2km, vam_3km = vam_3km)
        desempenhodesvam.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_desvam(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_desvam.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
