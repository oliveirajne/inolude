from django.shortcuts import render, redirect
from .models import Processo



def list_processos(request):
    processos = Processo.objects.all()
    return render(request, 'processos.html', {'processos': processos})

