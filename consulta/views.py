
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from consulta.models import Consulta
from atleta.models import Atleta
from instrutor.models import Instrutor
from usuario.models import Usuario
from atleta.models import Atleta
from . import forms
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max

def home_consulta(request,id):
    status = request.GET.get('status')
    atleta = Atleta.objects.get(id= id)
    if request.session.get('usuario'):
                
        usuario = Usuario.objects.get(id=request.session['usuario'])
        usuario_id = request.session.get('usuario')
        
        imagens = {
            'lista_consulta_url': '/media/img/consulta_nova.png',
            'historico_consulta_url': '/media/img/consulta_historico.png',
            'usuario_admin': usuario.administrador,
            'usuario_id': usuario_id,
            'atleta' : atleta,
        
        }

        if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            imagens['usuario_id'] = usuario_id
            
            return render(request, 'home_consulta.html', imagens)
        else:
            return redirect('/usuario/login/?status=2')

    else:
        return redirect('/usuario/login/') 


def cadastrar_consulta(request, id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        atleta = Atleta.objects.get(id = id)
        atletas = Atleta.objects.all()
        instrutores = Instrutor.objects.all()
    
        status = request.GET.get('status')

        usuario = Usuario.objects.get(id=request.session['usuario'])
        instrutor_relacionado = usuario.instrutor

        
        last_consulta = Consulta.objects.aggregate(Max('id'))
        next_id = last_consulta['id__max'] + 1 if last_consulta['id__max'] else 1

        
        codigo = f'{next_id:03}'

        return render(request, 'cadastro_consulta.html', {'status': status,'atletas': atletas, 'instrutores': instrutores, 'instrutor_relacionado':instrutor_relacionado, 'atleta' : atleta, 'codigo':codigo})
    return redirect('/usuario/login/')

def valida_cad_consulta(request):

    numero = request.POST.get('numero')
    data = request.POST.get('data')
    receituario = request.POST.get('receituario')
    relato = request.POST.get('relato')
    atleta = request.POST.get('atleta')
    instrutor = request.POST.get('instrutor')
    sigilo = request.POST.get('sigilo')
    

    try:
        atletas = get_object_or_404(Atleta, id=int(atleta))
        instrutores = get_object_or_404(Instrutor, id=int(instrutor))

        consulta = Consulta(numero = numero, data = data, receituario = receituario, 
                     relato = relato, atleta = atletas,
                        instrutor = instrutores, sigilo = sigilo)
        consulta.save()
        return redirect(reverse('cadastrar_consulta', args=[atletas.id]) + f'?status=0')
    except:
        return redirect(reverse('cadastrar_consulta', args=[atletas.id]) + f'?status=1')
        


def editar_consulta(request, atleta_id, consulta_id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        atleta = Atleta.objects.get(id=atleta_id)

        consultas = Consulta.objects.filter(atleta=atleta)
        
        instrutores = Instrutor.objects.all()
        
        status = request.GET.get('status')

        consulta = Consulta.objects.get(id=consulta_id)
        instrutor_relacionado = consulta.instrutor

        usuario = Usuario.objects.get(id=request.session['usuario'])
        instrutor = consulta.instrutor
        instrutor_logado = usuario.instrutor
        print('instrutor', usuario.instrutor)
        print('consulta', consulta.id)
        if instrutor_logado == instrutor:
            
            return render(request, 'editar_consulta.html', {'status': status, 'consulta': consulta, 'atleta':atleta})
        else:
            
            edit_url = reverse('ver_consulta', args=[atleta.id, consulta.id])
            return redirect(f'{edit_url}?status=2')
    return redirect('/usuario/login/')

def ver_consulta(request, atleta_id, consulta_id):
    atleta = Atleta.objects.get(id=atleta_id)
    consultas = Consulta.objects.filter(atleta=atleta)
    
    instrutores = Instrutor.objects.all()
    
    status = request.GET.get('status')

    consulta = Consulta.objects.get(id=consulta_id)
    instrutor_relacionado = consulta.instrutor
    sigilo = consulta.sigilo
    print('tem sigilo', sigilo)
    
    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor = consulta.instrutor
    instrutor_logado = usuario.instrutor

    sigilo = consulta.sigilo

    if instrutor_logado != instrutor and sigilo==False:
    
        return render(request, 'ver_consulta.html', {'status': status, 'atleta': atleta, 'consultas': consultas, 'instrutor_relacionado': instrutor_relacionado, 'consulta':consulta, 'sigilo':sigilo})
    if instrutor_logado == instrutor:
        return render(request, 'ver_consulta.html', {'status': status, 'atleta': atleta, 'consultas': consultas, 'instrutor_relacionado': instrutor_relacionado, 'consulta':consulta, 'sigilo':sigilo})
    

    edit_url = reverse('historico_consulta', args=[atleta_id])
    return redirect(f'{edit_url}?status=1')
    

def historico_consulta(request,id):
    atleta = Atleta.objects.get(id = id)
    consultas = Consulta.objects.filter(atleta=atleta).order_by('criado')
    status = request.GET.get('status')
    usuario_logado = Usuario.objects.get(id=request.session['usuario'])

    usuario = Usuario.objects.get(id=request.session['usuario'])
       
    try:
        consulta = Consulta.objects.get(id=id)
        instrutor_relacionado = consulta.instrutor
        sigilo = consulta.sigilo
        
    except ObjectDoesNotExist:
        consulta = None
        instrutor_relacionado = None
        sigilo = None
        

    instrutor_logado = usuario.instrutor
    

    return render(request, 'historico_consulta.html', {'status': status, 'atleta' : atleta, 'consultas':consultas, 'usuario_logado':usuario_logado, 'sigilo':sigilo, 'instrutor_logado':instrutor_logado,'instrutor_relacionado':instrutor_relacionado})

def busca_atleta_consulta(request):
    status = request.GET.get('status')

    atletas = Atleta.objects.all().order_by('nome')
    instrutores = Instrutor.objects.all()
   
    status = request.GET.get('status')

    usuario = Usuario.objects.get(id=request.session['usuario'])
    instrutor_relacionado = usuario.instrutor

    return render(request, 'busca_atleta.html', {'status': status,'atletas': atletas, 'instrutores': instrutores, 'instrutor_relacionado':instrutor_relacionado})

def valida_edit_consulta(request, atleta_id, consulta_id):

    consulta = Consulta.objects.get(id=consulta_id)

    atleta = Atleta.objects.get(id=atleta_id)
    consultas = Consulta.objects.filter(atleta=atleta)
    
    status = request.GET.get('status')

    consulta = Consulta.objects.get(id=consulta_id)

    numero = request.POST.get('numero')
    data = request.POST.get('data')
    receituario = request.POST.get('receituario')
    relato = request.POST.get('relato')
    atleta = request.POST.get('atleta')
    instrutor = request.POST.get('instrutor')
    sigilo = request.POST.get('sigilo')
    

    try:
        atletas = get_object_or_404(Atleta, id=int(atleta))
        instrutores = get_object_or_404(Instrutor, id=int(instrutor))

        consulta.numero = numero
        consulta.data = data
        consulta.receituario = receituario
        consulta.relato = relato
        consulta.atleta = atletas
        consulta.instrutor = instrutores
        consulta.sigilo = sigilo

        consulta.save()
        edit_url = reverse('editar_consulta', args=[atleta_id, consulta_id])
        return redirect(f'{edit_url}?status=3')
       
    except:
        edit_url = reverse('editar_consulta', args=[atleta_id, consulta_id])
        return redirect(f'{edit_url}?status=4')
        