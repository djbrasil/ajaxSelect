from django.db import models


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
    name = models.CharField(max_length=124)
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE, related_name="solicitacao") 
    text = models.TextField()

    def __str__(self):
        return self.name
     