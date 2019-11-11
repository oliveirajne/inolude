from django.shortcuts import render, redirect
from .models import Processo
from .forms import ProcessoForm



def list_processos(request):
    processos = Processo.objects.all()
    return render(request, 'processos.html', {'processos': processos})

def create_processo(request):
    form = ProcessoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Processos:list_processos')

    return render(request, 'form-processos.html', {'form': form})

def update_processo(request, id):
    processo = Processo.objects.get(id=id)
    form = ProcessoForm(request.POST or None, instance=processo)

    if form.is_valid():
        form.save()
        return redirect('Processos:list_processos')

    return render(request, 'form-processos.html', {'form': form, 'processo': processo})

def delete_processo(request, id):
    processo = Processo.objects.get(id=id)

    if request.method == 'POST':
        processo.delete()
        return redirect('Processos:list_processos')

    return render(request, 'delete-processo.html', {'processo': processo})


