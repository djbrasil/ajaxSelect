from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import solicitacaoForm
from .models import Empresas, Solicitacao, Endereco


def solicitacao_create_view(request):
    form = solicitacaoForm() 
    if request.method == 'POST':
        form = solicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitacao_add') 
    return render(request, 'end/home.html', {'form': form})


def solicitacao_update_view(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    form = solicitacaoForm(instance=solicitacao)
    if request.method == 'POST':
        form = solicitacaoForm(request.POST, instance=solicitacao)
        if form.is_valid():
            form.save()
            return redirect('solicitacao_change', pk=pk)
    return render(request, 'end/home.html', {'form': form})


# AJAX
def load_empresas(request):
    empresas_id = request.GET.get('empresas_id')
    enderecos = Endereco.objects.filter(empresas_id=empresas_id).all()
    return render(request, 'end/enderecos.html', {'enderecos': enderecos})

