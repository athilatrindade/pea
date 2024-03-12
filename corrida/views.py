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
from usuario.models import Usuario
from instrutor.models import Instrutor
from modalidade.models import Modalidade
from teste.models import Teste
from corrida.models import Corrida


def cadastrar_corrida(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    
    return render(request, 'cadastrar_corrida.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_corrida(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    

    atletas = Atleta.objects.get(id=atleta_id)

    tr = request.POST.get('tr')
    c20m = request.POST.get('c20m')
    muddirecao = request.POST.get('muddirecao')
    c10m = request.POST.get('c10m')
    c30m = request.POST.get('c30m')
    vift = request.POST.get('vift')
    teste = request.POST.get('teste')

    

    try:

        teste = get_object_or_404(Teste, id=int(teste))

        corrida = Corrida(tr = tr, c20m = c20m, muddirecao = muddirecao, c10m = c10m, c30m = c30m, vift = vift, teste = teste)
        corrida.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_corrida(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_corrida.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
