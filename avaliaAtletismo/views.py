from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from avaliaAtletismo.models import AvaliaAtletismo

def cadastrar_avaliacao(request):

    status = request.GET.get('status')
    return render(request, 'cadastro_avaliacao_atle.html', {'status': status})


def valida_cad_avaliacao(request):

    atleta = request.POST.get('atleta')
    data = request.POST.get('data')
   

    try:
        avaliaAtletismo = AvaliaAtletismo(atleta = atleta, data = data)
        avaliaAtletismo.save()
    except:
        return HttpResponse(f" except  atleta {atleta} data {data}")
    


def editar_avaliacao(request, id):

    pass

def ver_avaliacao(request, id):
    pass