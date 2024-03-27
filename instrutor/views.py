from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from instrutor.models import Instrutor, PerfilInstrutor
from . forms import CadastroInstrutor
from django.views.decorators.cache import never_cache 



def cadastrar_instrutor(request):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')

        form = CadastroInstrutor()
        perfis = PerfilInstrutor.objects.all().order_by('nome')
        
        return render(request, 'cadastro_instrutor.html',{'form': form, 'status': status, 'perfis': perfis})
    return redirect('/usuario/login/')

def valida_cadastro_instrutor(request):
    
    nome = request.POST.get('nome')
    identificador = request.POST.get('identificador')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    curso = request.POST.get('curso')
    endereco = request.POST.get('endereco')
    perfil = request.POST.get('perfil')

    instrutor_outros = Instrutor.objects.filter(identificador=identificador)
    if instrutor_outros.exists():
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=2')
        
    
    instrutor_outros = Instrutor.objects.filter(email=email)
    if instrutor_outros.exists():
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=3')

    try:
        perfis = get_object_or_404(PerfilInstrutor, id=int(perfil))

        instrutor = Instrutor (nome = nome, identificador = identificador, telefone = telefone, 
                     email = email, curso = curso,
                        endereco = endereco, perfil = perfis)
        instrutor.save()
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=0')
    except:
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=1')


def editar_instrutor(request, id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        perfis = PerfilInstrutor.objects.all().order_by('nome')
        status = request.GET.get('status')
        form = CadastroInstrutor()
        instrutor = Instrutor.objects.get(id=id)

        return render(request, 'editar_instrutor.html', {'status': status,'perfis': perfis, 'form': form, 'instrutor': instrutor})
    return redirect('/usuario/login/')

def valida_edicao_instrutor(request, id):

    instrutor = Instrutor.objects.get(id=id)
    status = request.GET.get('status')

    nome = request.POST.get('nome')
    identificador = request.POST.get('identificador')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    curso = request.POST.get('curso')
    endereco = request.POST.get('endereco')
    perfil = request.POST.get('perfil')

    instrutor_outros = Instrutor.objects.filter(identificador=identificador).exclude(id=instrutor.id)
    if instrutor_outros.exists():
        edit_url = reverse('editar_instrutor', args=[instrutor.id])
        return redirect(f'{edit_url}?status=2')
        
    
    instrutor_outros = Instrutor.objects.filter(email=email).exclude(id=instrutor.id)
    if instrutor_outros.exists():
        edit_url = reverse('editar_instrutor', args=[instrutor.id])
        return redirect(f'{edit_url}?status=3')
        
    
    
    try:
        
        perfis = get_object_or_404(PerfilInstrutor, id=perfil)

        instrutor.nome = nome
        instrutor.identificador = identificador
        instrutor.telefone = telefone
        instrutor.email = email
        instrutor.curso = curso
        instrutor.endereco = endereco
        instrutor.perfil = perfis
        instrutor.save()




        edit_url = reverse('editar_instrutor', args=[instrutor.id])
        return redirect(f'{edit_url}?status=6')
        
        
    except:
        edit_url = reverse('editar_instrutor', args=[instrutor.id])
        return redirect(f'{edit_url}?status=1')
        


def ver_instrutor(request, id):
    
    return render(request, 'visualizar_instrutor.html')

def cadastrar_perfil(request):
    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        return render(request, 'cadastro_perfil_instrutor.html',{'status': status})
    return redirect('/usuario/login/')

def validar_perfil(request):
    
    nome = request.POST.get('nome')

    
    perfil_outros = PerfilInstrutor.objects.filter(nome=nome)
    if perfil_outros.exists():
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=5')

    try:
        
        perfilInstrutor = PerfilInstrutor (nome = nome)
        perfilInstrutor.save()
        return redirect('/instrutor/cadastrar_perfil/?status=0')
        
    except:
        return redirect('/instrutor/cadastrar_perfil/?status=1')
        

def validar_perfil_2(request):
    
    nome = request.POST.get('nome')

    
    perfil_outros = PerfilInstrutor.objects.filter(nome=nome)
    if perfil_outros.exists():
        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=5')
    try:
        
        perfilInstrutor = PerfilInstrutor (nome = nome)
        perfilInstrutor.save()

        edit_url = reverse('cadastrar_instrutor')
        return redirect(f'{edit_url}?status=4')
        
    except:
        return HttpResponse(f"Erro ao realizar o cadastro" )




def excluir_perfil(request, id):
    pass

def editar_perfil(request, id):
    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        perfis = PerfilInstrutor.objects.get(id = id)

        return render(request, 'editar_perfil.html',{'status': status, 'perfil':perfis, 'status': status})
    return redirect('/usuario/login/')

def validar_edicao_perfil(request, id):
    
    perfil_id = request.POST.get('perfil_instrutor_id') 

    perfilInstrutor = PerfilInstrutor.objects.get(id=perfil_id)
    nome = request.POST.get('nome')
    status = request.GET.get('status')

    
    perfil_outros = PerfilInstrutor.objects.filter(nome=nome)
    if perfil_outros.exists():
        edit_url = reverse('editar_perfil', args=[perfilInstrutor.id])
        return redirect(f'{edit_url}?status=5')
    
    instrutor_do_perfil = Instrutor.objects.filter(perfil=perfilInstrutor)
    if instrutor_do_perfil.exists():
        edit_url = reverse('editar_perfil', args=[perfilInstrutor.id])
        return redirect(f'{edit_url}?status=6')
    
    try:
        
        
        perfilInstrutor.nome = nome
        perfilInstrutor.save()
        edit_url = reverse('editar_perfil', args=[perfilInstrutor.id])
        return redirect(f'{edit_url}?status=4')
        
    except:
        return redirect('/instrutor/cadastrar_perfil/?status=1')
        


@never_cache
def lista_instrutor(request):
    if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            instrutor = Instrutor.objects.filter().order_by('nome')

            return render(request, 'lista_instrutor.html', {'instrutor': instrutor})
    return redirect('/usuario/login/')        

@never_cache
def lista_perfil(request):
    if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            perfis = PerfilInstrutor.objects.all().order_by('nome')
            perfis_com_qtd_instrutor = []

            for perfil in perfis:
                qtd_instrutor = Instrutor.objects.filter(perfil=perfil).count()
                perfis_com_qtd_instrutor.append((perfil, qtd_instrutor))

            return render(request, 'lista_perfil.html', {'perfis_com_qtd_instrutor': perfis_com_qtd_instrutor})
    return redirect('/usuario/login/')        

def lista_membros_perfil(request,id):
    

    perfilInstrutor = PerfilInstrutor.objects.get(id=id)
    instrutor_do_perfil = Instrutor.objects.filter(perfil=perfilInstrutor).order_by('nome')
    

    return render(request, 'lista_membros_perfis.html', {'instrutor_do_perfil':instrutor_do_perfil, 'perfilInstrutor':perfilInstrutor})