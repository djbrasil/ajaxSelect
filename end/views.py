from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages  
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView  
from django.shortcuts import render 
from django.template.defaultfilters import slugify
from .forms import solicitacaoForm
from .models import Empresas, Solicitacao, Endereco



class SolicitacaoCreate(CreateView):
    model = Solicitacao 
    form_class = solicitacaoForm 
    template_name = 'end/home.html' 

    def get(self, request): 
        form = solicitacaoForm() 
        solicitacao = Solicitacao.objects.all() 
        context = { 'solicitacao':solicitacao, 'form':form}  
        return render(request, self.template_name, context)
      
    def post(self, request, *args, **kwargs):   
        form = solicitacaoForm(request.POST)   
        if form.is_valid(): 
                form_model = form.save(commit=False) 
                form_model.save() 
                return self.form_valid(form)
        else:
                return self.form_invalid(form)
        
    def get_success_url(self) -> str:
        messages.success(self.request, 'O solicitacao foi Cadastrado com sucesso')
        return reverse_lazy('solicitacao-create')


# def solicitacao_create_view(request):
#     form = solicitacaoForm() 
#     if request.method == 'POST':
#         form = solicitacaoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('solicitacao_add') 
#     return render(request, 'end/home.html', {'form': form})

class SolicitacaoUpdate(UpdateView):
        model = Solicitacao 
        form_class = solicitacaoForm 
        template_name = 'end/home.html'   
        success_url = reverse_lazy('solicitacao-create')
        success_message = 'O solicitação foi Atualizado com sucesso'
    


# def solicitacao_update_view(request, pk):
#     solicitacao = get_object_or_404(Solicitacao, pk=pk)
#     form = solicitacaoForm(instance=solicitacao)
#     if request.method == 'POST':
#         form = solicitacaoForm(request.POST, instance=solicitacao)
#         if form.is_valid():
#             form.save()
#             return redirect('solicitacao_change', pk=pk)
#     return render(request, 'end/home.html', {'form': form})

 
class Load_empresas(ListView):
        model = Solicitacao 
        form_class = solicitacaoForm 
        template_name = 'end/enderecos.html'   
        
        def get(self, request):
                empresas_id = request.GET.get('empresas_id')
                enderecos = Endereco.objects.filter(empresas_id=empresas_id).all()
                return render(request, 'end/enderecos.html', {'enderecos': enderecos})
             

# AJAX
# def load_empresas(request):
#     empresas_id = request.GET.get('empresas_id')
#     enderecos = Endereco.objects.filter(empresas_id=empresas_id).all()
#     return render(request, 'end/enderecos.html', {'enderecos': enderecos})

