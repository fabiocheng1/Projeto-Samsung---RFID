from django.db import models

class Compra(models.Model):
    data = models.DateTimeField()
    forma_pagamento = models.CharField(max_length=15)
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)


class Usuario(models.Model):

    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=10)

class ItemCompra(models.Model):

    qtd = models.IntegerField()
    Fk_Compra = models.ForeignKey('Compra', on_delete=models.DO_NOTHING)
    Fk_Produto = models.ForeignKey('Produto', on_delete=models.DO_NOTHING)

