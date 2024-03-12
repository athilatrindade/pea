from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
import re
from django.core.validators import validate_email 
from django.core.exceptions import ValidationError 
from datetime import date
from . forms import CadastroUsuario
from instrutor.models import Instrutor
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.views.decorators.cache import never_cache

@never_cache
def home(request): 

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
  
        
        usuario = Usuario.objects.get(id=request.session['usuario'])
        usuario_id = request.session.get('usuario')
        
        imagens = {
            'atleta_url': '/media/img/atleta.png',
            'instrutor_url': '/media/img/instrutor.png',
            'modalidade_url': '/media/img/modalidade.png',
            'perfil_url': '/media/img/perfil_instrutor.png',
            'usuario_url': '/media/img/usuarios.png',
            'editar_usuario_url': '/media/img/editar_usuario.png',
            'consultas_url':'/media/img/consulta.png',
            'teste_url': '/media/img/teste.png',
            'painel_url': '/media/img/painel.png',
            'usuario_admin': usuario.administrador,
            'usuario_id': usuario_id
        }

        if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            imagens['usuario_id'] = usuario_id

            return render(request, 'inicial.html', imagens)
        else:
            return redirect('/usuario/login/?status=2')
    else:
        return redirect('/usuario/login/') 


def cadastrar_usuario(request): 
   
    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        status = request.GET.get('status')

        form = CadastroUsuario()
        instrutores = Instrutor.objects.all()

        
        return render(request, 'cadastro_usuario.html', {'status': status, 'form': form, 'instrutores': instrutores})
    return redirect('/usuario/login/')   
    
def valida_cadastro_usuario(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    ativado = request.POST.get('ativado')
    senha = request.POST.get('senha')
    instrutor_id = request.POST.get('instrutor')
    administrador = request.POST.get('administrador')

    usuario = Usuario.objects.filter(email = email)
    instrutor = get_object_or_404(Instrutor, id=int(instrutor_id))

    status = request.GET.get('status')
    
    
    if not valida_cpf(cpf) == 0:
        return redirect('/usuario/cadastrar/?status=5')
        
    
    
    usuario_outros = Usuario.objects.filter(cpf=cpf)
    print("CPF duplicado")
    if usuario_outros.exists():
        edit_url = reverse('cadastrar_usuario')
        return redirect(f'{edit_url}?status=7')
    
    
    email_outros = Usuario.objects.filter(email=email)
    print("Email duplicado")
    if email_outros.exists():
        edit_url = reverse('cadastrar_usuario')
        return redirect(f'{edit_url}?status=8')
    
    
    instrutor_outros = Usuario.objects.filter(instrutor=instrutor)
    print("Instrutor inválido")
    if instrutor_outros.exists():
        edit_url = reverse('cadastrar_usuario')
        return redirect(f'{edit_url}?status=9')
    


    
    try:
        validate_email(email)
    except ValidationError:
        return redirect('/usuario/cadastrar/?status=6')

    
    usuario = Usuario.objects.filter(cpf=cpf)

    if len(cpf.strip()) == 0 or len(email.strip()) == 0:
    
        return redirect('/usuario/cadastrar/?status=1')
    
    if len(senha) < 8:
        return redirect('/usuario/cadastrar/?status=2')

    if len(usuario)>0:
        return redirect('/usuario/cadastrar/?status=3')
    
    
    cpf = re.sub(r'[^0-9]', '', cpf)   
    try:
        
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, cpf = cpf, email = email, 
                     telefone = telefone, ativado = ativado,
                        senha = senha, instrutor = instrutor, administrador = administrador)
        usuario.save()
        return redirect('/usuario/cadastrar/?status=0')
    
    except:
        return redirect('/usuario/cadastrar/?status=4')
        
    
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

def is_admin(usuario_id): 
    usuario = Usuario.objects.get(id=usuario_id)
    return usuario.administrador

@never_cache
def editar_usuario(request, id):

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        usuario = Usuario.objects.get(id=id)
        instrutores = Instrutor.objects.all()
        status = request.GET.get('status')

        
        usuario_id_logado = request.session.get('usuario')
        if not is_admin(usuario_id_logado):
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")


        
        if request.method == 'POST':
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            ativado = request.POST.get('ativado')
            senha = request.POST.get('senha')
            instrutor_id = request.POST.get('instrutor')
            administrador = request.POST.get('administrador')

            
            instrutor = get_object_or_404(Instrutor, id=int(instrutor_id))
            senha = sha256(senha.encode()).hexdigest()
            
            usuario.nome = nome
            usuario.cpf = cpf
            usuario.email = email
            usuario.telefone = telefone
            usuario.ativado = ativado
            usuario.senha = senha
            usuario.instrutor = instrutor
            usuario.administrador = administrador
            usuario.save()

            
            return redirect('/usuario/home/?status=0')        
        return render(request, 'editar_usuario.html', {'usuario': usuario, 'instrutores': instrutores, 'status':status})
    return redirect('/usuario/login/')

@login_required
def valida_edicao_meuusuario(request): 
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    ativado = request.POST.get('ativado')
    senha = request.POST.get('senha')
    instrutor_id = request.POST.get('instrutor')
    administrador = request.POST.get('administrador')

    usuario = request.user  

    status = request.GET.get('status')

    
    try:
        validate_email(email)
    except ValidationError:
        return redirect('/usuario/editar/?status=6')

    
    if not valida_cpf(cpf):
        return redirect('/usuario/editar/?status=5')

    
    usuario_outros = Usuario.objects.filter(email=email).exclude(id=usuario.id)
    if usuario_outros.exists():
        return redirect('/usuario/editar/?status=3')

    if len(senha) < 8:
        return redirect('/usuario/editar/?status=2')

    try:
        instrutor = get_object_or_404(Instrutor, id=int(instrutor_id))
        senha = sha256(senha.encode()).hexdigest()

        
        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.telefone = telefone
        usuario.ativado = ativado
        usuario.senha = senha
        usuario.instrutor = instrutor
        usuario.administrador = administrador
        usuario.save()

        return redirect('/usuario/home/?status=0')

    except:
        return redirect('/usuario/editar/?status=4')


 
def valida_edicao_usuario_qualquer(request, id): 

    usuario = Usuario.objects.get(id=id)
    
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    ativado = request.POST.get('ativado')
    senha = request.POST.get('senha')
    instrutor = request.POST.get('instrutor')
    administrador = request.POST.get('administrador')

    status = request.GET.get('status')

    
    
    if len(senha) < 8:
        return redirect('/usuario/editar/?status=2')

    if not valida_cpf(cpf) == 0:
        return redirect('/usuario/editar/?status=5')

    
    try:
        validate_email(email)
    except ValidationError:
        return redirect('/usuario/editar/?status=6')

    usuario_outros = Usuario.objects.filter(cpf=cpf).exclude(id=usuario.id)
    print("CPF duplicado")
    print (usuario)
    if usuario_outros.exists():
        edit_url = reverse('editar_usuario', args=[usuario.id])
        return redirect(f'{edit_url}?status=7')
    
    email_outros = Usuario.objects.filter(email=email).exclude(id=usuario.id)
    print("Email duplicado")
    if email_outros.exists():
        edit_url = reverse('editar_usuario', args=[usuario.id])
        return redirect(f'{edit_url}?status=8')
    
    
    instrutor_outros = Usuario.objects.filter(instrutor=instrutor).exclude(id=usuario.id)
    print("Instrutor inválido")
    if instrutor_outros.exists():
        edit_url = reverse('editar_usuario', args=[usuario.id])
        return redirect(f'{edit_url}?status=9')


    instrutores = get_object_or_404(Instrutor, id=int(instrutor))
    senha = sha256(senha.encode()).hexdigest()

    
    usuario.nome = nome
    usuario.cpf = cpf
    usuario.email = email
    usuario.telefone = telefone
    usuario.ativado = ativado
    usuario.senha = senha
    usuario.instrutor = instrutores
    usuario.administrador = administrador
    usuario.save()

    
    edit_url = reverse('editar_usuario', args=[usuario.id])
    return redirect(f'{edit_url}?status=0')
    


def login(request):
    if request.session.get('usuario'):
        return redirect('/usuario/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status})



def valida_login_usuario(request): 
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/usuario/login/?status=1')
        
    elif len(usuario) > 0: 
        request.session['usuario'] = usuario[0].id
        return redirect(f'/usuario/home/?id_usuario= {request.session["usuario"]}')
    
@never_cache
def sair(request): 
    request.session.flush()
    return redirect('/usuario/login/')

@never_cache
def ver_meu_cad(request, id):
    if request.session.get('usuario') == id:
        request.session.get('usuario')
        status = request.GET.get('status')
        usuario = Usuario.objects.get(id = id)
    else:
        return HttpResponse(f"Você não tem permissão para editar esse usuário.")
    
    return render(request, 'meucadastro_func.html', {'usuario': usuario, 'id_usuario':id})
    
@never_cache
def editar_meu_cad(request, id): 

    if request.session.get('usuario'):
        usuario_id = request.session.get('usuario')
        user_id = request.user.id
        request.session.get('usuario')
        usuario = Usuario.objects.get(id = request.session['usuario'])

        
        usuario_id = request.session.get('usuario')
        imagens = {
            'usuario_admin': usuario.administrador,
            'usuario_id': usuario_id,
            'usuario': usuario
        }

        
        if request.method == 'POST':
            
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            ativado = request.POST.get('ativado')
            senha = request.POST.get('senha')
            instrutor_id = request.POST.get('instrutor')
            administrador = request.POST.get('administrador')
                
            instrutor = get_object_or_404(Instrutor, id=instrutor_id)

            
            usuario.nome = nome
            usuario.cpf = cpf
            usuario.email = email
            usuario.telefone = telefone
            usuario.ativado = ativado
            usuario.senha = sha256(senha.encode()).hexdigest()
            usuario.instrutor = instrutor
            usuario.administrador = administrador
            usuario.save()

            return redirect(f'/usuario/home/')    
        return render(request, 'editar_meu_cad.html', imagens)
    return redirect('/usuario/login/')

def lista_usuario(request):
    usuario = Usuario.objects.filter().order_by('nome')

    return render(request, 'lista_usuario.html', {'usuario': usuario})



    


   