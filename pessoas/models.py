from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField(default=datetime.now, blank=True)
    email = models.EmailField()
    apelido = models.CharField(max_length=100)
    observação = models.CharField(max_length=100)