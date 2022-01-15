from email.message import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.contrib import messages  
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView  
from django.shortcuts import render 
from django.template.defaultfilters import slugify
from .forms import solicitacaoForm, ClienteSolicitacoesForm
from .models import ClienteSolicitacoes, Empresas, Solicitacao, Endereco

class SolicitacaoNewView(CreateView):
        model = ClienteSolicitacoes
        form_class = ClienteSolicitacoesForm
        template_name = 'end/solicitacao-novo.html'
        success_url = reverse_lazy('home')
        success_message = 'Solicitação cadastrada com sucesso'
        
class SolicitacaoListView(ListView):
        model = ClienteSolicitacoes
        template_name = 'end/solicitacao-view.html'  
        paginate_by = 9
        context_object_name = 'solicitacao'

class SolicitacaoCreate(CreateView):
        model = Solicitacao 
        form_class = solicitacaoForm 
        template_name = 'end/_send.html' 

        def get(self, request, pk, *args, **kwargs):  
                form = solicitacaoForm() 
                cliente = ClienteSolicitacoes.objects.get(pk=pk)
                solicitacao = Solicitacao.objects.all() 
                context = { 'solicitacao':solicitacao, 'form':form, 'cliente':cliente}   
                return render(request, self.template_name, context)
         
        def post(self, request, *args, **kwargs):
                solicitacao = ClienteSolicitacoes.objects.filter(pk=kwargs['pk'])    
                form = self.get_form() 
                if form.is_valid():  
                        form_model = form.save(commit=False) 
                        form_model.cliente = solicitacao[0]   
                        form_model.save()   
                        
                        email_context = {
                                'cliente': solicitacao[0],
                                'empresas': form.cleaned_data.get('empresas'),
                                'text': form.cleaned_data.get('text'), 
                        } 
                        
                        # Envia Email para cliente do local da assistencia que precisa levar o equipamento.
                        email = solicitacao[0].client_email # pega email do cliente 
                        message = get_template('end/BODY_EMAIL.html').render(email_context)
                        msg = EmailMessage('Assistencia tecnica', message,'EMAIL CONFIG SETTINGS', str[email])
                        msg.content_subtype = "html" 
                        msg.send()
                        print("E-mail enviado com sucesso")
                        
                        return self.form_valid(form)
                else:
                        return self.form_invalid(form) 
        
        def get_success_url(self) -> str:
                messages.success(self.request, 'O Email foi Cadastrado com sucesso')
                return reverse_lazy('home')
 

class SolicitacaoUpdate(UpdateView):
        model = Solicitacao 
        form_class = solicitacaoForm 
        template_name = 'end/home.html'   
        success_url = reverse_lazy('home')
        success_message = 'O solicitação foi Atualizado com sucesso'
      
class Load_empresas(ListView):
        model = Solicitacao 
        form_class = solicitacaoForm 
        template_name = 'end/enderecos.html'   
        
        def get(self, request):
                empresas_id = request.GET.get('empresas_id')
                enderecos = Endereco.objects.filter(empresas_id=empresas_id).all()
                return render(request, 'end/enderecos.html', {'enderecos': enderecos})
              