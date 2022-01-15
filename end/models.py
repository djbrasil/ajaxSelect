from re import T
from django.db import models

class ClienteSolicitacoes(models.Model): 
        client_namefull = models.CharField(max_length=200)
        client_email = models.EmailField(max_length=150)
        client_cnpjcpf = models.CharField(max_length=16) 
        client_error = models.TextField(max_length=300)
 
        def __str__(self):
                return self.client_namefull
        
        class Meta:
                verbose_name = "client_namefull"
                verbose_name_plural = "client_namefull"
                ordering = ['client_namefull']

class Empresas(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Endereco(models.Model):
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE, related_name="endereco")
    name = models.CharField(max_length=40) 
    c_cep = models.CharField(max_length=10)
    c_road = models.CharField(max_length=200)
    c_district = models.CharField(max_length=200)
    c_complement = models.CharField(max_length=30)
    c_number = models.CharField(max_length=5)
    c_city = models.CharField(max_length=20)
    c_uf = models.CharField(max_length=2)
        
    def __str__(self):
        return self.name


class Solicitacao(models.Model):
    cliente = models.ForeignKey(ClienteSolicitacoes, on_delete=models.CASCADE, related_name="cliente", blank=True, null=True)
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE, related_name="solicitacao") 
    text = models.TextField()

    def __str__(self):
        return self.cliente
     