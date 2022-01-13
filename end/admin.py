from django.contrib import admin

# Register your models here.
from end.models import Endereco, Solicitacao, Empresas

admin.site.register(Empresas)
admin.site.register(Endereco)
admin.site.register(Solicitacao)