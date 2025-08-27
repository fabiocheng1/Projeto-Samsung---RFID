from django.db import models

class Compra(models.Model):
    data = models.DateTimeField()
    forma_pagamento = models.CharField(max_length=15)
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)

