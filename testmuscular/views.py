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
from testmuscular.models import Testmuscular
from modalidade.models import Modalidade
from teste.models import Teste

def cadastrar_testmuscular(request, modalidade_id, atleta_id, teste_id):
    
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
    modalidade = Modalidade.objects.get(id = modalidade_id)
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'cadastrar_testmuscular.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id})


def valida_testmuscular(request, modalidade_id, atleta_id, teste_id):

    modalidade = Modalidade.objects.get(id=modalidade_id)
    
    instrutores = Instrutor.objects.all()
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor
    
    atletas = Atleta.objects.get(id=atleta_id)

    teste = request.POST.get('teste')
    abduquadrildir = request.POST.get('abduquadrildir')
    abduquadrilesq = request.POST.get('abduquadrilesq')
    rotquadrildir = request.POST.get('rotquadrildir')
    rotquadrilesq = request.POST.get('rotquadrilesq')
    flexplantardir = request.POST.get('flexplantardir')
    flexplantaresq = request.POST.get('flexplantaresq')
    flexjoelhodir = request.POST.get('flexjoelhodir')
    flexjoelhoesq = request.POST.get('flexjoelhoesq')
    exjoelhodir = request.POST.get('exjoelhodir')
    exjoelhoesq = request.POST.get('exjoelhoesq')



    try:
        

        teste = get_object_or_404(Teste, id=int(teste))

        testmuscular = Testmuscular(abduquadrildir = abduquadrildir, abduquadrilesq = abduquadrilesq,
                         rotquadrildir = rotquadrildir, rotquadrilesq = rotquadrilesq,
                          flexplantardir = flexplantardir, flexplantaresq = flexplantaresq,
                          flexjoelhodir = flexjoelhodir, flexjoelhoesq = flexjoelhoesq,
                          exjoelhodir = exjoelhodir, exjoelhoesq = exjoelhoesq, teste = teste)
        testmuscular.save()
        
        edit_url = reverse('lista_avaliacoes', args=[modalidade_id, atleta_id])
        edit_url_with_test_id = f'{edit_url}?teste_id={teste_id}'
        return redirect(edit_url_with_test_id)

    except:
        return HttpResponse(f"Deu fora teste {teste}")


def home_testmuscular(request, modalidade_id, atleta_id, teste_id):

    avaliacao2_url = {'avaliacao2_url': '/media/img/avaliacao2.png'}
    atleta = Atleta.objects.get(id = atleta_id)
    atletas = Atleta.objects.all()
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'home_testmuscular.html', {'atleta':atleta, 'atletas':atletas, 'instrutores':instrutores, 'status':status, 'instrutor_relacionado':instrutor_relacionado, 'teste_id':teste_id, 'modalidade_id':modalidade_id, 'avaliacao2_url':avaliacao2_url})
