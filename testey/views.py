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
from testey.models import Testey
from teste.models import Teste
from modalidade.models import Modalidade


def cadastrar_testey(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'cadastrar_testey.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_testey(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    atletas = Atleta.objects.get(id=atleta_id)

    anterior_direito_1 = request.POST.get('anterior_direito_1')
    anterior_direito_2 = request.POST.get('anterior_direito_2')
    anterior_direito_3 = request.POST.get('anterior_direito_3')
    anterior_esquerdo_1 = request.POST.get('anterior_esquerdo_1')
    anterior_esquerdo_2 = request.POST.get('anterior_esquerdo_2')
    anterior_esquerdo_3 = request.POST.get('anterior_esquerdo_3')
    postero_medial_dir_1 = request.POST.get('postero_medial_dir_1')
    postero_medial_dir_2 = request.POST.get('postero_medial_dir_2')
    postero_medial_dir_3 = request.POST.get('postero_medial_dir_3')
    postero_medial_esq_1 = request.POST.get('postero_medial_esq_1')
    postero_medial_esq_2 = request.POST.get('postero_medial_esq_2')
    postero_medial_esq_3 = request.POST.get('postero_medial_esq_3')
    postero_lat_esq_1 = request.POST.get('postero_lat_esq_1')
    postero_lat_esq_2 = request.POST.get('postero_lat_esq_2')
    postero_lat_esq_3 = request.POST.get('postero_lat_esq_3')
    postero_lat_dir_1 = request.POST.get('postero_lat_dir_1')
    postero_lat_dir_2 = request.POST.get('postero_lat_dir_2')
    postero_lat_dir_3 = request.POST.get('postero_lat_dir_3')
    teste = request.POST.get('teste')


    try:
        

        teste = get_object_or_404(Teste, id=int(teste))

        testey = Testey(anterior_direito_1 = anterior_direito_1, anterior_direito_2 = anterior_direito_2,
                         anterior_direito_3 = anterior_direito_3, anterior_esquerdo_1 = anterior_esquerdo_1,
                         anterior_esquerdo_2 = anterior_esquerdo_2, anterior_esquerdo_3 = anterior_esquerdo_3,
                          postero_medial_dir_1 = postero_medial_dir_1, postero_medial_dir_2 = postero_medial_dir_2,
                          postero_medial_dir_3 = postero_medial_dir_3, postero_medial_esq_1 = postero_medial_esq_1,
                           postero_medial_esq_2 = postero_medial_esq_2, postero_medial_esq_3 = postero_medial_esq_3,
                            postero_lat_esq_1 = postero_lat_esq_1, postero_lat_esq_2 = postero_lat_esq_2,
                             postero_lat_esq_3 = postero_lat_esq_3, postero_lat_dir_1 = postero_lat_dir_1,
                              postero_lat_dir_2 = postero_lat_dir_2, postero_lat_dir_3 = postero_lat_dir_3, teste = teste)
        testey.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora teste {teste}")


def home_testey(request, modalidade_id, atleta_id, teste_id):
    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_testey.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
