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
from angpopliteo.models import Angpopliteo
from modalidade.models import Modalidade

def cadastrar_angpopliteo(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'cadastrar_angpopliteo.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_angpopliteo(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor


    atletas = Atleta.objects.get(id=atleta_id)

    direito = request.POST.get('direito')
    esquerdo = request.POST.get('esquerdo')
    teste = request.POST.get('teste')
    

    try:

        teste = get_object_or_404(Teste, id=int(teste))

        angpopliteo = Angpopliteo(direito = direito, esquerdo = esquerdo, teste = teste)
        angpopliteo.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito {direito}, esquerdo {esquerdo}, teste {teste}")


def historico_angpopliteo(request, modalidade_id, atleta_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()

    testes = Teste.objects.filter( atleta = atleta)
    teste_id = request.GET.get('teste_id')

    angpopliteos = Angpopliteo.objects.filter(id = teste_id)

    status = request.GET.get('status')

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'historico_angpopliteo.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'modalidade_id':modalidade_id, 'testes':testes, 'angpopliteos':angpopliteos, 'modalidade':modalidade})

def home_angpopliteo(request, modalidade_id, atleta_id, teste_id):

    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}

    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_angpopliteo.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
