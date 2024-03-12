from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from atleta.models import Atleta, Modalidade
from usuario.models import Usuario
from modalidade_historico.models import Modalidades_atleta
from . forms import CadastroAtleta
from django import forms
from hashlib import sha256
import re
from django.core.validators import validate_email 
from django.core.exceptions import ValidationError
from django.views.decorators.cache import never_cache 


def cadastrar_atleta(request): 
    
    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        
        form = CadastroAtleta()
        modalidades = Modalidade.objects.all().order_by('nome')
        modalidades_atleta = Modalidades_atleta.objects.all()

        return render(request, 'cadastro_atleta.html', {'form': form, 'status': status,'modalidades': modalidades, 'modalidades_atleta':modalidades_atleta})
    return redirect('/usuario/login/')

def valida_cadastro_atleta(request):
    nome = request.POST.get('nome')
    celular = request.POST.get('celular')
    data_nasc = request.POST.get('data_nasc')
    cel_resp = request.POST.get('cel_resp')
    grau_instrucao = request.POST.get('grau_instrucao')
    origem_escolar = request.POST.get('origem_escolar')
    cpf = request.POST.get('cpf')
    sexo = request.POST.get('sexo')

    status = request.GET.get('status')
    
    if not valida_cpf(cpf) == 0:
        cadastro_url = reverse('cadastrar_atleta')
        return redirect(f'{cadastro_url}?status=2')
        
    atleta_outros = Atleta.objects.filter(cpf=cpf)
    if atleta_outros.exists():
        cpf_url = reverse('cadastrar_atleta')
        return redirect(f'{cpf_url}?status=3')
        
    cpf = re.sub(r'[^0-9]','',cpf)    
    try:
        
        atleta = Atleta(nome = nome, celular = celular, data_nasc = data_nasc, 
                     cel_resp = cel_resp, grau_instrucao = grau_instrucao,
                        origem_escolar = origem_escolar, cpf = cpf, sexo = sexo)
        atleta.save()

        return redirect('/atleta/cadastrar/?status=0')
        
    except:
        return redirect('/atleta/cadastrar/?status=1')
        
        

def editar_atleta(request, id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        atleta = Atleta.objects.get(id=id)
        
        modalidades = Modalidade.objects.all().order_by('nome')
        modalidades_atleta = Modalidades_atleta.objects.all()
        return render(request, 'editar_atleta.html', {'atleta': atleta, 'status': status, 'modalidades':modalidades, 'modalidades_atleta':modalidades_atleta})
    return redirect('/usuario/login/')

def valida_cpf(cpf):
    # Extrai somente os números do CPF, removendo traços e pontos
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica se os dígitos calculados são iguais aos informados
    if cpf[-2:] == f'{digito1}{digito2}':
        return False
    else:
        return True


def valida_edicao_atleta(request,id):

    atleta = Atleta.objects.get(id=id)
    status = request.GET.get('status')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        celular = request.POST.get('celular')
        data_nasc = request.POST.get('data_nasc')
        cel_resp = request.POST.get('cel_resp')
        grau_instrucao = request.POST.get('grau_instrucao')
        origem_escolar = request.POST.get('origem_escolar')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
    
        
        if not valida_cpf(cpf) == 0:
            edit_url = reverse('editar_atleta', args=[atleta.id])
            return redirect(f'{edit_url}?status=5')

        
        atleta_outros = Atleta.objects.filter(cpf=cpf).exclude(id=atleta.id)
        print("CPF duplicado")
        if atleta_outros.exists():
            edit_url = reverse('editar_atleta', args=[atleta.id])
            return redirect(f'{edit_url}?status=3')
            

        try:
            atleta.nome = nome
            atleta.celular = celular
            atleta.data_nasc = data_nasc
            atleta.cel_resp = cel_resp
            atleta.grau_instrucao = grau_instrucao
            atleta.origem_escolar = origem_escolar
            atleta.cpf = cpf
            atleta.sexo = sexo
            atleta.save()

            edit_url = reverse('editar_atleta', args=[atleta.id])
            return redirect(f'{edit_url}?status=2')
            
        except:
            
            return HttpResponse (f" Status 4 {nome} {celular} {data_nasc} {cel_resp} {grau_instrucao} {origem_escolar} {cpf} {sexo} {atleta.modalidade_atleta}")



@never_cache  
def ver_atletas(request): 
    atleta = Atleta.objects.filter().order_by('nome')

    modalidades_atletas = Modalidades_atleta.objects.select_related('modalidade').order_by('atleta__nome')

    return render(request, 'lista_atleta.html', {'atleta': atleta, 'modalidades_atletas': modalidades_atletas})


def visualizar_atleta(request,id):

    pass


