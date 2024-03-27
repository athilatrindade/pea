from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from modalidade.models import Modalidade
from modalidade_historico.models import Modalidades_atleta
from atleta.models import Atleta
from django.db.models import Count
from django.http import HttpResponseRedirect
from usuario.models import Usuario
from django.db.models import Max
from django.views.decorators.cache import never_cache 



def cadastrar_modalidade(request):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')
        
        last_modalidade = Modalidade.objects.aggregate(Max('id'))
        next_id = last_modalidade['id__max'] + 1 if last_modalidade['id__max'] else 1

        
        codigo = f'{next_id:03}'

        return render(request, 'cadastro_modalidade.html', {'status': status, 'codigo':codigo})
    return redirect('/usuario/login/')

def valida_cadastro_modalidade(request):
    
    status = request.GET.get('status')
    
    codigo = request.POST.get('codigo')
    nome = request.POST.get('nome')
    
    
    modalidade_outros = Modalidade.objects.filter(codigo=codigo)
    print("Código modalidade duplicada")
    if modalidade_outros.exists():
        cadastra_url = reverse('cadastrar_modalidade')
        return redirect(f'{cadastra_url}?status=3')
    
    modalidade_outros = Modalidade.objects.filter(nome=nome)
    print("Nome modalidade duplicada")
    if modalidade_outros.exists():
        cadastra_url = reverse('cadastrar_modalidade')
        return redirect(f'{cadastra_url}?status=4')
    

    try:
        modalidade = Modalidade(codigo = codigo, nome = nome)
        modalidade.save()

        
        cadastra_url = reverse('cadastrar_modalidade')
        return redirect(f'{cadastra_url}?status=0')
    except:
        cadastra_url = reverse('cadastrar_modalidade')
        return redirect(f'{cadastra_url}?status=1')


def editar_modalidade(request, id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        modalidade = Modalidade.objects.get(id=id)
        status = request.GET.get('status')
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        return render(request, 'editar_modalidade.html', {'status':status, 'modalidade':modalidade})
    return redirect('/usuario/login/')

def valida_edicao_modalidade(request,id):

    modalidade = Modalidade.objects.get(id=id)
    status = request.GET.get('status')
    
    codigo = request.POST.get('codigo')
    nome = request.POST.get('nome')
    
    
    modalidade_outros = Modalidade.objects.filter(codigo=codigo).exclude(id=modalidade.id)
    print("Código modalidade duplicada")
    if modalidade_outros.exists():
        cadastra_url = reverse('editar_modalidade', args=[modalidade.id])
        return redirect(f'{cadastra_url}?status=3')
    
    modalidade_outros = Modalidade.objects.filter(nome=nome)
    print("Nome modalidade duplicada")
    if modalidade_outros.exists():
        cadastra_url = reverse('editar_modalidade', args=[modalidade.id])
        return redirect(f'{cadastra_url}?status=4')

    atletas_da_modalidade = Modalidades_atleta.objects.filter(modalidade=modalidade)
    if atletas_da_modalidade.exists():
        cadastra_url = reverse('editar_modalidade', args=[modalidade.id])
        return redirect(f'{cadastra_url}?status=5')

    try:
        modalidade.codigo = codigo
        modalidade.nome = nome
        modalidade.save()

        
        cadastra_url = reverse('editar_modalidade', args=[modalidade.id])
        return redirect(f'{cadastra_url}?status=0')
    except:
        cadastra_url = reverse('editar_modalidade', args=[modalidade.id])
        return redirect(f'{cadastra_url}?status=1')

def excluir_modalidade(request, id):
    pass

@never_cache
def lista_modalidade(request):
    if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            modalidades = Modalidade.objects.all().order_by('nome')
            modalidades_com_qtd_atletas = []

            for modalidade in modalidades:
               qtd_atletas = Modalidades_atleta.objects.filter(modalidade=modalidade, ativo=True).count()
               modalidades_com_qtd_atletas.append((modalidade, qtd_atletas))



            return render(request, 'lista_modalidade.html', {'modalidades_com_qtd_atletas': modalidades_com_qtd_atletas})
    return redirect('/usuario/login/')        


def lista_membros(request,id):
   
    modalidade = Modalidade.objects.get(id=id)
    membros_da_modalidade = Modalidades_atleta.objects.filter(modalidade=modalidade, ativo=True).select_related('atleta').order_by('atleta__nome')
    
    return render(request, 'lista_membros.html', {'modalidade': modalidade, 'membros_da_modalidade': membros_da_modalidade})

def lista_atletas(request, id):

    atleta = Atleta.objects.all().order_by('nome')
    atleta_id = Atleta.objects.all().order_by('id')
    modalidade = Modalidade.objects.get(id=id)
    modalidade_id = modalidade
  
    return render(request, 'lista_atletas.html', {'modalidade': modalidade, 'atleta':atleta, 'modalidade_id':modalidade_id, 'atleta_id':atleta_id})

def adicionar_modalidade(request, modalidade_id, atleta_id):
    status = request.GET.get('status')
    modalidade = Modalidade.objects.get(id=modalidade_id)
    atleta = Atleta.objects.get(id=atleta_id)
    modalidades = Modalidade.objects.all().order_by('nome')

    
    modalidades_do_atleta = Modalidades_atleta.objects.filter(atleta=atleta)

    modalidades_vinculadas = set(modalidades_do_atleta.filter(ativo=True).values_list('modalidade__id', flat=True))

    return render(request, 'modalidade_do_atleta.html', {
        'modalidade': modalidade,
        'atleta': atleta,
        'modalidade_id': modalidade_id,
        'atleta_id': atleta_id,
        'modalidades': modalidades,
        'modalidades_vinculadas': modalidades_vinculadas,
        'status': status,
    })

def valida_adicionar_modalidade(request, modalidade_id, atleta_id):
    status = 0
    modalidade = Modalidade.objects.get(id=modalidade_id)
    atleta = Atleta.objects.get(id=atleta_id)

    if request.method == 'POST':
        modalidades_selecionadas = request.POST.getlist('modalidades')
        
        
        modalidades_do_atleta = Modalidades_atleta.objects.filter(atleta=atleta)
        
        
        modalidades_selecionadas_ids = set(map(int, modalidades_selecionadas))
        
        
        for modalidade_atleta in modalidades_do_atleta:
            
            if modalidade_atleta.modalidade_id not in modalidades_selecionadas_ids:
                
                modalidade_atleta.ativo = False
                modalidade_atleta.save()
        
        for modalidade_id in modalidades_selecionadas:
            modalidade_id = int(modalidade_id)
            
            
            if not modalidades_do_atleta.filter(modalidade_id=modalidade_id).exists():
                modalidade_atleta = Modalidades_atleta(
                    modalidade=Modalidade.objects.get(id=modalidade_id),
                    atleta=atleta,
                    usuario= Usuario.objects.get(id=request.session['usuario']),
                    ativo=True,
                )
                modalidade_atleta.save()
                
        url_redirecionamento = reverse('lista_atletas', args=[modalidade_id])
        url_redirecionamento += f'?status={status}'
        return HttpResponseRedirect(url_redirecionamento)

    modalidades = Modalidade.objects.all() 

    return render(request, 'modalidade_do_atleta.html', {
        'modalidade': modalidade,
        'atleta': atleta,
        'modalidades': modalidades,
        'modalidade_id': modalidade_id,
        'atleta_id': atleta_id,
        'status':status,
    })