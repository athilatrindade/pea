from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db import models
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
    if request.session.get('usuario'):
            usuario_id = request.session.get('usuario')
            
            imagens = {
                'atleta_url': '/media/img/atleta.png',
                'instrutor_url': '/media/img/instrutor.png',
                'modalidade_url': '/media/img/modalidade.png',
                'perfil_url': '/media/img/perfil_instrutor.png',
                'usuario_url': '/media/img/usuario.png'
            }
            imagens['usuario_id'] = usuario_id
            response = HttpResponse(f"Página expirada, faça login para entrar novamente.")
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1
            response['Pragma'] = 'no-cache'  # HTTP 1.0
            response['Expires'] = '0'  # Proxies    
            return render(request, 'inicial.html', imagens)
    
    response = HttpResponse(f"Página expirada, faça login para entrar novamente.")
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1
    response['Pragma'] = 'no-cache'  # HTTP 1.0
    response['Expires'] = '0'  # Proxies        
    return redirect('/usuario/login/')

