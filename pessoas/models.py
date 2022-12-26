from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    email = models.EmailField()
    apelido = models.CharField(max_length=100,blank=True)
    observação = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.nome_pessoa