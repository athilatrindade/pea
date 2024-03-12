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
from modalidade.models import Modalidade
from runmatic.models import Runmatic, AssimetriaRunmatic
from decimal import Decimal




def cadastrar_runmatic(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    
    return render(request, 'cadastrar_runmatic.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_runmatic(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atletas = Atleta.objects.get(id=atleta_id)

    teste = request.POST.get('teste')
    tcontatoesq = request.POST.get('tcontatoesq')
    tcontatodir = request.POST.get('tcontatodir')
    tvooesq = request.POST.get('tvooesq')
    tvoodir = request.POST.get('tvoodir')
    freqpassadaesq = request.POST.get('freqpassadaesq')
    freqpassadadir = request.POST.get('freqpassadadir')
    osverticalesq = request.POST.get('osverticalesq')
    osverticaldir = request.POST.get('osverticaldir')
    stifnessesq = request.POST.get('stifnessesq')
    stifnessdir = request.POST.get('stifnessdir')
    fmaximaesq = request.POST.get('fmaximaesq')
    fmaximadir = request.POST.get('fmaximadir')

    try:
        # Convertendo os valores para Decimal
        tcontatoesq = Decimal(tcontatoesq)
        tcontatodir = Decimal(tcontatodir)
    except (ValueError) as e:
        
        tcontatoesq = Decimal(0)
        tcontatodir = Decimal(0)

    tcontato = ((100* (tcontatodir - tcontatoesq))/((tcontatodir + tcontatoesq)/2))

    try:
        

        teste = get_object_or_404(Teste, id=int(teste))

        runmatic = Runmatic(teste = teste, tcontatoesq = tcontatoesq, tcontatodir = tcontatodir,
                                  tvooesq = tvooesq, tvoodir = tvoodir, freqpassadaesq = freqpassadaesq,
                                   freqpassadadir = freqpassadadir, osverticalesq = osverticalesq, osverticaldir = osverticaldir,
                                    stifnessesq = stifnessesq, stifnessdir = stifnessdir, fmaximaesq = fmaximaesq,
                                     fmaximadir = fmaximadir)
        runmatic.save()


        assimetriaRunmatic = AssimetriaRunmatic(teste = teste, tcontato = tcontato)
        assimetriaRunmatic.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_runmatic(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_runmatic.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
