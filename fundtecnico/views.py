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
from fundtecnico.models import Fundtecnico


def cadastrar_fundtecnico(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    return render(request, 'cadastrar_fundtecnico.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_fundtecnico(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atletas = Atleta.objects.get(id=atleta_id)

    controle_1 = request.POST.get('controle_1')
    controle_2 = request.POST.get('controle_2')
    controle_3 = request.POST.get('controle_3')
    passe_1 = request.POST.get('passe_1')
    passe_2 = request.POST.get('passe_2')
    passe_3 = request.POST.get('passe_3')
    conducao_1 = request.POST.get('conducao_1')
    conducao_2 = request.POST.get('conducao_2')
    conducao_3 = request.POST.get('conducao_3')
    chute_1 = request.POST.get('chute_1')
    chute_2 = request.POST.get('chute_2')
    chute_3 = request.POST.get('chute_3')
    teste = request.POST.get('teste')




    try:
       

        teste = get_object_or_404(Teste, id=int(teste))

        fundtecnico = Fundtecnico(controle_1 = controle_1, controle_2 = controle_2, controle_3 = controle_3,
                                  passe_1 = passe_1, passe_2 = passe_2, passe_3 = passe_3,
                                  conducao_1 = conducao_1, conducao_2 = conducao_2, conducao_3 = conducao_3,
                                    chute_1 = chute_1, chute_2 = chute_2, chute_3 = chute_3, teste = teste)
        fundtecnico.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora direito teste {teste}")


def home_fundtecnico(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_fundtecnico.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
