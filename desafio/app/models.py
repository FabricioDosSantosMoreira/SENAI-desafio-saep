from django.db import models

from app.enums import Prioridade, Status


class Usuario(models.Model):

    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    nome_setor = models.CharField(max_length=255)
    descricao = models.TextField()

    prioridade = models.CharField(
        max_length=12,
        choices=Prioridade.choices
    )
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.FAZER
    )
